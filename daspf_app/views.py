from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from daspf_app.models import Post, Category


def index(request):
    post_list = Post.objects.all().filter(visible=True).order_by('-created_at')

    posts = paginate(request, post_list)
    context = {'posts': posts}
    return render(request, 'views/index.html', context=context)


def events(request):
    post_list = Post.objects.all().filter(category=Category.objects.get(name='Evenimente'), visible=True).order_by(
        '-created_at')

    posts = paginate(request, post_list)
    context = {'posts': posts}
    return render(request, 'views/events.html', context=context)


def post(request, post_id):

    try:
        post = Post.objects.get(id=post_id)

        context = {'post': post}
        return render(request, 'views/post.html', context=context)
    except Post.DoesNotExist:
        return redirect('index')


def home(request):
    context = {}
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
