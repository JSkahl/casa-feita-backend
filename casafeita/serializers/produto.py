from rest_framework.serializers import ModelSerializer

from casafeita.models import Produto

class ProdutoSeralizer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1