from rest_framework.viewsets import ModelViewSet

from casafeita.models import Categoria
from casafeita.serializers import CategoriaSeralizer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSeralizer
    