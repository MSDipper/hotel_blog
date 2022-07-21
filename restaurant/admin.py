from django.contrib import admin

from restaurant.models import *

@admin.register(CategoryMenu)
class CategoryMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    save_as = True
    save_on_top = True

@admin.register(RangeMenu)
class RangeMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True