from django.db import models
from .paciente import Paciente

class Historia_clinica(models.Model):
    id_histClinica = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='historia_clinica', on_delete=models.CASCADE)
    sugerencias_cuidado = models.CharField('Sugerencias_cuidado', max_length=250)
    diagnostico = models.CharField('Diagnostico', max_length=250)
    entorno = models.CharField('Entorno', max_length=250)
    fecha_sugerencia = models.DateField()
    descripcion = models.CharField('Diagnostico', max_length=100)