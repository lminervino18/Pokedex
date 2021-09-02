import gamelib
import constantes as ctes
import ventana_inicial
import ventana_colores
import ventana_vista_pokemones
import ventana_vista_equipos
import ventana_vista_equipo_actual

DIMENSON_RECTANGULO_PRINCIPAL_X = (ctes.ANCHO_VENTANA*0.0125, ctes.ANCHO_VENTANA*0.9875)
DIMENSON_RECTANGULO_PRINCIPAL_Y = (ctes.ALTO_VENTANA*0.02, ctes.ALTO_VENTANA*0.98)

def mostrar_ventana(ventana_actual, pokemon_actual, diccionario_pokemons, lista_nombres_pokemones, equipos, equipo_actual, colores_actuales):

    "Dibuja el rectangulo principal y dependiendo de la ventana_actual dibuja su representación"
    x1, x2 = DIMENSON_RECTANGULO_PRINCIPAL_X
    y1, y2 = DIMENSON_RECTANGULO_PRINCIPAL_Y
    gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][0])
    
    if ventana_actual == ctes.VENTANA_INICIAL:
        ventana_inicial.mostrar_ventana_inicial(colores_actuales)
        
    if ventana_actual == ctes.VENTANA_VISTA_POKEMONS:
        ventana_vista_pokemones.mostrar_ventana_vista_pokemons(pokemon_actual, lista_nombres_pokemones, diccionario_pokemons, colores_actuales)
        
    if ventana_actual == ctes.VENTANA_VISTA_EQUIPOS:
        ventana_vista_equipos.mostrar_ventana_vista_equipos(equipos, equipo_actual, colores_actuales)
            
    if ventana_actual == ctes.VENTANA_EQUIPO_ACTUAL:
        ventana_vista_equipo_actual.mostrar_ventana_equipo_actual(equipos, equipo_actual, colores_actuales)

    if ventana_actual == ctes.VENTANA_COLORES:
        ventana_colores.mostrar_ventana_colores(colores_actuales)
    
    return
        