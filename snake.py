import pygame
import random

pygame.init()

largura, altura = 640, 480
tamanho_celula = 20
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Snake')

cobra = [(largura // 2, altura // 2)]
comida = (random.randint(0, largura // tamanho_celula - 1) * tamanho_celula,
          random.randint(0, altura // tamanho_celula - 1) * tamanho_celula)

direcao = (0, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != (0, 1):
                direcao = (0, -1)
            elif evento.key == pygame.K_DOWN and direcao != (0, -1):
                direcao = (0, 1)
            elif evento.key == pygame.K_LEFT and direcao != (1, 0):
                direcao = (-1, 0)
            elif evento.key == pygame.K_RIGHT and direcao != (-1, 0):
                direcao = (1, 0)

    cobra.insert(0, (cobra[0][0] + direcao[0] * tamanho_celula, cobra[0][1] + direcao[1] * tamanho_celula))

    if cobra[0] == comida:
        comida = (random.randint(0, largura // tamanho_celula - 1) * tamanho_celula,
                  random.randint(0, altura // tamanho_celula - 1) * tamanho_celula)
    else:
        cobra.pop()

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, cor_comida, (comida[0], comida[1], tamanho_celula, tamanho_celula))
    for segmento in cobra:
        pygame.draw.rect(tela, cor_cobra, (segmento[0], segmento[1], tamanho_celula, tamanho_celula))

    pygame.display.update()
