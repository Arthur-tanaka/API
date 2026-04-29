# transactions/models.py

from django.db import models

class Transaction(models.Model):
    TYPE_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )

    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateField()
    tipo = models.CharField(max_length=10,choices=TYPE_CHOICES)