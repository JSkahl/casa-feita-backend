from rest_framework.viewsets import ModelViewSet

from casafeita.models import Produto
from casafeita.serializers import ProdutoSeralizer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSeralizer
    