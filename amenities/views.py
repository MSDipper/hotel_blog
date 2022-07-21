from django.shortcuts import render
from amenities.models import Amenities

from django.views.generic import *

class AmenitiesListView(ListView):
    model = Amenities
    template_name = 'amenities/services_list.html'