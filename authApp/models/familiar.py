from django.db import models
from .usuario import Usuario
from .paciente import Paciente

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length=35)
    correo = models.EmailField('Correo', max_length=100)