from django.urls import path,include
from app_basico import views
from django.conf.urls import url

app_name = 'app_basico'

urlpatterns = [
    path('',views.escolas.as_view(),name='escola_list'),
    url(r'^(?P<pk>\d+)/$',views.escola_detalhe.as_view(),name='detalhes_escolas'),
    url(r'^criar/$',views.criar_escola.as_view(),name='criar'),
    url(r'^update/(?P<pk>\d+)/$',views.update_escola.as_view(),name='update_escola'),
    url(r'^deletar/(?P<pk>\d+)/$',views.deletar_escola.as_view(),name='deletar_escola')

]
