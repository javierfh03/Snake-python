from ui.utilidades.colores import VERDE

from pygame.font import Font
from pygame.surface import Surface


def dibujar_texto(texto, fuente: Font, color, ventana, x, y) -> Surface:
    texto_render = fuente.render(texto, True, color)

    ventana.blit(texto_render, (x, y))

    return texto_render


def obtener_centro_texto(fuente_texto, texto: str, anchura: int) -> int:
    texto_dimensiones = fuente_texto.render(texto, True, VERDE).get_size()
    return (anchura - texto_dimensiones[0]) / 2
