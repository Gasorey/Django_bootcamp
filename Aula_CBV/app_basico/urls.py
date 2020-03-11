from django.urls import path,include
from app_basico import views
from django.conf.urls import url

app_name = 'app_basico'

urlpatterns = [
    path('',views.escolas.as_view(),name='escola_list'),
    url(r'^(?P<pk>[-\w]+)/$',views.escola_detalhe.as_view(),name='detalhes_escolas'),
]
