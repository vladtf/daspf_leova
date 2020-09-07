import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from daspf_app.forms import PostForm, PageDataForm, ImageForm, MessageForm
from daspf_app.models import *


def page(request, name='acasa'):
    form = {}
    page = Page.objects.get(name=name)

    if request.user.is_authenticated:
        form = PageDataForm(request.POST or None, request.FILES or None, initial={
            'body': page.body,
        })

        if form.is_valid():
            page.body = form.cleaned_data['body']
            page.created_by = request.user

            page.save()

    context = {'form': form, 'page': page}
    return render(request, 'views/index.html', context=context)


def post_index(request, category=''):
    search_query = request.GET.get('search') or ''

    post_list = Post.objects.all() \
        .filter(Q(title__icontains=search_query) | Q(body__icontains=search_query), visible=True,
                category__name__icontains=category) \
        .order_by('-created_at')

    post_list = paginate(request, post_list)
    context = {'posts': post_list}
    return render(request, 'views/post/post_index.html', context=context)


def post_show(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)

    images = PostImage.objects.filter(post=post)

    context = {
        'post': post,
        'images': images
    }
    return render(request, 'views/post/post_show.html', context=context)


@login_required(login_url='post_index', redirect_field_name='')
def post_create(request):
    # client_id = settings.IMGUR_CLIENT_ID
    # client_secret = settings.IMGUR_CLIENT_SECRET
    #
    # if request.method != 'POST':
    #     client = ImgurClient(client_id=client_id, client_secret=client_secret)
    #     auth_url = client.get_auth_url('token')
    #     return redirect(auth_url)
    # imgur_client = get_imgur_client(request, client_id, client_secret)
    #
    # if imgur_client:
    #     imgur_client.upload_from_url(url='/images/student_faculty_view_ROeeYKg.png')

    post = Post(created_by=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    ImageFormSet = modelformset_factory(PostImage, form=ImageForm, extra=3)
    formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=PostImage.objects.none())

    if form.is_valid() and formset.is_valid():
        post = form.save()

        for image_form in formset.cleaned_data:
            if 'image' in image_form:
                image = image_form['image']
                PostImage.objects.create(image=image, post=post)

        return redirect('post_index')

    context = {'form': form, 'formset': formset}
    return render(request, 'views/post/post_edit.html', context=context)


# def get_imgur_client(request, client_id, client_secret):
#     data = json.loads(request.body)
#
#     access_token = data['access_token']
#     expires_in = data['expires_in']
#     token_type = data['token_type']
#     refresh_token = data['refresh_token']
#     account_username = data['account_username']
#     account_id = data['account_id']
#
#     if access_token and refresh_token:
#         client = ImgurClient(client_id=client_id, client_secret=client_secret, access_token=access_token,
#                              refresh_token=refresh_token)
#         return client
#
#     return {}
#
#     # driver.get(auth_url)
#     #
#     # token = request.GET.get('acces_token')
#     # client.authorize(token, 'token')
#     # client.authorize()
#     # auth_url = client.get_auth_url('token')
#     #
#     # credentials = client.authorize('TOKEN OBTAINED FROM AUTHORIZATION', 'token')
#     # client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
#     # uploaded_image = client.image_upload(filename='http://127.0.0.1:8000/images/student_faculty_view_ROeeYKg.png', description="None", title="Untitled")
#     # imgur.upload_from_url(url='/images/student_faculty_view_ROeeYKg.png')
#     # image_id = uploaded_image['response']['data']['id']
#     # print(uploaded_image.link)


@login_required(login_url='post_index', redirect_field_name='')
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    ImageFormSet = modelformset_factory(PostImage, form=ImageForm, extra=0)
    formset = ImageFormSet(request.POST or None, request.FILES or None, queryset=post.get_post_images)

    if form.is_valid():
        form.save()
        return redirect('post_index')

    context = {'form': form, 'formset': formset}
    return render(request, 'views/post/post_edit.html', context=context)


@login_required(login_url='post_index', redirect_field_name='')
def post_delete(request):
    data = json.loads(request.body)

    post_id = data.get('post_id')
    action = data.get('action')

    message = 'Unknown action'
    redirect = reverse('post_index')

    if action == 'edit':
        Post.objects.get(id=post_id).delete()
        message = 'Post deleted successfully!'

    if action == 'create':
        message = 'Post create abandoned'
        redirect = reverse('post_create')

    return HttpResponse(json.dumps({
        "message": message,
        "redirect": redirect
    }), content_type="application/json")


def contacts(request):
    message = Message()
    form = MessageForm(request.POST or None, request.FILES or None, instance=message)

    alert_message = ''
    alert_flag = False

    if form.is_valid():
        form.save()

        alert_flag = True
        alert_message = 'Mesaj trimis cu succes.'

        form = MessageForm()

    context = {'form': form, 'alert_message': alert_message, 'alert_flag': alert_flag}
    return render(request, 'views/contacts.html', context=context)


@login_required(login_url='post_index', redirect_field_name='')
def message_index(request):
    email = request.GET.get('email', '')
    text = request.GET.get('text', '')

    message_list = Message.objects.order_by('-created_at')

    if email or text:
        message_list = Message.objects.filter(Q(email__icontains=email) & Q(text__icontains=text)) \
 \
            # if email:
    #     message_list = message_list.filter(email__icontains=email)
    # if text:
    #     message_list = message_list.filter(text__icontains=text)

    message_list = paginate(request, message_list, items_per_page=17)

    context = {'messages': message_list}

    return render(request, 'views/message/message_index.html', context=context)


@login_required(login_url='post_index', redirect_field_name='')
def message_show(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    context = {"message": message}
    return render(request, 'views/message/message_show.html', context=context)


def paginate(request, items_list, items_per_page=4):
    page = request.GET.get('page', 1)
    paginator = Paginator(items_list, items_per_page)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    return items
