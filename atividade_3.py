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
    
    # Visualizar a árvore com graphviz
    
    def desenhar(self, nome_arquivo="arvore"):
        grafo = Digraph(format="png")
        grafo.attr("node", shape="circle")

        def adicionar_nos(no):
            if no is None:
                return
            grafo.node(str(id(no)), str(no.valor))
            if no.esquerda:
                grafo.edge(str(id(no)), str(id(no.esquerda)))
                adicionar_nos(no.esquerda)
            if no.direita:
                grafo.edge(str(id(no)), str(id(no.direita)))
                adicionar_nos(no.direita)

        adicionar_nos(self.raiz)
        grafo.render(nome_arquivo, view=True)


# ------------------------------
# Demonstração do funcionamento
# ------------------------------

if __name__ == "__main__":

    # Árvore com valores fixos

    print("==== Árvore com valores fixos ====")
    valores_fixos = [55, 30, 80, 20, 45, 70, 90]
    arvore_fixa = ArvoreBinariaBusca()
    for v in valores_fixos:
        arvore_fixa.inserir(v)

    arvore_fixa.desenhar("arvore_fixa_dfs")

    print("In-Order (Esquerda, Raiz, Direita):", arvore_fixa.inorder())
    print("Pre-Order (Raiz, Esquerda, Direita):", arvore_fixa.preorder())
    print("Post-Order (Esquerda, Direita, Raiz):", arvore_fixa.postorder())

    # Árvore com valores aleatórios

    print("\n==== Árvore com valores aleatórios ====")
    numeros_aleatorios = random.sample(range(1, 100), 10)
    print("Números aleatórios:", numeros_aleatorios)

    arvore_aleatoria = ArvoreBinariaBusca()
    for n in numeros_aleatorios:
        arvore_aleatoria.inserir(n)

    arvore_aleatoria.desenhar("arvore_aleatoria_dfs")

    print("In-Order (Esquerda, Raiz, Direita):", arvore_aleatoria.inorder())
    print("Pre-Order (Raiz, Esquerda, Direita):", arvore_aleatoria.preorder())
    print("Post-Order (Esquerda, Direita, Raiz):", arvore_aleatoria.postorder())