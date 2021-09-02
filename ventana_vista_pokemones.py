import constantes as ctes
import mensajes
import gamelib
from funciones_auxiliares import siguiente_indice, anterior_indice, buscar_pokemon, esta_dentro_circuferencia
from random import choice
'''Defino constantes para las dimensiones de lo que vamos a dibujar'''
#Formato 
# TEXTO = (POSICION_X, POSICION_Y, TAMAÑO_LETRA)
# RECTANGULO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# RECTANGULO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# OVALO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# OVALO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# IMAGEN = (POSICION_ESQUINA_X, POSICION_ESQUNA_Y)

DIMENSIONES_TEXTO_NUMEROS_POKEMONES = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.2, int(ctes.ALTO_VENTANA*0.03))
COORDENADA_TEXTO_STATS_IZQ = ctes.ANCHO_VENTANA*0.1625
COORDENADA_TEXTO_STATS_DER = ctes.ANCHO_VENTANA*0.85
TAMANIO_TEXTO_STATS = int(ctes.ALTO_VENTANA*0.04)
INDICE_MIN_STATS_DER = 7
DIMENSIONES_TEXTO_PRESIONA_B = (ctes.ANCHO_VENTANA*0.125, ctes.ALTO_VENTANA*0.84, int(ctes.ALTO_VENTANA*0.02))
DIMENSIONES_TEXTO_PRESIONA_R = (ctes.ANCHO_VENTANA*0.875, ctes.ALTO_VENTANA*0.84, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_TEXTO_TIPOS = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.26, int(ctes.ALTO_VENTANA*0.04))
RECTANGULO_NOMBRE_POKEMONES_X = (ctes.ANCHO_VENTANA*0.30625, ctes.ANCHO_VENTANA*0.70625)
RECTANGULO_NOMBRE_POKEMONES_Y = (ctes.ALTO_VENTANA*0.036, ctes.ALTO_VENTANA*0.16)
DIMENSION_IMAGEN_POKEMON = (ctes.ANCHO_VENTANA*0.275, ctes.ALTO_VENTANA*0.34)
PALABRA_BUSCAR = (ctes.ANCHO_VENTANA*0.125, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.04))
PALABRA_RANDOM = (ctes.ANCHO_VENTANA*0.875, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.04))
PALABRA_NOMBRE_POKEMON = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.1, int(ctes.ALTO_VENTANA*0.08))


