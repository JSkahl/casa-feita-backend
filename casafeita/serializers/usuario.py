from rest_framework.serializers import ModelSerializer, SlugRelatedField

from casafeita.models import Usuario
from uploader.models import Image
from uploader.serializers import ImageSerializer

class UsuarioSerializer(ModelSerializer):
    avatar_attachment_key = SlugRelatedField(source="avatar", queryset=Image.objects.all(), slug_field="attachment_key", required=False, write_only=True)

    avatar = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'