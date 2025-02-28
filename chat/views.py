from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage

@login_required
def index(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {
        'chat_rooms': chat_rooms
    })

@login_required
def room(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = ChatMessage.objects.filter(room=room)[:100]
    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages
    })