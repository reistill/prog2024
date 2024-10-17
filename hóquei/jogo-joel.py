import pygame

# github de humrochagf no repositório 05-moviment-and-speed, feito por Humberto Rocha
 

# Constantes para cores
PRETO = pygame.Color(0, 0, 0)
BRANCO = pygame.Color(255, 255, 255)

# Inicializa o Pygame
pygame.init()

# Configura a tela
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Colisão')

# Cria o Retângulo do quadrado
quadrado = pygame.Rect(300, 230, 20, 20)

# Cria os Retângulos das barras
barra_esquerda = pygame.Rect(20, 210, 20, 60)
barra_direita = pygame.Rect(600, 210, 20, 60)
barras = [barra_esquerda, barra_direita]

# Velocidade do quadrado
velocidade_x = 0.5

# Velocidade de movimento das barras
velocidade_barras = 5

# Relógio do jogo para controlar a taxa de quadros
relógio = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    # Limita a taxa de quadros para 75 FPS
    dt = relógio.tick(75)

    # Manipulação de eventos, no caso o único evento que é o de saída 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Move o quadrado
    quadrado.move_ip(velocidade_x * dt, 0)

    # Verifica colisão com as barras
    if quadrado.collidelist(barras) >= 0:
        velocidade_x = -velocidade_x

    # Movimentação das barras
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and barra_esquerda.top > 0:  # Barra esquerda para cima
        barra_esquerda.move_ip(0, -velocidade_barras)
    if teclas[pygame.K_s] and barra_esquerda.bottom < 480:  # Barra esquerda para baixo
        barra_esquerda.move_ip(0, velocidade_barras)
    if teclas[pygame.K_UP] and barra_direita.top > 0:  # Barra direita para cima
        barra_direita.move_ip(0, -velocidade_barras)
    if teclas[pygame.K_DOWN] and barra_direita.bottom < 480:  # Barra direita para baixo
        barra_direita.move_ip(0, velocidade_barras)

    # Limpa a tela
    tela.fill(PRETO)

    # Desenha o quadrado
    pygame.draw.rect(tela, BRANCO, quadrado)

    # Desenha as barras
    for barra in barras:
        pygame.draw.rect(tela, BRANCO, barra)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
