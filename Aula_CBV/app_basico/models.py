from django.db import models
from django.urls import reverse
# Create your models here.

class escola(models.Model):
    nome = models.CharField(max_length=256)
    local = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('app_basico:detalhes_escolas',kwargs={'pk':self.pk})



class estudante(models.Model):
    nome = models.CharField(max_length=256)
    escola = models.ForeignKey('escola',on_delete=models.CASCADE,related_name='estudantes' )
    idade = models.PositiveIntegerField()

    
