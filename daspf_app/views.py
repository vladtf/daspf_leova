from itertools import chain

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404

from daspf_app.forms import PostForm, PageDataForm, PostFullForm, ImageForm, MessageForm
from daspf_app.models import Post, Category, PostImage, Message


def home(request):
    form = {}
    home = Post.objects.get(category=Category.objects.get(name='Acasa'))

    if request.user.is_authenticated:
        form = PageDataForm(request.POST or None, request.FILES or None, initial={
            'title': home.title,
            'body': home.body,
        })

        if form.is_valid():
            home.body = form.cleaned_data['body']
            home.title = form.cleaned_data['title']
            home.created_by = request.user

            home.save()

    context = {'form': form, 'home': home}
    return render(request, 'views/home.html', context=context)


def post_index(request):
    search_query = request.GET.get('search') or ''

    post_list = Post.objects.all() \
        .filter(Q(title__icontains=search_query) | Q(body__icontains=search_query), visible=True) \
        .order_by('-created_at')

    posts = paginate(request, post_list)
    context = {'posts': posts}
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


def events(request):
    post_list = Post.objects.all().filter(category=Category.objects.get(name='Evenimente'), visible=True).order_by(
        '-created_at')

    posts = paginate(request, post_list)
    context = {'posts': posts}
    return render(request, 'views/post/post_index.html', context=context)


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
    messages = Message.objects.all().order_by('-created_at')

    context = {'messages': messages}

    return render(request, 'views/message/message_index.html', context=context)


@login_required(login_url='post_index', redirect_field_name='')
def message_show(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    context = {"message": message}
    return render(request, 'views/message/message_show.html', context=context)


def paginate(request, post_list, post_per_page=4):
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, post_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts
