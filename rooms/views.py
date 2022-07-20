from django.shortcuts import render

from django.views.generic import ListView

from rooms.models import Room


class RoomListView(ListView):
    model = Room
    template_name = 'room.html'