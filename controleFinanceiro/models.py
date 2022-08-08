from django.db import models

class Despesa (models.Model):
    descricao = models.CharField (max_length = 10)
    valor =  models.DecimalField (max_digits=10, decimal_places=2)
    data = models.DateField ()
    def __str__():
        return self.descricao


class Receita (models.Model):
    descricao = models.CharField (max_length = 10)
    valor =  models.DecimalField (max_digits=10, decimal_places=2)
    data = models.DateField ()
    def __str__():
        return self.descricao
