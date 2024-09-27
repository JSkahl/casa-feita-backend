from rest_framework.serializers import ModelSerializer
from casafeita.models import Categoria

class CategoriaSeralizer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'