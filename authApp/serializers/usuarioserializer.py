from authApp.models.usuario import Usuario
from rest_framework import serializers

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'perfil', 'nombre', 'apellidos', 'telefono', 'genero')