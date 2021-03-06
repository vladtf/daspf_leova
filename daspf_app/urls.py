from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('postari/<str:category>/', views.post_index, name='post_index_category'),
    path('postare/<int:post_id>', views.post_show, name='post_show'),
    path('postare/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('postare/create', views.post_create, name='post_create'),
    path('postare/delete', views.post_delete, name='post_delete'),

    path('index/<str:name>', views.page, name='index'),
    path('index/', views.page),

    path('contacte/', views.contacts, name='contacts'),

    path('messages/', views.message_index, name='message_index'),
    path('messages/show/<int:message_id>', views.message_show, name='message_show'),
]
