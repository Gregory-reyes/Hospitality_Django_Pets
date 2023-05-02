from rest_framework import status, views
from rest_framework.response import Response

from authApp.serializers.signos_serializer import Signos_Serializer

class CrearSignosView(views.APIView):
    def post(self,request):
        serializers = Signos_Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 