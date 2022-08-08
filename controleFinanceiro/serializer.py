from rest_framework import serializers
from controleFinanceiro.models import Receita, Despesa

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['id','descricao','valor','data']

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id','descricao','valor','data']