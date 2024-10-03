from rest_framework.viewsets import ModelViewSet

from casafeita.models import Produto
from casafeita.serializers import ProdutoSerializer, ProdutoDetailSerializer, ProdutoListSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer