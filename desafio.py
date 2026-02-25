import pygame
import sys
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Janela')

AZUL = (0,0,255)
PRETO = (0,0,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
BRANCO = (255,255,255)

TEXTO_1 = "PY"
TEXTO_2 = "DVD"

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

def gerar_cor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def gerar_velocidade(x_range, y_range):
    vx = random.randint(*x_range)
    vy = random.randint(*y_range)
    while vx == 0 and vy == 0:
        vx = random.randint(*x_range)
        vy = random.randint(*y_range)
    return vx, vy

def criar_texto(valor, centro, cor_inicial=BRANCO):
    superficie = fonte.render(valor, True, cor_inicial)
    rect = superficie.get_rect(center=centro)
    velocidade = list(gerar_velocidade((-1, 1), (-1, 1)))
    return {
        "valor": valor,
        "cor": cor_inicial,
        "surface": superficie,
        "rect": rect,
        "vel": velocidade,
    }

def atualizar_surface(item):
    item["surface"] = fonte.render(item["valor"], True, item["cor"])

def aplicar_colisao_paredes(item):
    rect = item["rect"]
    bateu_direita = rect.right >= largura
    bateu_esquerda = rect.left <= 0
    bateu_baixo = rect.bottom >= altura
    bateu_cima = rect.top <= 0

    if bateu_direita or bateu_esquerda or bateu_baixo or bateu_cima:
        if bateu_direita:
            x_range = (-1, 0)
        elif bateu_esquerda:
            x_range = (0, 1)
        else:
            x_range = (-1, 1)

        if bateu_baixo:
            y_range = (-1, 0)
        elif bateu_cima:
            y_range = (0, 1)
        else:
            y_range = (-1, 1)

        item["vel"] = list(gerar_velocidade(x_range, y_range))
        item["cor"] = gerar_cor()
        atualizar_surface(item)

def aplicar_colisao_textos(item_a, item_b):
    if item_a["rect"].colliderect(item_b["rect"]):
        item_a["vel"] = list(gerar_velocidade((-1, 1), (-1, 1)))
        item_b["vel"] = list(gerar_velocidade((-1, 1), (-1, 1)))
        item_a["cor"] = gerar_cor()
        item_b["cor"] = gerar_cor()
        atualizar_surface(item_a)
        atualizar_surface(item_b)

texto_1 = criar_texto(TEXTO_1, (largura / 3, altura / 2))
texto_2 = criar_texto(TEXTO_2, (2 * largura / 3, altura / 2))

clock = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(PRETO)

    for item in (texto_1, texto_2):
        item["rect"].x += item["vel"][0]
        item["rect"].y += item["vel"][1]
        aplicar_colisao_paredes(item)
        tela.blit(item["surface"], item["rect"])

    aplicar_colisao_textos(texto_1, texto_2)

    clock.tick(120)
    pygame.display.flip()
pygame.quit()
sys.exit()