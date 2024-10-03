from rest_framework.viewsets import ModelViewSet

from casafeita.models import Cor
from casafeita.serializers import CorSeralizer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSeralizer
    