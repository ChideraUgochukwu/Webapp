from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topic_list, name='topics'),
    path('topics/create/', views.topic_create, name='topic_create'),
    path('topics/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('chat-rooms/', views.chat_room_list, name='chat_rooms'),
    path('chat-rooms/create/', views.chat_room_create, name='chat_room_create'),
    path('chat-rooms/<int:pk>/', views.chat_room_detail, name='chat_room_detail'),
    path('search/', views.search, name='search'),
]
