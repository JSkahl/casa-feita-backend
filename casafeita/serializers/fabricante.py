from rest_framework.serializers import ModelSerializer
from casafeita.models import Fabricante

class FabricanteSeralizer(ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'