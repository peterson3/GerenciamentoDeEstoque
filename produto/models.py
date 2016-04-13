from __future__ import unicode_literals
from django.db import models
import time
import threading

# Create your models here.
processamentoEmExecucao = False


class Produto(models.Model):
    # Campos
    nome = models.CharField(max_length=100)
    qtd = models.IntegerField(default=0)
    precoMedio = models.FloatField(default=0)

    def __str__(self):
        if (self.qtd == 0):
            return (self.nome + " " +"QTD:"+ str(self.qtd) + "	S/PM")
        else:
            return (self.nome + " " + "QTD:"+ str(self.qtd) + "	PRECOMEDIO: " + str(self.precoMedio))


    def atualizarEstoque(self, qtdAdd, preco):
        if (self.qtd == 0):
            self.precoMedio = preco
            self.qtd = qtdAdd
            self.save(update_fields=["precoMedio", "qtd"])
        else:
            x = self.qtd * self.precoMedio
            y = qtdAdd * preco
            z = (x + y) / (self.qtd + qtdAdd)
            self.precoMedio = z
            self.qtd = self.qtd+qtdAdd
            self.save(update_fields=["precoMedio", "qtd"])


class CompraProduto(models.Model):
    # Campos
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.IntegerField()
    preco = models.FloatField()
    processado = models.IntegerField(default=-1)

    def __str__(self):
        return ('Produto: ' + self.produto.nome + ' Quantidade: ' + str(self.qtd) + " Preco: " + str(self.preco))

    def processarCompra(self):

        if self.processado == -1:
            while (processamentoEmExecucao == True):
                time.sleep(5)
            global processamentoEmExecucao
            processamentoEmExecucao = True
            self.processado = 0
            self.save(update_fields=["processado"])
            time.sleep(20)
            self.produto.atualizarEstoque(self.qtd, self.preco)
            self.processado = 1
            self.save(update_fields=["processado"])
            processamentoEmExecucao = False

        # processamentoEmExecucao=False
