from rest_framework.serializers import ModelSerializer
from casafeita.models import Cor

class CorSeralizer(ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'