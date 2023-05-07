from urllib import request,response
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.usuarioserializer import UsuarioSerializer

class CrearUsuarioView(views.APIView):
    def post(self, request, *args, **kwargs):
            serializer = UsuarioSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            tokenData = {"username":request.data["username"],
                        "password":request.data["password"]}
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)                      
            if tokenSerializer.is_valid():
                return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 