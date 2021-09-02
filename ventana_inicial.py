import constantes as ctes
import gamelib
import mensajes
from funciones_auxiliares import esta_dentro_circuferencia

'''Defino constantes sobre las dimensiones de los botones'''
#FORMATO
#DIMENSION_X = Range(COORDENAD_X_INICIO, COORDENADA_X_FINAL)
#DIMENSION_Y = Range(COORDENAD_Y_INICIO, COORDENADA_Y_FINAL)
#DIMENSION_OVALO = (COORDENADA_CENTRO_X, COORDENADA_CENTRO_Y, RADIO)

DIMENSIONES_TITULO_POKEDEX = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.2, int(ctes.ALTO_VENTANA*0.1))
DIMENSIONES_INFO_POKEDEX = (ctes.ANCHO_VENTANA*0.71875, ctes.ALTO_VENTANA*0.148, int(ctes.ALTO_VENTANA*0.04))
DIMENSIONES_PALABRA_POKEMONES = (ctes.ANCHO_VENTANA*0.375, ctes.ALTO_VENTANA*0.5, int(ctes.ALTO_VENTANA*0.06))
DIMENSIONES_INFORMACION_POKEMONES = (ctes.ANCHO_VENTANA*0.5325, ctes.ALTO_VENTANA*0.464, int(ctes.ALTO_VENTANA*0.02)) 
DIMENSIONES_PALABRA_EQUIPOS = (ctes.ANCHO_VENTANA*0.35, ctes.ALTO_VENTANA*0.7, int(ctes.ALTO_VENTANA*0.06))
DIMENSIONES_INFORMACION_EQUIPOS = (ctes.ANCHO_VENTANA*0.475, ctes.ALTO_VENTANA*0.654, int(ctes.ALTO_VENTANA*0.02))
DIMENSIONES_INTRUCCIONES_TECLADO = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.94, int(ctes.ALTO_VENTANA*0.02))
OVALO_A_VENTANA_PK_EQ_X = (ctes.ANCHO_VENTANA*0.75, ctes.ANCHO_VENTANA*0.8)
OVALO_A_VENTANA_POKEMONS_Y = (ctes.ALTO_VENTANA*0.46, ctes.ALTO_VENTANA*0.54)
OVALO_A_VENTANA_EQUIPOS_Y = (ctes.ALTO_VENTANA*0.66, ctes.ALTO_VENTANA*0.74)

#FORMATO
#DIMENSION_X = Range(COORDENAD_X_INICIO, COORDENADA_X_FINAL)
#DIMENSION_Y = Range(COORDENAD_Y_INICIO, COORDENADA_Y_FINAL)
#DIMENSION_OVALO = (COORDENADA_CENTRO_X, COORDENADA_CENTRO_Y, RADIO)

DIMENSIONES_INFORMACION_POKEDEX_X = (ctes.ANCHO_VENTANA*0.70375, ctes.ANCHO_VENTANA*0.7325)
DIMENSIONES_INFORMACION_POKEDEX_Y = (ctes.ALTO_VENTANA*0.124, ctes.ALTO_VENTANA*0.178)
DIMENSIONES_INFORMACION_POKEMONS_X = (ctes.ANCHO_VENTANA*0.52125, ctes.ANCHO_VENTANA*0.545) 
DIMENSIONES_INFORMACION_POKEMONS_Y = (ctes.ALTO_VENTANA*0.448, ctes.ALTO_VENTANA*0.474)
DIMENSIONES_INFORMACION_EQUIPOS_X = (ctes.ANCHO_VENTANA*0.46375, ctes.ANCHO_VENTANA*0.48625) 
DIMENSIONES_INFORMACION_EQUIPOS_Y = (ctes.ALTO_VENTANA*0.638, ctes.ALTO_VENTANA*0.664) 
DIMENSION_OVALO_VENTANA_POKEMONS = (ctes.ANCHO_VENTANA*0.775, ctes.ALTO_VENTANA*0.5, ctes.ALTO_VENTANA*0.04)
DIMENSION_OVALO_VENTANA_EQUIPOS = (ctes.ANCHO_VENTANA*0.775, ctes.ALTO_VENTANA*0.7, ctes.ALTO_VENTANA*0.04)

