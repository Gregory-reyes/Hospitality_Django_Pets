from authApp.models.paciente import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id_personalsalud','id_user','ciudad','fecha_nacimiento','direccion')