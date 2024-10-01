from rest_framework.serializers import ModelSerializer, SerializerMethodField
from casafeita.models import Compra, Endereco, ItemCompra

class CompraSeralizer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class ItemCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.produto.preco * instance.quantidade
    
    class Meta:
        model = ItemCompra
        fields = '__all__'
        depth = 1

class CompraDetailSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        depth = 1
