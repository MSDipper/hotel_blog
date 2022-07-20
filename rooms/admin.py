from django.contrib import admin

from rooms.models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True


@admin.register(RoomStar)
class RoomStarAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    save_on_top = True