def mostrar_ventana_inicial(colores_actuales):
    '''Dibuja la ventana inicial de la Pokedex con los colores actuales'''
    x, y, tamaño = DIMENSIONES_TITULO_POKEDEX
    gamelib.draw_text(ctes.TEXTO_POKEDEX, x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSIONES_INFO_POKEDEX
    gamelib.draw_text(ctes.SIMBOLO_INFORMACION, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x, y, tamaño = DIMENSIONES_PALABRA_POKEMONES
    gamelib.draw_text(ctes.TEXTO_POKEMONES, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSIONES_INFORMACION_POKEMONES
    gamelib.draw_text(ctes.SIMBOLO_INFORMACION, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x, y, tamaño = DIMENSIONES_PALABRA_EQUIPOS
    gamelib.draw_text(ctes.TEXTO_EQUIPOS, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSIONES_INFORMACION_EQUIPOS
    gamelib.draw_text(ctes.SIMBOLO_INFORMACION, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x, y, tamaño = DIMENSIONES_INTRUCCIONES_TECLADO
    gamelib.draw_text(ctes.TEXTO_INFORMACION_FUNCIONES_TECLAS, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x1, x2 = OVALO_A_VENTANA_PK_EQ_X
    y1, y2 = OVALO_A_VENTANA_POKEMONS_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COMBINACION_DE_COLORES[colores_actuales][2], fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
    x1, x2 = OVALO_A_VENTANA_PK_EQ_X
    y1, y2 = OVALO_A_VENTANA_EQUIPOS_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COMBINACION_DE_COLORES[colores_actuales][2], fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)

def evaluar_en_ventana_inicial(ev):

    '''Evalua la accion del usuario en la ventana inicial y retorna la ventana actual'''

    if ev.type == gamelib.EventType.ButtonPress:
        #El usuario clickeo

        x, y = ev.x, ev.y
        xc, yc, radio = DIMENSION_OVALO_VENTANA_POKEMONS
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            return ctes.VENTANA_VISTA_POKEMONS

        xc, yc, radio = DIMENSION_OVALO_VENTANA_EQUIPOS
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            return ctes.VENTANA_VISTA_EQUIPOS

        xi, xf = DIMENSIONES_INFORMACION_POKEDEX_X
        yi, yf = DIMENSIONES_INFORMACION_POKEDEX_Y
        if xi < x < xf  and yi < y < yf :
            gamelib.say(mensajes.MENSAJE_INFO_POKEDEX)
            return ctes.VENTANA_INICIAL

        xi, xf = DIMENSIONES_INFORMACION_POKEMONS_X
        yi, yf = DIMENSIONES_INFORMACION_POKEMONS_Y
        if xi < x < xf  and yi < y < yf :
            gamelib.say(mensajes.MENSAJE_INFO_POKEMONS)
            return ctes.VENTANA_INICIAL

        xi, xf = DIMENSIONES_INFORMACION_EQUIPOS_X
        yi, yf = DIMENSIONES_INFORMACION_EQUIPOS_Y
        if xi < x < xf  and yi < y < yf :
            gamelib.say(mensajes.MENSAJE_INFO_EQUIPOS)
            return ctes.VENTANA_INICIAL

    if ev.type == gamelib.EventType.KeyPress:
        #El usuario presiono una tecla

        if ev.key == ctes.TECLA_VENTANA_POKEMONS:
            return ctes.VENTANA_VISTA_POKEMONS

        if ev.key == ctes.TECLA_VENTANA_EQUIPOS:
            return ctes.VENTANA_VISTA_EQUIPOS

        if ev.key == ctes.TECLA_VENTANA_ANTERIOR:
            return ctes.SALIR

        if ev.key == ctes.TECLA_VENTANA_COLORES:
            return ctes.VENTANA_COLORES

    return ctes.VENTANA_INICIAL