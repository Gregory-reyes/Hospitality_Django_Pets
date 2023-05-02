from authApp.models.personal_de_salud import Personal_salud
from rest_framework import serializers

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_salud
        fields = ('id_user', 'rol', 'especialidad')