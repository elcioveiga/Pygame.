import pygame
import os

#Inicializando o Pygame
pygame.init()

#Definindo o tamanho da janela padrão
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Janela com Imagem")

#Definindo a cor de fundo
BG_COLOR = (30, 30, 40)

#Caminho da imagem
image_file = "player.png"
if os.path.exists(image_file):
    img = pygame.image.load(image_file).convert_alpha()
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
else:
    print("Imagem não encontrada!")

#Variáveis de controle de tamanho
is_maximized = False

#Função para centralizar a imagem
def center_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center = (WIDTH // 2, HEIGHT // 2)

#Função para alternar para o modo maximizado
def toggle_maximized():
    global is_maximized, screen, WIDTH, HEIGHT, img_rect
    if is_maximized:
       # Voltar ao tamanho normal
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        center_image()
        is_maximized = True

#Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.key == pygame.K_F11:
            toggle_maximized()

    #Atualize o tamanho da janela em tempo real
    WIDTH, HEIGHT = screen.get_size()
    center_image()

    #Preencher o fundo
    screen.fill(BG_COLOR)

    #Desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)

    #Atualizar a tela
    pygame.display.flip()

#Finalizar o Pygame
pygame.quit()