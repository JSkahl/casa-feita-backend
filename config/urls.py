from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter

from casafeita.views import (AvaliacaoViewSet, CartaoViewSet, CategoriaViewSet, CompraViewSet, CorViewSet, FabricanteViewSet, ProdutoViewSet, UsuarioViewSet)

router = DefaultRouter()
router.register(r"avaliações", AvaliacaoViewSet, basename="avaliações")
router.register(r"cartões", CartaoViewSet, basename="cartões")
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"compras", CompraViewSet, basename="compras")
router.register(r"cores", CorViewSet, basename="cores")
router.register(r"fabricantes", FabricanteViewSet, basename="fabricantes")
router.register(r"produtos", ProdutoViewSet, basename="produtos")
router.register(r"usuários", UsuarioViewSet, basename="usuários")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/media/", include(uploader_router.urls)),
    path("api/", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)