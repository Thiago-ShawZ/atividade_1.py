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

    # -------- Métodos de Travessia --------
    
    def inorder(self):
        return self._inorder(self.raiz)

    def _inorder(self, no):
        if no is None:
            return []
        return self._inorder(no.esquerda) + [no.valor] + self._inorder(no.direita)

    def preorder(self):
        return self._preorder(self.raiz)

    def _preorder(self, no):
        if no is None:
            return []
        return [no.valor] + self._preorder(no.esquerda) + self._preorder(no.direita)

    def postorder(self):
        return self._postorder(self.raiz)

    def _postorder(self, no):
        if no is None:
            return []
        return self._postorder(no.esquerda) + self._postorder(no.direita) + [no.valor]