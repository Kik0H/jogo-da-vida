import copy

def proxima_geracao(matriz_atual):
    # Ler da matriz_atual, atualizar na matriz_nova. 
    # Se nao havia erros nas leituras/escritas
    matriz_nova = copy.deepcopy(matriz_atual)

    for linha in range(30):
        for coluna in range(40):
            # Contar os vizinhos vivos a volta
            vizinhos_vivos = 0

            # Cada celula tem 8 vizinhos, tenho de verificar todos
            # Percorrer o "quadrado" a volta da celula. -1 (cima), 0 (mesma) e 1 (baixo)
            for i in range(-1,2):
                for j in range(-1,2):

                    if i == 0 and j == 0:
                        continue # Ignorar a propria celula

                    linha_vizinho = linha + i 
                    coluna_vizinho = coluna + j 

                    # Verificar se o vizinho esta dentro dos limites do ecra
                    if 0 <= linha_vizinho < 30 and 0 <= coluna_vizinho < 40:
                        if matriz_atual[linha_vizinho][coluna_vizinho] == 1:
                            vizinhos_vivos += 1

            # VERIFICAR AS REGRAS
            celula_viva = (matriz_atual[linha][coluna] == 1)

            if celula_viva:
                # Regra 1 e 3: menos 2 vizinhos vivos, mais 3 vizinhos vivos
                if vizinhos_vivos < 2 or vizinhos_vivos > 3 :
                    matriz_nova[linha][coluna] = 0 # morre
            
            else:
                # Regra 4: Se tiver 3 vizinhos vivos, nasce
                if vizinhos_vivos == 3:
                    matriz_nova[linha][coluna] = 1
    
    return matriz_nova