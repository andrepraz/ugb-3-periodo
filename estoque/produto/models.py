from django.db import models

class Cores(models.Model):
    cor = models.CharField('Cor', max_length=200)

    def __str__(self) -> str:
        return self.cor

class Produtos(models.Model):
    produto = models.CharField('Produto', max_length=200)
    cor = models.ForeignKey(Cores, on_delete=models.PROTECT)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=0)
    quantidade = models.IntegerField('Quantidade', default=0)

    def __str__(self) -> str:
        return self.produto
