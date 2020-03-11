from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    
