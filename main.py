import pygame
import sys
from regras import proxima_geracao


# parametros inicias
pygame.init()
# JANELA
LARGURA, ALTURA = 800, 600 
TAMANHO_CELULA = 20  #pixeis de um quadrado
janela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

running = True 
simulacao = False  #Começa pausado para o user desenhar o pattern inicial

# Preciso de ter uma matriz que vai simular as celulas
# Se tou a usar uma janela 800 x 600, e cada celula ocupa 20 pixeis
# Preciso de 800/20 = 40 colunas ; 600/20 = 30 linhas.
matriz = [[0 for _ in range(40)] for _ in range(30)]

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                simulacao = not simulacao  # Espaço para pausar / play
            
            if evento.key == pygame.K_r: # R para resetar o ecra
                simulacao = False
                matriz = [[0 for _ in range(40)] for _ in range(30)]
        
        if evento.type == pygame.MOUSEBUTTONDOWN:  # Se carregar no rato (desenhar o pattern)
            if evento.button == 1: # Mouse 1
                pos_rato = pygame.mouse.get_pos()
                # a posicao do rato é em pixeis 
                # Por exemplo : X = 245, Y = 122.
                # Para saber a linha e coluna a que se refere na matriz, posso usar divisao inteira
                # Ou seja, coluna = 245 // 20 = 12 <- Coluna
                # linha = 122 // 20 = 6 <- linha

                coluna = pos_rato[0] // TAMANHO_CELULA
                linha = pos_rato[1] // TAMANHO_CELULA


                # Inverte o estado da celula: Se estava morta (0) passa a 1, se estava 1 passa a 0
                if matriz[linha][coluna] == 0:
                    matriz[linha][coluna] = 1
                else:
                    matriz[linha][coluna] = 0

    
    if simulacao:
        ecra = pygame.display.set_caption("O Jogo da Vida - A CORRER")
        matriz = proxima_geracao(matriz)
    else:
        ecra = pygame.display.set_caption("O Jogo da Vida - PAUSADO")

    janela.fill((0,0,0))

    # DESENHAR A GRELHA
    # Linhas verticais (colunas)
    # (0,800,20) -> 0 até 800, a andar de 20 em 20
    for x in range(0, 800, 20):
        # (x,0) -> começa com Y=0 (topo) . acaba em (x,600) -> Y= 600 ->fundo
        #(superficie,cor,ponto_inicial,ponto_final)
        pygame.draw.line(janela, (128,128,128), (x,0), (x,600))

    # Linhas Horizontais
    for y in range(0,600,20):
        pygame.draw.line(janela, (128,128,128), (0,y), (800,y))


    # PINTAR AS CELULAS ATIVAS
    for linha in range(30):
        for coluna in range(40):
            if matriz[linha][coluna] == 1:
                # Fazemos a operacao inversa para voltar a ter coordenadas
                x = coluna * TAMANHO_CELULA
                y = linha * TAMANHO_CELULA

                #(janela,cor,(x_pixel,y_pixel,largura,altura))
                # x+1 e TAMANHO - 1 para ficar dentro dos limites (nao tapar as bordas)
                pygame.draw.rect(janela,(255,255,255), (x+1, y+1, TAMANHO_CELULA - 1, TAMANHO_CELULA - 1))

    pygame.display.flip()
    relogio.tick(10)

pygame.quit()
sys.exit()
