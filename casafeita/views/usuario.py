from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from casafeita.models import Usuario
from casafeita.serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        usuario = request.usuario
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data, status=status.HTTP_200_OK)