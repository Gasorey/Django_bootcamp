from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView
from app_basico.models import escola,estudante
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class escolas(ListView):
    model = escola
    context_object_name = 'escolas'


class escola_detalhe(DetailView):
    context_object_name = 'detalhes'
    model = escola
    template_name = 'app_basico/detalhes_escolas.html'


    
