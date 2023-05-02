from authApp.models.signos_vitales import Signos_vitales
from rest_framework import serializers

class Signos_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Signos_vitales
        fields = ('id_paciente','oximetria', 'frecuencia_respiratoria', 'frecuencia_cardiaca',
         'temperatura','glicemias','presion_arterial','fecha_hora')