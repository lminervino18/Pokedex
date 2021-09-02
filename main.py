import gamelib
import constantes as ctes
import manejo_de_archivos
import mensajes
import ventana_inicial
import ventana_colores
import ventana_vista_pokemones
import ventana_vista_equipos
import ventana_vista_equipo_actual
from random import choice
from mostrar_pokedex import mostrar_ventana
from funciones_auxiliares import verificador_de_accion

ARCHIVO_POKEMONS = "pokemons.csv"
ARCHIVO_MOVIMIENTOS = "movimientos.csv"
ARCHIVO_DATOS_EQUIPOS = "equipos.csv"
ARCHIVO_ICONO = 'imgs/icono.gif'
TEXTO_POKEDEX = 'POKEDEX'
SEPARACION_TEXTO = '/'
                       
def main():
    '''Abre la ventana y evalua lo que hace el usuario'''
    
    #Define estado inicial
    ventana_actual = ctes.VENTANA_INICIAL
    lista_nombres_pokemones, diccionario_pokemons = manejo_de_archivos.cargar_pokemones(ARCHIVO_POKEMONS, ARCHIVO_MOVIMIENTOS)
    cantidad_pokemones = len(lista_nombres_pokemones)
    pokemon_actual = choice(range(cantidad_pokemones - 1)) 
    equipos, equipo_actual = manejo_de_archivos.cargar_equipos(ARCHIVO_DATOS_EQUIPOS)
    colores = choice(range(ctes.CANTIDAD_COLORES))
    
    gamelib.resize(ctes.ANCHO_VENTANA, ctes.ALTO_VENTANA)
    #Abre la ventana
    
    while gamelib.is_alive():
        
        #Define titulo e icono de la ventana
        gamelib.title(f'{TEXTO_POKEDEX}{SEPARACION_TEXTO}{SEPARACION_TEXTO}{ventana_actual}')
        gamelib.icon(ARCHIVO_ICONO)
        
        if ventana_actual == ctes.SALIR:
            #El usuario decidio salir y le pregunta si quiere guardar los datos
            if verificador_de_accion(mensajes.MENSAJE_VERIFICACION_GUARDAR_ANTES_DE_SALIR):
                manejo_de_archivos.guardar_datos_equipos(ARCHIVO_DATOS_EQUIPOS, equipos)
                gamelib.say(mensajes.MENSAJE_DATOS_GUARDADOS)
            break
        
        gamelib.draw_begin()
        #Dibuja la ventana actual
        mostrar_ventana(ventana_actual, pokemon_actual, diccionario_pokemons, lista_nombres_pokemones, equipos, equipo_actual, colores)
        gamelib.draw_end()

        ev = gamelib.wait()
        #Espera evaluacion del usuario

        if not ev:
            #El usuario cerro la ventana
            break
        
        #Dependiendo de la ventana actual evalua de diferente forma la accion
        if ventana_actual == ctes.VENTANA_INICIAL:
            ventana_actual = ventana_inicial.evaluar_en_ventana_inicial(ev)
            continue

        if ventana_actual == ctes.VENTANA_VISTA_POKEMONS:
            ventana_actual, pokemon_actual = ventana_vista_pokemones.evaluar_en_ventana_vista_pokemons(ev, pokemon_actual, lista_nombres_pokemones)
            continue
        
        if ventana_actual == ctes.VENTANA_VISTA_EQUIPOS:
            ventana_actual, equipos, equipo_actual = ventana_vista_equipos.evaluar_en_ventana_vista_equipos(ev, equipos, equipo_actual, diccionario_pokemons, lista_nombres_pokemones)
            continue
        
        if ventana_actual == ctes.VENTANA_EQUIPO_ACTUAL:
            ventana_actual, equipos = ventana_vista_equipo_actual.evaluar_en_ventana_equipo_actual(ev, equipos, equipo_actual, diccionario_pokemons, lista_nombres_pokemones)
            continue

        if ventana_actual == ctes.VENTANA_COLORES:
            ventana_actual, colores = ventana_colores.evaluar_en_ventana_colores(ev, colores)
    
gamelib.init(main)