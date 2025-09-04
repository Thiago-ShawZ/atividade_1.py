import random
from graphviz import Digraph

# Classe para representar um nó da árvore
class No:
    def __init__(self, valor, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita


# Função recursiva para desenhar a árvore com graphviz
def desenhar_arvore(no, grafo=None, pai=None):
    if grafo is None:
        grafo = Digraph(format="png")
        grafo.attr("node", shape="circle")

    # Cria o nó no grafo
    grafo.node(str(id(no)), str(no.valor))

    if pai:
        grafo.edge(str(id(pai)), str(id(no)))

    # Chama recursivamente para os filhos
    if no.esquerda:
        desenhar_arvore(no.esquerda, grafo, no)
    if no.direita:
        desenhar_arvore(no.direita, grafo, no)

    return grafo


# Função para converter uma expressão em árvore
def expressao_para_arvore(tokens):
    pilha = []
    operadores = []

    def aplicar_operador():
        operador = operadores.pop()
        direito = pilha.pop()
        esquerdo = pilha.pop()
        pilha.append(No(operador, esquerdo, direito))

    for token in tokens:
        if token.isdigit():
            pilha.append(No(token))
        elif token in "+-*/":
            while operadores and operadores[-1] in "*/" and token in "+-":
                aplicar_operador()
            operadores.append(token)
        elif token == "(":
            operadores.append(token)
        elif token == ")":
            while operadores and operadores[-1] != "(":
                aplicar_operador()
            operadores.pop()

    while operadores:
        aplicar_operador()

    return pilha[0]


# Função para gerar uma expressão aleatória
def gerar_expressao_aleatoria():
    numeros = [str(random.randint(1, 20)) for _ in range(3)]
    op = random.sample(["+", "-", "*", "/"], 2)

    # Exemplo: (a op1 b) op2 c
    expressao = f"( {numeros[0]} {op[0]} {numeros[1]} ) {op[1]} {numeros[2]}"
    return expressao


if __name__ == "__main__":
    # Expressão fixa
    expressao_fixa = "( ( ( 7 + 3 ) * ( 5 - 2 ) ) / ( 10 * 20 ) )"
    tokens_fixos = expressao_fixa.replace("(", " ( ").replace(")", " ) ").split()
    arvore_fixa = expressao_para_arvore(tokens_fixos)

    grafo1 = desenhar_arvore(arvore_fixa)
    grafo1.render("arvore_fixa", view=True)  # Salva e abre a imagem

    # Expressão aleatória
    expressao_aleatoria = gerar_expressao_aleatoria()
    print("Expressão aleatória:", expressao_aleatoria)
    tokens_aleatorios = expressao_aleatoria.replace("(", " ( ").replace(")", " ) ").split()
    arvore_aleatoria = expressao_para_arvore(tokens_aleatorios)

    grafo2 = desenhar_arvore(arvore_aleatoria)
    grafo2.render("arvore_aleatoria", view=True)
