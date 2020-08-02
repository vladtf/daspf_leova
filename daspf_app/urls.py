from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('postare/<int:post_id>', views.post_show, name='post_show'),
    path('postare/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('postare/create', views.post_create, name='post_create'),

    path('acasa/', views.home, name='home'),
    path('evenimente/', views.events, name='events'),
    path('contacte/', views.contacts, name='contacts'),

]
