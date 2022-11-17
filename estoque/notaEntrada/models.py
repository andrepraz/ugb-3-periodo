from django.db import models
from produto.models import Produtos

class NotasEntradas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=0)
    quantidade = models.IntegerField('Quantidade', default=0)

    criado = models.DateTimeField('criado', auto_now_add=True)
    modificado = models.DateTimeField('modificado', auto_now=True)

    def __str__(self) -> str:
        return self.produto.produto

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['produto']