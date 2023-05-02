from rest_framework import views
from rest_framework.response import Response

from authApp.serializers.pacienteserializer import PacienteSerializer
from authApp.models.paciente import Paciente

class ConsultaPacienteView(views.APIView):
    
    def get (self, request, pk, format=None):
        modelo = Paciente.objects.get(pk=pk)
        serializers = PacienteSerializer(modelo)
        return Response(serializers.data)