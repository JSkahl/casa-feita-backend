from rest_framework.serializers import ModelSerializer
from casafeita.models import Avaliacao

class AvaliacaoSeralizer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'