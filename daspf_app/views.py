from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from daspf_app.forms import PostForm, PageDataForm
from daspf_app.models import Post, Category, PostImage


def index(request):
    post_list = Post.objects.all().filter(visible=True).order_by('-created_at')

    posts = paginate(request, post_list)
    context = {'posts': posts}
    return render(request, 'views/post/post_index.html', context=context)


def events(request):
    post_list = Post.objects.all().filter(category=Category.objects.get(name='Evenimente'), visible=True).order_by(
        '-created_at')

    posts = paginate(request, post_list)
    context = {'posts': posts}
    return render(request, 'views/events.html', context=context)


def post(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    images = PostImage.objects.filter(post=post)

    context = {
        'post': post,
        'images': images
    }

    return render(request, 'views/post/post_show.html', context=context)


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('index')

    post = Post(created_by=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'views/post/post_edit.html', context=context)


def post_edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('index')

    try:
        post = Post.objects.get(id=post_id)
        form = PostForm(request.POST or None, request.FILES or None, instance=post)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {'form': form}
        return render(request, 'views/post/post_edit.html', context=context)

    except Post.DoesNotExist:
        return redirect('index')


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


def contacts(request):
    context = {}
    return render(request, 'views/contacts.html', context=context)


def paginate(request, post_list):
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts
