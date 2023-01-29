import pygame
from pygame.font import Font
from pygame.surface import Surface

ANCHURA = 450
ALTURA = 500
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)


def dibujar_texto(texto, fuente: Font, color, ventana, x, y) -> Surface:
    texto_render = fuente.render(texto, True, color)

    ventana.blit(texto_render, (x, y))

    return texto_render


def obtener_centro_texto(fuente_texto, texto: str) -> int:
    texto_dimensiones = fuente_texto.render(texto, True, VERDE).get_size()
    return (ANCHURA - texto_dimensiones[0]) / 2
