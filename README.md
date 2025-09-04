# Atividades de Estruturas de Dados em Python

Este repositório contém três atividades práticas sobre árvores binárias, desenvolvidas em Python, com visualização utilizando a biblioteca Graphviz.

---

## Atividade 1: Árvore de Expressão Matemática

- **Objetivo:** Converter uma expressão aritmética linear em uma árvore binária, onde operadores são nós internos e operandos são folhas.
- **Funcionalidades:**
  - Construção da árvore a partir de uma expressão fixa:  
    `( ( ( 7 + 3 ) * ( 5 - 2 ) ) / ( 10 * 20 ) )`
  - Geração de uma expressão aleatória e construção da árvore correspondente.
  - Visualização das árvores com Graphviz.

---

## Atividade 2: Árvore Binária de Busca (BST)

- **Objetivo:** Implementar as operações fundamentais de uma BST: inserção, busca, remoção, cálculo de altura e profundidade.
- **Funcionalidades:**
  - Métodos: `inserir`, `buscar`, `remover`, `altura`, `profundidade`.
  - Demonstração com valores fixos: `[55, 30, 80, 20, 45, 70, 90]`.
  - Demonstração com valores aleatórios.
  - Visualização das árvores antes e depois das operações.

---

## Atividade 3: Travessias em Profundidade (DFS)

- **Objetivo:** Implementar e demonstrar os três principais algoritmos de travessia em profundidade em uma árvore binária.
- **Funcionalidades:**
  - Métodos: `inorder` (Esquerda-Raiz-Direita), `preorder` (Raiz-Esquerda-Direita), `postorder` (Esquerda-Direita-Raiz).
  - Demonstração com valores fixos e aleatórios.
  - Visualização das árvores.

---

## Requisitos

- Python 3.8+
- [graphviz](https://graphviz.gitlab.io/) instalado no sistema
- Biblioteca Python:  
  ```bash
  pip install graphviz
  ```

---

## Execução

Execute cada arquivo Python para visualizar as árvores e os resultados das operações:

```bash
python atividade_1.py
python atividade_2.py
python atividade_3.py
```

As imagens das árvores serão geradas automaticamente e abertas pelo sistema.

---

## Licença

Este projeto é apenas