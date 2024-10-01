from rest_framework.viewsets import ModelViewSet

from casafeita.models import Fabricante
from casafeita.serializers import FabricanteSeralizer

class FabricanteViewSet(ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSeralizer
    