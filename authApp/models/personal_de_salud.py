from django.db import models
from .usuario import Usuario

class Personal_salud(models.Model):
    id_personalsalud = models.AutoField(primary_key=True)
    id_user = models.OneToOneField(Usuario, related_name='personal_de_salud', on_delete= models.CASCADE)
    rol = models.CharField('Rol', max_length=30)
    especialidad = models.CharField('Especialidad', max_length=40)