from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acasa/', views.home, name='home'),
    path('evenimente/', views.events, name='events'),
    path('contacte/', views.contacts, name='contacts'),
    path('postare/<int:post_id>', views.post, name='post'),
    path('postare/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('postare/create', views.post_create, name='post_create'),
]
