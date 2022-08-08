from rest_framework import viewsets
from controleFinanceiro.models import Despesa, Receita
from controleFinanceiro.serializer import DespesaSerializer, ReceitaSerializer


class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class ReceitasViewSet (viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
