from rest_framework.viewsets import ModelViewSet

from casafeita.models import Cartao
from casafeita.serializers import CartaoSerializer

class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    