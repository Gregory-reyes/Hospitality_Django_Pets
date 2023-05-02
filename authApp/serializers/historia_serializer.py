from authApp.models.historia_clinica import Historia_clinica
from rest_framework import serializers

class Historia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_clinica
        fields = ('id_paciente', 'sugerencias_cuidado', 'diagnostico', 'entorno', 'fecha_sugerencia','descripcion', 'diagnostico')
        