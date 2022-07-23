from django.shortcuts import render
from contact.models import OurAddress 
from django.views.generic import ListView

class ContactListView(ListView):
    model = OurAddress
    template_name = 'contact/contact_list.html'


