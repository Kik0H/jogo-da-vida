# Jogo da Vida - Conway's Game of Life

Não tinha nada melhor que fazer a uma sexta feira, por isso saiu isto.

Implementação do autómato celular de John Conway, feita em Python com a biblioteca `pygame`.

## Como funciona

A grelha é representada por uma matriz de 30 linhas x 40 colunas (células de 20x20 pixeis numa janela de 800x600).

Na matriz:
- **0** = célula morta
- **1** = célula viva

O utilizador começa por desenhar um pattern inicial, e começa a simulação. Pode interagir com a simulação a meio (ativar/desativar células) para poder modificar a maneira como a simulação se comporta.


A cada tick, aplicam-se as regras de Conway:

1. Uma célula viva com menos de 2 vizinhos vivos morre (isolamento).
2. Uma célula viva com 2 ou 3 vizinhos vivos mantém-se viva.
3. Uma célula viva com mais de 3 vizinhos vivos morre (sobrepopulação).
4. Uma célula morta com exatamente 3 vizinhos vivos nasce.

## Como executar

```bash
pip install pygame
python main.py
```

## Controlos

| Tecla         | Efeito                                  |
|---------------------|------------------------------------------|
| Clique esquerdo      | Liga/desliga uma célula (desenhar pattern) |
| Espaço               | Inicia/pausa a simulação                  |
| R                    | Reinicia a grelha (limpa tudo)            |


## Estrutura do projeto

- `main.py` - ciclo principal, janela, eventos e desenho na grelha.
- `regras.py` - lógica das regras do jogo (`proxima_geracao`).

## O que ainda posso melhorar
Isto ainda dá para melhorar, fica para outra sexta que não tenha nada que fazer
- Tornar o tamanho da grelha configurável.
- Permitir que a janela seja expandível (sem bordas, vai expandindo quando as células chegam à borda).
- Consequentemente, adicionar um slider para dar zoomOut/zoomIn
- Adicionar um slider para controlar a velocidade da simulação.


