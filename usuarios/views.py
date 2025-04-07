from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuarios
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def criar_usuario(request):
    telefone = request.data.get('telefone')

    if not telefone:
         return Response({'Erro': 'Campos obrigatorios incompleto'}, status = status.HTTP_400_BAD_REQUEST)
    if Usuarios.objects.filter(telefone=telefone).exists():
          return Response({'Erro': f'Telefone{telefone} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuarios.objects.create_user(
         telefone = telefone,
    )
    return Response({'Mensagem': f'Usuario {telefone} criado com sucesso' }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar_usuario(request):
    telefone = request.data.get('telefone')

    usuario = authenticate(telefone = telefone)

    if usuario:
        refresh = RefreshToken.for_user(usuario)

        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str (refresh)
        }, status = status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuario ou/e senha incorreto(s)'},status=status.HTTP_401_UNAUTHORIZED) 
    