from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Topic, ChatRoom, Message
from .forms import TopicForm, ChatRoomForm, MessageForm

def home(request):
    topics = Topic.objects.all()[:5]
    recent_rooms = ChatRoom.objects.all().order_by('-updated_at')[:5]
    context = {
        'topics': topics,
        'recent_rooms': recent_rooms,
    }
    return render(request, 'chat/home.html', context)

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'chat/topic_list.html', {'topics': topics})

@login_required
def topic_create(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.created_by = request.user
            topic.save()
            messages.success(request, 'Topic created successfully!')
            return redirect('topic_detail', pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'chat/topic_form.html', {'form': form})

def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    rooms = topic.chat_rooms.all()
    return render(request, 'chat/topic_detail.html', {
        'topic': topic,
        'rooms': rooms
    })

def chat_room_list(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/chat_room_list.html', {'rooms': rooms})

@login_required
def chat_room_create(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_by = request.user
            room.save()
            room.participants.add(request.user)
            messages.success(request, 'Chat room created successfully!')
            return redirect('chat_room_detail', pk=room.pk)
    else:
        form = ChatRoomForm()
    return render(request, 'chat/chat_room_form.html', {'form': form})

@login_required
def chat_room_detail(request, pk):
    room = get_object_or_404(ChatRoom, pk=pk)
    messages = room.messages.all()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.user = request.user
            message.save()
            return redirect('chat_room_detail', pk=pk)
    else:
        form = MessageForm()
    
    if request.user not in room.participants.all():
        room.participants.add(request.user)
    
    return render(request, 'chat/chat_room_detail.html', {
        'room': room,
        'messages': messages,
        'form': form
    })

def search(request):
    query = request.GET.get('q', '')
    if query:
        topics = Topic.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        rooms = ChatRoom.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        messages = Message.objects.filter(content__icontains=query)
    else:
        topics = Topic.objects.none()
        rooms = ChatRoom.objects.none()
        messages = Message.objects.none()
    
    return render(request, 'chat/search_results.html', {
        'query': query,
        'topics': topics,
        'rooms': rooms,
        'messages': messages
    })
