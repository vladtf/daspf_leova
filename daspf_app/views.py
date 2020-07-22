from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'views/index.html', context=context)


def contacts(request):
    context = {}
    return render(request, 'views/contacts.html', context=context)
