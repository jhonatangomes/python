import pygame
import random
#tela
LARGURA, ALTURA = 400, 600



#CORES
AZUL = (135, 206, 250)
VERDE = (0, 200, 0)
AMARELO = (255, 255, 0)
PRETO = (0, 0 , 0,)

#JOGO
GRAVIDADE = 0.5
TAMANHO_PASSARO = 20
ESPACO_CANOS = 200
LARGURA_CANO = 60
VELOCIDADE_CANO = 5
ALTURA_PULO = -10

#INICIALIZAÇÃO
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")
fonte = pygame.font.SysFont("Arial", 36)
relogio = pygame.time.Clock()

passaro_x = 50
passaro_y = ALTURA // 2
velocidade = 0

cano_x = LARGURA
cano_altura = random.randint(150, 450)

pontos = 0
ja_contou_pontos = False

rodando = True

while rodando:
    relogio.tick(60)
    tela.fill(AZUL)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando == False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            velocidade = ALTURA_PULO



    velocidade += GRAVIDADE
    passaro_y += velocidade

    pygame.draw.circle(tela, AMARELO, (passaro_x, int(passaro_y)),TAMANHO_PASSARO)


    cano_x -= VELOCIDADE_CANO

    if cano_x + LARGURA_CANO < 0:
        cano_x = LARGURA
        ja_contou_pontos = False
        cano_altura = random.randint(150, 450)

    pygame.draw.rect(tela, VERDE, (cano_x, 0, LARGURA_CANO, cano_altura))
    pygame.draw.rect(tela, VERDE, (cano_x, cano_altura + ESPACO_CANOS, LARGURA_CANO, ALTURA))


    colidiu_horizontal = (
        passaro_x + TAMANHO_PASSARO > cano_x and
        passaro_x - TAMANHO_PASSARO < cano_x + LARGURA_CANO
    )

    colidiu_vertical = (
        passaro_y - TAMANHO_PASSARO < cano_altura or
        passaro_y + TAMANHO_PASSARO > cano_altura + ESPACO_CANOS
    )

    colideu_cano = colidiu_horizontal and colidiu_vertical
    fora_da_tela = passaro_y > ALTURA or passaro_y < 0


    if colideu_cano or fora_da_tela:
        rodando = False

    if cano_x + LARGURA_CANO < passaro_x and not ja_contou_pontos:
        pontos += 1
        ja_contou_pontos = True

    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()