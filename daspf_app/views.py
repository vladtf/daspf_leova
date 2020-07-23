from django.http import HttpResponse
from django.shortcuts import render

from daspf_app.models import Post


def index(request):
    news = Post.objects.all().filter(visible=True).order_by('-created_at')
    context = {'posts': news}
    return render(request, 'views/index.html', context=context)


def contacts(request):
    context = {}
    return render(request, 'views/contacts.html', context=context)
