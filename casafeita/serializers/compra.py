from rest_framework.serializers import ModelSerializer
from casafeita.models import Compra

class CompraSeralizer(ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'