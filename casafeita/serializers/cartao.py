from rest_framework.serializers import ModelSerializer

from casafeita.models import Cartao

class CartaoSerializer(ModelSerializer):
    class Meta:
        model = Cartao
        fields = '__all__'