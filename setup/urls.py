from django.contrib import admin
from django.urls import path, include
from controleFinanceiro.views import DespesasViewSet,ReceitasViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('despesas', DespesasViewSet,basename='Despesas')
router.register('receitas', ReceitasViewSet, basename='Receitas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]