from django.shortcuts import render
from django.views.generic import ListView
from rooms.models import Room, Rating


class RoomListView(ListView):
    model = Room
    template_name = 'room/room_list.html'
