from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView,DetailView,ListView,View, CreateView,UpdateView,DeleteView
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

class criar_escola(CreateView):
    fields = ('nome','local','email')
    model = escola
    

class update_escola(UpdateView):
     fields = ('nome','email')
     model = escola

class deletar_escola(DeleteView):
    model = escola
    success_url = reverse_lazy('app_basico:escola_list')