from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evenimente/', views.events, name='events'),
    path('contacte/', views.contacts, name='contacts'),
]
