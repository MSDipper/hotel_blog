from urllib.parse import urlparse
from django.shortcuts import render
from about.models import *
from django.views.generic import ListView


class AboutListView(ListView):
    model = About
    template_name = 'about/about_list.html'