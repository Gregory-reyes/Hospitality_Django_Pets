from django.db import models
from .paciente import Paciente


class Signos_vitales(models.Model):
    id_signos_vitales = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='signos_vitales', on_delete=models.CASCADE)
    oximetria = models.CharField('Oximetria', max_length=20)
    frecuencia_respiratoria = models.CharField('Frecuencia_respiratoria', max_length=20)
    frecuencia_cardiaca = models.CharField('Frecuencia_cardiaca', max_length=20)
    temperatura = models.CharField('Temperatura', max_length=20)
    glicemias = models.CharField('Glicemias', max_length=20)
    presion_arterial = models.CharField('Presion_arterial', max_length=20)
    fecha_hora = models.DateField()
