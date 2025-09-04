import random
from graphviz import Digraph


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # Inserção de um nó
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = No(valor)
            else:
                self._inserir(atual.esquerda, valor)
        else:
            if atual.direita is None:
                atual.direita = No(valor)
            else:
                self._inserir(atual.direita, valor)