def mostrar_ventana_vista_pokemons(pokemon_actual, lista_nombres_pokemones, diccionario_pokemons, colores_actuales):
    '''Dibuja la ventana de vista de Pokemons del Pokemon actual con sus caracteristicas'''
    nombre_pokemon = lista_nombres_pokemones[pokemon_actual]
    cantidad_pokemones = len(lista_nombres_pokemones)
    x1, x2 = RECTANGULO_NOMBRE_POKEMONES_X
    y1, y2 = RECTANGULO_NOMBRE_POKEMONES_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
    x1, x2 = ctes.DIMENSION_RECTANGULO_INF_DER_X
    y1, y2 = ctes.DIMENSION_RECTANGULO_INF_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
    x1, x2 = ctes.DIMENSION_RECTANGULO_INF_IZQ_X
    y1, y2 = ctes.DIMENSION_RECTANGULO_INF_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
    x, y, tamaño = PALABRA_BUSCAR
    gamelib.draw_text(ctes.TEXTO_BUSCAR, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x, y, tamaño = PALABRA_RANDOM
    gamelib.draw_text(ctes.TEXTO_RANDOM, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x, y, tamaño = PALABRA_NOMBRE_POKEMON
    gamelib.draw_text(nombre_pokemon, x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y = DIMENSION_IMAGEN_POKEMON
    gamelib.draw_image(diccionario_pokemons[nombre_pokemon][ctes.ENCABEZADO_POKEMONES[1]], x, y)
    numero_string = f'{pokemon_actual + 1} {ctes.BARRA} {cantidad_pokemones}'
    x, y, tamaño = DIMENSIONES_TEXTO_NUMEROS_POKEMONES
    gamelib.draw_text(numero_string, x, y, font = ctes.FUENTE, size = tamaño, italic = True, bold = True,fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    tipos_string = f'{ctes.BARRA}{ctes.BARRA}'.join(diccionario_pokemons[nombre_pokemon][ctes.ENCABEZADO_POKEMONES[3]])
    x, y, tamaño = DIMENSION_TEXTO_TIPOS
    gamelib.draw_text(tipos_string, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    dy = 0.1
    for stats in ctes.ENCABEZADO_POKEMONES[4:]:
        string_stat = stats.capitalize() + diccionario_pokemons[nombre_pokemon][stats]
        if ctes.ENCABEZADO_POKEMONES.index(stats) < INDICE_MIN_STATS_DER:
            x = COORDENADA_TEXTO_STATS_IZQ
        else:
            x = COORDENADA_TEXTO_STATS_DER
        if ctes.ENCABEZADO_POKEMONES.index(stats) == INDICE_MIN_STATS_DER:
            dy = 0.1
        y = ctes.ALTO_VENTANA*dy
        gamelib.draw_text(string_stat, x, y, font = ctes.FUENTE, size = TAMANIO_TEXTO_STATS, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        dy += 0.06
    x1, x2 = ctes.DIMENSION_OVALO_SIGUIENTE_X
    y1, y2 = ctes.DIMENSION_OVALO_SIG_ANT_Y
    gamelib.draw_oval(x1 , y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
    x1, x2 = ctes.DIMENSION_OVALO_ANTERIOR_X
    y1, y2 = ctes.DIMENSION_OVALO_SIG_ANT_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
    x1, x2 = ctes.OVALO_VOLVER_VENTANA_X
    y1, y2 = ctes.OVALO_VOLVER_VENTANA_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COLOR_ROJO, activefill = ctes.COLOR_ROSA)
    x, y, tamaño = DIMENSIONES_TEXTO_PRESIONA_B
    gamelib.draw_text(f'Presione {ctes.TECLA_BUSCAR}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSIONES_TEXTO_PRESIONA_R
    gamelib.draw_text(f'Presione {ctes.TECLA_POKEMON_RANDOM}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])

def evaluar_en_ventana_vista_pokemons(ev, pokemon_actual, lista_nombres_pokemones):
    '''Evalua la accion del usuario en la ventana vista pokemons y retorna la ventana actual
     y el pokemon_actual'''
    ventana_actual = ctes.VENTANA_VISTA_POKEMONS
    cantidad_pokemones = len(lista_nombres_pokemones)
    
    if ev.type == gamelib.EventType.ButtonPress:
        #El usuario clickeo
        x, y = ev.x, ev.y
        xc, yc, radio = ctes.DIMENSION_OVALO_SIGUIENTE
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            pokemon_actual = siguiente_indice(pokemon_actual, cantidad_pokemones)
        
        xc, yc, radio = ctes.DIMENSION_OVALO_ANTERIOR
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            pokemon_actual = anterior_indice(pokemon_actual, cantidad_pokemones)
        
        xc, yc, radio = ctes.DIMENSION_OVALO_ANTERIOR_VENTANA
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            ventana_actual = ctes.VENTANA_INICIAL
        
        xi, xf = ctes.DIMENSION_RECTANGULO_INF_IZQ_X
        yi, yf = ctes.DIMENSION_RECTANGULO_INF_Y
        if xi < x < xf and yi < y < yf:
            cadena = gamelib.input(mensajes.MENSAJE_INGRESE_POKEMON)
            pokemon_actual = buscar_pokemon(cadena, pokemon_actual, lista_nombres_pokemones)

        xi, xf = ctes.DIMENSION_RECTANGULO_INF_DER_X
        yi, yf = ctes.DIMENSION_RECTANGULO_INF_Y
        if xi < x < xf and yi < y < yf:  
            pokemon_actual = choice(range(cantidad_pokemones - 1))
            
    if ev.type == gamelib.EventType.KeyPress:
        #El usuario presiono una tecla
        if ev.key == ctes.TECLA_SIGUIENTE:
            pokemon_actual = siguiente_indice(pokemon_actual, cantidad_pokemones)
            
        if ev.key == ctes.TECLA_ANTERIOR:
            pokemon_actual = anterior_indice(pokemon_actual, cantidad_pokemones)
            
        if ev.key == ctes.TECLA_VENTANA_ANTERIOR:
            ventana_actual = ctes.VENTANA_INICIAL
        
        if ev.key == ctes.TECLA_BUSCAR:
            cadena = gamelib.input(mensajes.MENSAJE_INGRESE_POKEMON)
            pokemon_actual = buscar_pokemon(cadena, pokemon_actual, lista_nombres_pokemones)
        
        if ev.key == ctes.TECLA_POKEMON_RANDOM:
            pokemon_actual = choice(range(cantidad_pokemones-1))
        
        if ev.key == ctes.TECLA_VENTANA_EQUIPOS:
            ventana_actual = ctes.VENTANA_VISTA_EQUIPOS
            
        
    return ventana_actual, pokemon_actual
    