import constantes as ctes
import gamelib
from funciones_auxiliares import esta_dentro_circuferencia

'''Defino constantes para las dimensiones de lo que vamos a dibujar'''
#Formato 
# TEXTO = (POSICION_X, POSICION_Y, TAMAÑO_LETRA)
# RECTANGULO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# RECTANGULO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# OVALO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# OVALO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# IMAGEN = (POSICION_ESQUINA_X, POSICION_ESQUNA_Y)

DIMENSIONES_INTRUCCIONES_TECLADO = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.94, int(ctes.ALTO_VENTANA*0.02))
CARTEL_COLORES = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.125, int(ctes.ALTO_VENTANA*0.1))
DIMENSIONES_TEXTO_COLORES = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.25, int(ctes.ALTO_VENTANA*0.03))
RECTANGULO_OPCIONES_COLORES_X = (ctes.ANCHO_VENTANA*0.0875, ctes.ANCHO_VENTANA*0.2875)
RECTANGULO_OPCIONES_COLORES_Y = (ctes.ALTO_VENTANA*0.32, ctes.ALTO_VENTANA*0.38)
OPCIONES_COLORES = (ctes.ANCHO_VENTANA*0.1875, ctes.ALTO_VENTANA*0.35, int(ctes.ALTO_VENTANA*0.05))
CUADRADOS_COLORES_X = (ctes.ANCHO_VENTANA*0.4375, ctes.ANCHO_VENTANA*0.48375)
CUADRADOS_COLORES_Y = (ctes.ALTO_VENTANA*0.32, ctes.ALTO_VENTANA*0.38)
OVALO_VOLVER_VENTANA_X = (ctes.ANCHO_VENTANA*0.015, ctes.ANCHO_VENTANA*0.04)
OVALO_VOLVER_VENTANA_Y = (ctes.ALTO_VENTANA*0.024, ctes.ALTO_VENTANA*0.064)
DIMENSION_OVALO_ANTERIOR_VENTANA = (ctes.ANCHO_VENTANA*0.0275, ctes.ALTO_VENTANA*0.044, ctes.ALTO_VENTANA*0.02)

#FORMATO
#DIMENSION_X = (COORDENAD_X_INICIO, COORDENADA_X_FINAL)
#DIMENSION_Y = (COORDENAD_Y_INICIO, COORDENADA_Y_FINAL)
#DIMENSION_OVALO = (COORDENADA_CENTRO_X, COORDENADA_CENTRO_Y, RADIO)

DIMENSION_OPCIONES_COLORES_X = (ctes.ANCHO_VENTANA*0.0875, ctes.ANCHO_VENTANA*0.2875)
DIMENSION_OPCIONES_COLORES_Y = (ctes.ALTO_VENTANA*0.32, ctes.ALTO_VENTANA*0.38)

def mostrar_ventana_colores(colores_actuales):
    '''Dibuja la ventana de colores con las distintas opciones'''
    x, y, tamaño = CARTEL_COLORES
    gamelib.draw_text(ctes.TEXTO_COLORES, x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSIONES_TEXTO_COLORES
    gamelib.draw_text(ctes.TEXTO_ELIGE_COLORES, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    for yc in range(len(ctes.COMBINACION_DE_COLORES)):
        x1, x2 = RECTANGULO_OPCIONES_COLORES_X
        y1, y2 = RECTANGULO_OPCIONES_COLORES_Y
        gamelib.draw_rectangle(x1, y1 + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*yc, x2, y2 + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*yc, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
        x, y, tamaño = OPCIONES_COLORES
        gamelib.draw_text(f'{ctes.TEXTO_OPCION} {yc + 1}:', x, y + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*yc, font = ctes.FUENTE, size = tamaño, italic = True, activefill = ctes.COLOR_GRIS, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        for xc in range(3):
            x1, x2 = CUADRADOS_COLORES_X
            y1, y2 = CUADRADOS_COLORES_Y
            gamelib.draw_rectangle(x1 + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*xc, y1 + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*yc, x2 + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*xc, y2 + ctes.DISTANCIA_ENTRE_OPCIONES_COLOR*yc, outline = ctes.COMBINACION_DE_COLORES[colores_actuales][2], fill = ctes.COMBINACION_DE_COLORES[yc][xc])
    x1, x2 = OVALO_VOLVER_VENTANA_X
    y1, y2 = OVALO_VOLVER_VENTANA_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COLOR_ROJO, activefill = ctes.COLOR_ROSA)
    x, y, tamaño = DIMENSIONES_INTRUCCIONES_TECLADO
    gamelib.draw_text(ctes.TEXTO_OPCIONES_EN_VENTANA_COLORES, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COLOR_NEGRO)

def evaluar_en_ventana_colores(ev, colores):
    '''Evalua la accion del usuario en la ventana colores y retorne la ventana actual y retorna el indice
    de los colores actuales'''
    ventana_actual = ctes.VENTANA_COLORES

    if ev.type == gamelib.EventType.KeyPress:

        if ev.key in ctes.TECLAS_NUMEROS_OPCIONES_COLORES:
            numero_elegido = int(ev.key) - 1
            colores = numero_elegido
            ventana_actual = ctes.VENTANA_INICIAL

        if ev.key == ctes.TECLA_VENTANA_ANTERIOR:
            ventana_actual = ctes.VENTANA_INICIAL


    if ev.type == gamelib.EventType.ButtonPress:
        x, y = ev.x, ev.y
        n = ctes.ALTO_VENTANA*0.09

        for dy in range(6):
            xi, xf = DIMENSION_OPCIONES_COLORES_X
            yi, yf = DIMENSION_OPCIONES_COLORES_Y
            if  xi < x < xf  and  (yi + n*dy) < y < (yf + n*dy):
                colores = dy
                ventana_actual = ctes.VENTANA_INICIAL
                
        xc, yc, radio = DIMENSION_OVALO_ANTERIOR_VENTANA
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            ventana_actual = ctes.VENTANA_INICIAL
    return ventana_actual, colores