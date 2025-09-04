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

     # Busca de um valor
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, atual, valor):
        if atual is None:
            return None
        if atual.valor == valor:
            return atual
        elif valor < atual.valor:
            return self._buscar(atual.esquerda, valor)
        else:
            return self._buscar(atual.direita, valor)

    # Remoção de um nó
    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, atual, valor):
        if atual is None:
            return None

        if valor < atual.valor:
            atual.esquerda = self._remover(atual.esquerda, valor)
        elif valor > atual.valor:
            atual.direita = self._remover(atual.direita, valor)
        else:
            # Caso 1: nó folha
            if atual.esquerda is None and atual.direita is None:
                return None
            # Caso 2: um filho
            elif atual.esquerda is None:
                return atual.direita
            elif atual.direita is None:
                return atual.esquerda
            # Caso 3: dois filhos
            else:
                sucessor = self._minimo(atual.direita)
                atual.valor = sucessor.valor
                atual.direita = self._remover(atual.direita, sucessor.valor)

        return atual

    def _minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    # Altura da árvore
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return -1
        return 1 + max(self._altura(no.esquerda), self._altura(no.direita))

    # Profundidade de um nó
    def profundidade(self, valor):
        return self._profundidade(self.raiz, valor, 0)

    def _profundidade(self, atual, valor, nivel):
        if atual is None:
            return -1
        if atual.valor == valor:
            return nivel
        elif valor < atual.valor:
            return self._profundidade(atual.esquerda, valor, nivel + 1)
        else:
            return self._profundidade(atual.direita, valor, nivel + 1)