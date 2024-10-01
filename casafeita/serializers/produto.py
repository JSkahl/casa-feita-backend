from rest_framework.serializers import ModelSerializer, SlugRelatedField

from casafeita.models import Produto
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ProdutoSeralizer(ModelSerializer):
    foto_attachment_key = SlugRelatedField(source="foto", queryset=Image.objects.all(), slug_field="attachment_key", required=False, write_only=True)

    foto = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'

class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1