from django.db import models
from .usuario import Usuario
from .personal_de_salud import Personal_salud


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_personalsalud = models.ForeignKey(Personal_salud, related_name='paciente', on_delete=models.CASCADE)
    id_user = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    ciudad = models.CharField('Ciudad', max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField('Direccion', max_length=100)