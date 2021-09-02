import constantes as ctes
import mensajes
import gamelib
import manejo_de_archivos
from funciones_auxiliares import siguiente_indice, anterior_indice, verificador_de_accion, esta_dentro_circuferencia
from Equipo import Equipo_pk

ARCHIVO_DATOS_EQUIPOS = "equipos.csv"

'''Defino constantes para las dimensiones de lo que vamos a dibujar'''
#Formato 
# TEXTO = (POSICION_X, POSICION_Y, TAMAÑO_LETRA)
# RECTANGULO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# RECTANGULO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# OVALO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# OVALO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# IMAGEN = (POSICION_ESQUINA_X, POSICION_ESQUNA_Y)

DIMENSION_RECTANGULO_NOMBRE_EQUIPO_X = (ctes.ANCHO_VENTANA*0.1875, ctes.ANCHO_VENTANA*0.8125)
DIMENSION_RECTANGULO_NOMBRE_EQUIPO_Y = (ctes.ALTO_VENTANA*0.036, ctes.ALTO_VENTANA*0.16)
DIMENSION_PALABRA_CREAR_EQUIPO = (ctes.ANCHO_VENTANA*0.125, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.04))
DIMENSION_PALABRA_BORRAR_EQUIPO = (ctes.ANCHO_VENTANA*0.875, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.04))
DIMENSION_PALABRA_PRESIONA_C = (ctes.ANCHO_VENTANA*0.125, ctes.ALTO_VENTANA*0.84, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_PALABRA_PRESIONA_B = (ctes.ANCHO_VENTANA*0.875, ctes.ALTO_VENTANA*0.84, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_PALABRA_PRESIONA_G = (ctes.ANCHO_VENTANA*0.86875, ctes.ALTO_VENTANA*0.012, int(ctes.ALTO_VENTANA*0.016))
DIMENSION_TEXTO_CREA_TUS_EQUIPOS = (ctes.ANCHO_VENTANA*0.5125, ctes.ALTO_VENTANA*0.55, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_NOMBRE_EQUIPO = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.1, int(ctes.ALTO_VENTANA*0.08))
DIMENSION_PALABRA_NOMBRE_EQUIPO = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.1, int(ctes.ALTO_VENTANA*0.08))
DIMENSION_TEXTO_PRESIONA_ESPACIO = (ctes.ANCHO_VENTANA*0.5125, ctes.ALTO_VENTANA*0.5, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_CANTIDAD_EQUIPOS = (ctes.ANCHO_VENTANA*0.5125, ctes.ALTO_VENTANA*0.6, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_NOMBRE_DEL_EQUIPO = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.1, int(ctes.ALTO_VENTANA*0.08))


def crear_equipo():
    '''Le pide al usuario el nombre del equipo a crear y retorna un nuevo equipo'''
    nombre_equipo = gamelib.input(mensajes.MENSAJE_NUEVO_NOMBRE_EQUIPO)
    if not nombre_equipo:
        return 
    nuevo_equipo = Equipo_pk(nombre_equipo)
    return nuevo_equipo

def borrar_equipo_actual(equipos, equipo_actual):
    '''Recibe una lista de equipos y el equipo actual (indice), verifica que el usuario quiera borrarlo,
    borra el equipo actual y retorna la nueva lista de equipos y el nuevo equipo actual'''
    if verificador_de_accion(mensajes.MENSAJES_VERIFICACION_BORRAR_EQUIPO_ACTUAL):
        objeto_equipo = equipos[equipo_actual]
        equipos.remove(objeto_equipo)
        if len(equipos) == 0:
            equipo_actual = None
        else:
            cantidad_equipos = len(equipos)
            equipo_actual = anterior_indice(equipo_actual, cantidad_equipos)
    return equipos, equipo_actual

def mostrar_ventana_vista_equipos(equipos, equipo_actual, colores_actuales):
    '''Dibuja la ventana de vista equipos de la Pokedex del equipo actual'''

    
    x1, x2 = DIMENSION_RECTANGULO_NOMBRE_EQUIPO_X
    y1, y2 = DIMENSION_RECTANGULO_NOMBRE_EQUIPO_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
    x1, x2 = ctes.DIMENSION_RECTANGULO_INF_DER_X
    y1, y2 = ctes.DIMENSION_RECTANGULO_INF_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
    x1, x2 = ctes.DIMENSION_RECTANGULO_INF_IZQ_X
    y1, y2 = ctes.DIMENSION_RECTANGULO_INF_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], outline = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamanio = DIMENSION_PALABRA_CREAR_EQUIPO
    gamelib.draw_text(ctes.TEXTO_PALABRA_CREAR, x, y, font = ctes.FUENTE, size = tamanio, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x, y, tamanio = DIMENSION_PALABRA_BORRAR_EQUIPO
    gamelib.draw_text(ctes.TEXTO_PALABRA_BORRAR, x, y, font = ctes.FUENTE, size = tamanio, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
    x1, x2 = ctes.DIMENSION_OVALO_SIGUIENTE_X
    y1, y2 = ctes.DIMENSION_OVALO_SIG_ANT_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
    x1, x2 = ctes.DIMENSION_OVALO_ANTERIOR_X
    y1, y2 = ctes.DIMENSION_OVALO_SIG_ANT_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
    x1, x2 = ctes.OVALO_VOLVER_VENTANA_X
    y1, y2 = ctes.OVALO_VOLVER_VENTANA_Y
    gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COLOR_ROJO, activefill = ctes.COLOR_ROSA)
    x, y, tamaño = DIMENSION_PALABRA_PRESIONA_C
    gamelib.draw_text(f'Presione {ctes.TECLA_CREAR_EQUIPO}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSION_PALABRA_PRESIONA_B
    gamelib.draw_text(f'Presione {ctes.TECLA_BORRAR}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
    x, y, tamaño = DIMENSION_PALABRA_PRESIONA_G
    gamelib.draw_text(f'Presione {ctes.TECLA_GUARDAR}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COLOR_BLANCO)
    
    if equipo_actual == None:
        x, y, tamaño = DIMENSION_TEXTO_CREA_TUS_EQUIPOS
        gamelib.draw_text(ctes.TEXTO_CREA_TUS_EQUIPOS, x, y, font = ctes.FUENTE, size = tamaño, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_PALABRA_NOMBRE_EQUIPO
        gamelib.draw_text(ctes.TEXTO_NOMBRE_EQUIPO, x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        
    else:
        objeto_equipo = equipos[equipo_actual]
        x, y, tamaño = DIMENSION_TEXTO_PRESIONA_ESPACIO
        gamelib.draw_text(ctes.TEXTO_PRESIONE_ESPACIO, x, y, size = tamaño, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_TEXTO_CANTIDAD_EQUIPOS
        gamelib.draw_text(f'{objeto_equipo.cantidad_pokemones()} {ctes.TEXTO_POKEMONES}', x, y, font = ctes.FUENTE, size = tamaño, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_TEXTO_NOMBRE_DEL_EQUIPO
        gamelib.draw_text(f'{objeto_equipo.obtener_nombre()}', x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])

def evaluar_en_ventana_vista_equipos(ev, equipos, equipo_actual, diccionario_pokemons, lista_nombres_pokemones):
    '''Evalua la accion del usuario en la ventana vista equipos y retorna la ventana_actual, la lista de equipos
    y el equipo actual'''
    ventana_actual = ctes.VENTANA_VISTA_EQUIPOS
    cantidad_equipos = len(equipos)
    
    if ev.type == gamelib.EventType.KeyPress:
        #El usuario clickeo

        if ev.key == ctes.TECLA_VENTANA_ANTERIOR:
            ventana_actual = ctes.VENTANA_INICIAL
        
        if ev.key == ctes.TECLA_CREAR_EQUIPO:
            nuevo_equipo = crear_equipo()
            if nuevo_equipo:
                equipos.append(nuevo_equipo)
                equipo_actual = equipos.index(nuevo_equipo)
        
        if ev.key == ctes.TECLA_VER_EQUIPO_ACTUAL and equipo_actual != None:
            ventana_actual = ctes.VENTANA_EQUIPO_ACTUAL
            
        if ev.key == ctes.TECLA_BORRAR and equipo_actual != None:
            equipos, equipo_actual = borrar_equipo_actual(equipos, equipo_actual)
        
        if ev.key == ctes.TECLA_SIGUIENTE and equipo_actual != None:
            equipo_actual = siguiente_indice(equipo_actual, cantidad_equipos)
        
        if ev.key == ctes.TECLA_ANTERIOR and equipo_actual != None:
            equipo_actual = anterior_indice(equipo_actual, cantidad_equipos)
        
        if ev.key == ctes.TECLA_GUARDAR:
            if verificador_de_accion(mensajes.MENSAJE_VERIFICACION_GUARDAR_DATOS):
                manejo_de_archivos.guardar_datos_equipos(ARCHIVO_DATOS_EQUIPOS, equipos)
                gamelib.say(mensajes.MENSAJE_DATOS_GUARDADOS)
        
    if ev.type == gamelib.EventType.ButtonPress:
        #El usuario presiono una tecla
        
        x, y = ev.x, ev.y

        xc, yc, radio = ctes.DIMENSION_OVALO_SIGUIENTE
        if esta_dentro_circuferencia(x, y, xc, yc, radio) and equipo_actual != None:
            equipo_actual = siguiente_indice(equipo_actual, cantidad_equipos)
        
        xc, yc, radio = ctes.DIMENSION_OVALO_ANTERIOR
        if esta_dentro_circuferencia(x, y, xc, yc, radio) and equipo_actual != None:
            equipo_actual = anterior_indice(equipo_actual, cantidad_equipos)
        
        xc, yc, radio = ctes.DIMENSION_OVALO_ANTERIOR_VENTANA
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            ventana_actual = ctes.VENTANA_INICIAL
        
        xi, xf = ctes.DIMENSION_RECTANGULO_INF_IZQ_X
        yi, yf = ctes.DIMENSION_RECTANGULO_INF_Y
        if xi < x < xf and yi < y < yf:
            nuevo_equipo = crear_equipo()
            if nuevo_equipo:
                equipos.append(nuevo_equipo)
                equipo_actual = equipos.index(nuevo_equipo)
        
        xi, xf = ctes.DIMENSION_RECTANGULO_INF_DER_X
        yi, yf = ctes.DIMENSION_RECTANGULO_INF_Y
        if xi < x < xf and yi < y < yf and equipo_actual != None:
            equipos, equipo_actual = borrar_equipo_actual(equipos, equipo_actual)
        
    return ventana_actual, equipos, equipo_actual