from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from daspf_app.models import Post, Category


def index(request):
    post_list = Post.objects.all().filter(visible=True).order_by('-created_at')

    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'views/index.html', context=context)


def events(request):
    post_list = Post.objects.all().filter(category=Category.objects.get(name='Evenimente'), visible=True).order_by(
        '-created_at')

    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'views/events.html', context=context)


def home(request):
    context = {}
    return render(request, 'views/home.html', context=context)


def contacts(request):
    context = {}
    return render(request, 'views/contacts.html', context=context)
