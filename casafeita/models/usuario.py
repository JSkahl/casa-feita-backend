from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from uploader.models import Image

class GerenciadorUsuario(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Usuários necessitam de um endereço de email.")
        
        usuario = self.model(email=self.normalize_email(email), **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(email, password)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)

        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    class TipoUsuario(models.IntegerChoices):
        CLIENTE = 1, 'Cliente'
        VENDEDOR = 2, 'Vendedor'
        GERENTE = 3, 'Gerente'

    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=255, unique=True)
    sobrenome = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    tipo_usuario = models.IntegerField(choices=TipoUsuario.choices, default=TipoUsuario.CLIENTE)
    avatar = models.ForeignKey(Image, related_name="+", on_delete=models.SET_NULL, blank=True, null=True)
    objects = GerenciadorUsuario()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"