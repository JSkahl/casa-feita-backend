from rest_framework.viewsets import ModelViewSet

from casafeita.models import Compra, ItemCompra, Endereco
from casafeita.serializers import CompraSeralizer, ItemCompraSerializer, EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSeralizer
    
class ItemCompraViewSet(ModelViewSet):
    queryset = ItemCompra.objects.all()
    serializer_class = ItemCompraSerializer