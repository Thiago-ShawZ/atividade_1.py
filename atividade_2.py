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

    arvore_fixa.desenhar("arvore_fixa")

    # Busca

    print("Busca pelo valor 45:", arvore_fixa.buscar(45) is not None)

    # Remoção

    print("Removendo o valor 30...")
    arvore_fixa.remover(30)
    arvore_fixa.desenhar("arvore_fixa_removida")

    # Nova inserção

    print("Inserindo o valor 60...")
    arvore_fixa.inserir(60)
    arvore_fixa.desenhar("arvore_fixa_inserida")

    # Altura e profundidade

    print("Altura da árvore:", arvore_fixa.altura())
    print("Profundidade do nó 45:", arvore_fixa.profundidade(45))

    # Árvore com valores aleatórios

    print("\n==== Árvore com valores aleatórios ====")
    numeros_aleatorios = random.sample(range(1, 200), 15)
    print("Números aleatórios:", numeros_aleatorios)

    arvore_aleatoria = ArvoreBinariaBusca()
    for n in numeros_aleatorios:
        arvore_aleatoria.inserir(n)

    arvore_aleatoria.desenhar("arvore_aleatoria")
    print("Altura da árvore aleatória:", arvore_aleatoria.altura())