from rest_framework.viewsets import ModelViewSet

from casafeita.models import Avaliacao
from casafeita.serializers import AvaliacaoSeralizer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSeralizer
    