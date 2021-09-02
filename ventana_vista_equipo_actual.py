import constantes as ctes
import gamelib
import mensajes
import manejo_de_archivos
from funciones_auxiliares import buscar_pokemon, verificador_de_accion, esta_dentro_circuferencia

'''Defino constantes a utilizar'''

CLAVE_MOVIMIENTOS = 'movimientos'
SALTO_DE_LINEA = '\n'
COMA_ESPACIO = ', '
ARCHIVO_DATOS_EQUIPOS = "equipos.csv"

'''Defino constantes para las dimensiones de lo que vamos a dibujar'''
#Formato 
# TEXTO = (POSICION_X, POSICION_Y, TAMAÑO_LETRA)
# RECTANGULO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# RECTANGULO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# OVALO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# OVALO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# IMAGEN = (POSICION_ESQUINA_X, POSICION_ESQUNA_Y)

RECTANGULO_BOTON_AGREGAR_MOV_X = (ctes.ANCHO_VENTANA*0.0375, ctes.ANCHO_VENTANA*0.20875)
RECTANGULO_BOTON_BORRAR_MOV_X = (ctes.ANCHO_VENTANA*0.2825, ctes.ANCHO_VENTANA*0.465)
RECTANGULO_BOTON_AGREGAR_PK_X = (ctes.ANCHO_VENTANA*0.81125, ctes.ANCHO_VENTANA*0.935)
RECTANGULO_BOTON_BORRAR_PK = (ctes.ANCHO_VENTANA*0.56125, ctes.ANCHO_VENTANA*0.685)
RECTANGULO_BOTONES_EQUIPO_ACTUAL_Y = (ctes.ALTO_VENTANA*0.842, ctes.ALTO_VENTANA*0.95)
RECTANGULO_POKEMON_EQUIPO_X = (ctes.ANCHO_VENTANA*0.1875, ctes.ANCHO_VENTANA*0.8125)
RECTANGULO_POKEMON_EQUIPO_Y = (ctes.ALTO_VENTANA*0.036, ctes.ALTO_VENTANA*0.16)
DIMENSION_PALABRA_PRESIONA_G = (ctes.ANCHO_VENTANA*0.86875, ctes.ALTO_VENTANA*0.012, int(ctes.ALTO_VENTANA*0.016))

DIMENSION_TEXTO_AGREGAR_MOV = (ctes.ANCHO_VENTANA*0.125, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_BORRAR_PK = (ctes.ANCHO_VENTANA*0.875, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_AGREGAR_PK = (ctes.ANCHO_VENTANA*0.625, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_BORRAR_MOV = (ctes.ANCHO_VENTANA*0.375, ctes.ALTO_VENTANA*0.9, int(ctes.ALTO_VENTANA*0.036))
DIMENSION_TEXTO_PRESIONE_M = (ctes.ANCHO_VENTANA*0.11875, ctes.ALTO_VENTANA*0.82, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_TEXTO_PRESIONE_N = (ctes.ANCHO_VENTANA*0.3775, ctes.ALTO_VENTANA*0.82, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_TEXTO_PRESIONE_A = (ctes.ANCHO_VENTANA*0.6225, ctes.ALTO_VENTANA*0.82, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_TEXTO_PRESIONE_B = (ctes.ANCHO_VENTANA*0.87125, ctes.ALTO_VENTANA*0.82, int(ctes.ALTO_VENTANA*0.02))
DIMENSION_TEXTO_NOMBRE_EQUIPO = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.2, int(ctes.ALTO_VENTANA*0.05))
DIMENSION_NOMBRE_POKEMON = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.1, int(ctes.ALTO_VENTANA*0.06))
DIMENSION_TEXTO_NO_HAY_PK = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.5, int(ctes.ALTO_VENTANA*0.06))
DIMENSION_TEXTO_MOV = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.3, int(ctes.ALTO_VENTANA*0.04))
DIMENSION_STRING_MOVS = (ctes.ANCHO_VENTANA*0.5, ctes.ALTO_VENTANA*0.6, int(ctes.ALTO_VENTANA*0.06))

'''Defino constantes sobre las dimensiones de los botones'''
#FORMATO
#DIMENSION_X = (COORDENAD_X_INICIO, COORDENADA_X_FINAL)
#DIMENSION_Y = (COORDENAD_Y_INICIO, COORDENADA_Y_FINAL)
#DIMENSION_OVALO = (COORDENADA_CENTRO_X, COORDENADA_CENTRO_Y, RADIO)

DIMENSION_BOTON_AGREGAR_MOVIMIENTO_X = (ctes.ANCHO_VENTANA*0.03875, ctes.ANCHO_VENTANA*0.20625) 
DIMENSION_BOTON_AGREGAR_MOVIMIENTO_Y = (ctes.ALTO_VENTANA*0.848, ctes.ALTO_VENTANA*0.942)
DIMENSION_BOTON_BORRAR_MOVIMIENTO_X = (ctes.ANCHO_VENTANA*0.285, ctes.ANCHO_VENTANA*0.4625)
DIMENSION_BOTON_BORRAR_MOVIMIENTO_Y = (ctes.ALTO_VENTANA*0.846, ctes.ALTO_VENTANA*0.948) 
DIMENSION_BOTON_AGREGAR_POKEMON_X = (ctes.ANCHO_VENTANA*0.56125, ctes.ANCHO_VENTANA*0.68375) 
DIMENSION_BOTON_AGREGAR_POKEMON_Y = (ctes.ALTO_VENTANA*0.846, ctes.ALTO_VENTANA*0.946)
DIMENSION_BOTON_BORRAR_POKEMON_X = (ctes.ANCHO_VENTANA*0.81125, ctes.ANCHO_VENTANA*0.9325)
DIMENSION_BOTON_BORRAR_POKEMON_Y = (ctes.ALTO_VENTANA*0.838, ctes.ALTO_VENTANA*0.948) 

def crear_string_movimientos(lista_movimientos):
    '''Recibe una lista con movimientos y retorna un string con los movimientos y su indice'''
    cantidad_movimientos = len(lista_movimientos)
    string = ''
    for indice, movimiento in enumerate(lista_movimientos):
        string += movimiento
        if not indice == cantidad_movimientos - 1:
            string += ctes.SALTO_DE_LINEA
    return string

def agregar_pokemon_a_equipo(objeto_equipo, equipos, diccionario_pokemons, lista_nombres_pokemones):
    '''Recibe el objeto equipo, la lista de equipos, el diccionario con las caracteristicas de los pokemones, la
    lista con los nombres. Le pide al usuario el pokemon a agregar y un movimiento obligatoriamente. Si algun dato
    ingresado por el usuario es incorrecto retora el estado actual de los equipo. Sino modifica el objeto y la lista de equipos 
    y l a retorna'''
    cantidad_inicial_pokemons = len(objeto_equipo.obtener_pokemons())
    indice_equipo = equipos.index(objeto_equipo)
    nombre_pokemon = gamelib.input(mensajes.MENSAJE_INGRESE_POKEMON)
    if not nombre_pokemon:
        return equipos
    if not nombre_pokemon.isdigit() and nombre_pokemon not in lista_nombres_pokemones:
        gamelib.say(mensajes.MENSAJE_POKEMON_INEXISTENTE)
        return equipos
    pokemon_nuevo = buscar_pokemon(nombre_pokemon, None, lista_nombres_pokemones)
    if not pokemon_nuevo:
        return equipos
    nombre_pokemon = lista_nombres_pokemones[pokemon_nuevo]
    lista_movimientos_posibles, string_mov_posibles = crear_movimientos_posibles(lista_nombres_pokemones, diccionario_pokemons, pokemon_nuevo, objeto_equipo)
    if not lista_movimientos_posibles:
        gamelib.say(mensajes.MENSAJE_POKEMON_SIN_MOVS)
        return equipos
    numero_movimiento = gamelib.input(f'{mensajes.MENSAJE_INGRESE_NUMERO_MOV}\n{string_mov_posibles}')
    if not numero_movimiento.isdigit():
        gamelib.say(mensajes.MENSAJE_NUMERO_INCORRECTO)
        return equipos
    if int(numero_movimiento) - 1 not in range(len(lista_movimientos_posibles)):
        gamelib.say(mensajes.MENSAJE_NUMERO_NO_ESTABA_EN_LAS_OPCIONES)
        return equipos
    movimiento = lista_movimientos_posibles[int(numero_movimiento) - 1]
    objeto_equipo.agregar_pokemon(nombre_pokemon, movimiento)
    if cantidad_inicial_pokemons > 5:
        gamelib.say(mensajes.MENSAJE_NO_SE_PUEDEN_AGREGAR_POKEMONS)
    elif len(objeto_equipo.obtener_pokemons()) == cantidad_inicial_pokemons:
        gamelib.say(mensajes.MENSAJE_POKEMON_YA_ESTA_EN_EL_EQUIPO)
    equipos[indice_equipo] = objeto_equipo
    return equipos

def crear_movimientos_posibles(lista_nombres_pokemones, diccionario_pokemones, pokemon_actual, objeto_equipo):
    '''Esta funcion recibe la lista de los nombres, el diccionario de los pokemon con sus caracteristicas.
    el pokemon_actual y el objeto_equipo. Retorna una lista con los movimientos del pokemon actual y un string
    con los movimientos y sus indices para que el usuario pueda elegir'''
    lista_movimientos_posibles = []
    nombre_pokemon = lista_nombres_pokemones[pokemon_actual]
    if CLAVE_MOVIMIENTOS not in diccionario_pokemones[nombre_pokemon].keys():
        return None, None
    for movimiento in diccionario_pokemones[nombre_pokemon][CLAVE_MOVIMIENTOS]:
        if pokemon_actual not in objeto_equipo.obtener_pokemons():
            lista_movimientos_posibles.append(movimiento)
            continue
        if movimiento not in objeto_equipo.obtener_movimientos(nombre_pokemon):
            lista_movimientos_posibles.append[movimiento]
    string_mov_posibles = ''
    contador = 1
    
    for movimiento in lista_movimientos_posibles:
        string_mov_posibles += f'{contador}: {movimiento}'
        if contador % 5 == 0:
            string_mov_posibles += SALTO_DE_LINEA
        else:
            if contador != len(lista_movimientos_posibles):
                string_mov_posibles += COMA_ESPACIO   
        contador += 1
    return lista_movimientos_posibles, string_mov_posibles

def agregar_movimiento_a_pokemon_actual (objeto_equipo, equipos, diccionario_pokemons, lista_nombres_pokemones):
    '''Recibe el objeto equipo, la lista de equipos, el diccionario con los pokemons y sus caracteristicas,
    la lista de nombres. Le pide al usuario un movimiento para agregarle al pokemon actual del objeto equipo
    Si algun dato ingresado no es valido retorna el estado actual de los equipos. Sino modifica el objeto actual
    y la lista de equipos y la retorna'''
    indice_equipo = equipos.index(objeto_equipo)
    nombre_pokemon_actual = objeto_equipo.obtener_pokemon_actual()
    numero_pokemon_actual = buscar_pokemon(nombre_pokemon_actual, None, lista_nombres_pokemones)
    lista_movimientos_posibles, string_mov_posibles = crear_movimientos_posibles(lista_nombres_pokemones, diccionario_pokemons, numero_pokemon_actual, objeto_equipo)
    numero_movimiento_elegido = gamelib.input(f'{mensajes.MENSAJE_INGRESE_MOVIMIENTO}\n{string_mov_posibles}')
    if not numero_movimiento_elegido:
        return equipos
    if not numero_movimiento_elegido.isdigit():
        gamelib.say(mensajes.MENSAJE_NUMERO_INCORRECTO)
        return equipos
    numero_movimiento_elegido = int(numero_movimiento_elegido) - 1
    if numero_movimiento_elegido not in range(len(lista_movimientos_posibles)):
        gamelib.say(mensajes.MENSAJE_NUMERO_NO_ESTABA_EN_LAS_OPCIONES)
        return equipos
    movimiento_elegido = lista_movimientos_posibles[numero_movimiento_elegido]
    if movimiento_elegido in objeto_equipo.obtener_movimientos(nombre_pokemon_actual):
        gamelib.say(mensajes.MENSAJE_MOV_YA_INCLUIDO)
        return equipos
    if len(objeto_equipo.obtener_movimientos(nombre_pokemon_actual))  ==  4:
        gamelib.say(mensajes.MENSAJE_CANTIDAD_MOV_EXCEDIDA)
        return equipos
    objeto_equipo.agregar_movimiento(nombre_pokemon_actual,movimiento_elegido)
    equipos[indice_equipo] = objeto_equipo
    return equipos

def avanzar_a_siguiente_pokemon(objeto_equipo, equipos):
    '''Recibe el objeto equipo y la lista de equipos. Avanza un pokemon_actual del
    objeto equipo, modifica la lista de los equipos y la retorna'''
    indice_equipo_actual = equipos.index(objeto_equipo)
    objeto_equipo.avanzar_pokemon_actual()
    equipos[indice_equipo_actual] = objeto_equipo
    return equipos

def retroceder_a_anterior_pokemon(objeto_equipo,equipos):
    '''Recibe el objeto equipo y la lista de equipos. Retrocede un pokemon_actual del
    objeto equipo, modifica la lista de los equipos y la retorna'''
    indice_equipo_actual = equipos.index(objeto_equipo)
    objeto_equipo.retroceder_pokemon_actual()
    equipos[indice_equipo_actual] = objeto_equipo
    return equipos

def crear_string_movimientos_actuales(movimientos_actuales):
    '''Recibe una lista de movimientos y retorna un string con los movimientos 
    y sus indices'''
    string = mensajes.MENSAJE_INGRESE_NUMERO_MOVIMIENTO_A_BORRAR 
    for i in range(len(movimientos_actuales)):
        string += f'{i + 1}: {movimientos_actuales[i]}'
        if i != len(movimientos_actuales) - 1:
            string += SALTO_DE_LINEA
    return string

def borrar_movimiento(objeto_equipo,equipos):
    '''Recibe el objeto equipo y la lista de equipos. Le muestra al usuario que movimientos tiene
    y le pide que elija uno. Si alguna accion es incorrecta retorna el estado actual de equipos. Sino modifica
    el objeto equipo y la lista de  equipos y la retorna'''
    indice_objeto_equipo = equipos.index(objeto_equipo)
    pokemon_actual = objeto_equipo.obtener_pokemon_actual()
    movimientos_actuales = objeto_equipo.obtener_movimientos(pokemon_actual)
    string_movimientos_actuales = crear_string_movimientos_actuales(movimientos_actuales)
    numero_movimiento_a_borrar = gamelib.input(string_movimientos_actuales)
    if numero_movimiento_a_borrar == None:
        return equipos
    if not numero_movimiento_a_borrar.isdigit():
        gamelib.say(mensajes.MENSAJE_NUMERO_INCORRECTO)
        return equipos
    numero_movimiento_a_borrar = int(numero_movimiento_a_borrar) - 1
    if numero_movimiento_a_borrar not in range(len(movimientos_actuales)):
        gamelib.say(mensajes.MENSAJE_NUMERO_NO_ESTABA_EN_LAS_OPCIONES)
        return equipos
    movimiento_a_borrar = movimientos_actuales[numero_movimiento_a_borrar]
    if len(objeto_equipo.obtener_movimientos(pokemon_actual)) - 1 == 0:
            gamelib.say(mensajes.MENSAJE_NO_SE_PUEDE_BORRAR_MOV)
            return equipos
    if len(objeto_equipo.obtener_movimientos(pokemon_actual)) == 1:
        gamelib.say(mensajes.MENSAJE_NO_SE_PUEDE_BORRAR_MOV)
        return equipos
    objeto_equipo.sacar_movimiento(pokemon_actual, movimiento_a_borrar)
    equipos[indice_objeto_equipo] = objeto_equipo
    return equipos

def mostrar_ventana_equipo_actual(equipos, equipo_actual, colores_actuales):
        '''Dibuja la ventana de vista del equipo actual de la Pokedex del equipo actual con sus caracteristicas'''
        objeto_equipo = equipos[equipo_actual]
        x1, x2 = RECTANGULO_POKEMON_EQUIPO_X
        y1, y2 = RECTANGULO_POKEMON_EQUIPO_Y
        gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], outline = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x1, x2 = RECTANGULO_BOTON_AGREGAR_MOV_X
        y1, y2 = RECTANGULO_BOTONES_EQUIPO_ACTUAL_Y
        gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
        x1, x2 = RECTANGULO_BOTON_BORRAR_MOV_X
        gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
        x1, x2 = RECTANGULO_BOTON_AGREGAR_PK_X
        gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
        x1, x2 = RECTANGULO_BOTON_BORRAR_PK
        gamelib.draw_rectangle(x1, y1, x2, y2, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1])
        x, y, tamaño = DIMENSION_TEXTO_AGREGAR_MOV
        gamelib.draw_text(ctes.TEXTO_AGREGAR_MOVIMIENTO, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
        x, y, tamaño = DIMENSION_TEXTO_BORRAR_PK
        gamelib.draw_text(ctes.TEXTO_BORRAR_POKEMON, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
        x, y, tamaño = DIMENSION_TEXTO_AGREGAR_PK
        gamelib.draw_text(ctes.TEXTO_AGREGAR_POKEMON, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
        x, y, tamaño = DIMENSION_TEXTO_BORRAR_MOV
        gamelib.draw_text(ctes.TEXTO_BORRAR_MOVIMIENTO, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2], activefill = ctes.COLOR_GRIS)
        x1, x2 = ctes.DIMENSION_OVALO_SIGUIENTE_X
        y1, y2 = ctes.DIMENSION_OVALO_SIG_ANT_Y
        gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
        x1, x2 = ctes.DIMENSION_OVALO_ANTERIOR_X
        gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][1], activefill = ctes.COLOR_GRIS)
        x1, x2 = ctes.OVALO_VOLVER_VENTANA_X
        y1, y2 = ctes.OVALO_VOLVER_VENTANA_Y
        gamelib.draw_oval(x1, y1, x2, y2, outline = ctes.COLOR_NEGRO, fill = ctes.COLOR_ROJO, activefill = ctes.COLOR_ROSA)
        x, y, tamaño = DIMENSION_TEXTO_NOMBRE_EQUIPO
        gamelib.draw_text(f'{ctes.TEXTO_EQUIPO_SINGULAR}{objeto_equipo.obtener_nombre()}', x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_TEXTO_PRESIONE_M
        gamelib.draw_text(f'Presione {ctes.TECLA_AGREGAR_MOV}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_TEXTO_PRESIONE_N
        gamelib.draw_text(f'Presione {ctes.TECLA_BORRAR_MOV}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_TEXTO_PRESIONE_A
        gamelib.draw_text(f'Presione {ctes.TECLA_AGREGAR_POKEMON}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_TEXTO_PRESIONE_B
        gamelib.draw_text(f'Presione {ctes.TECLA_BORRAR}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        x, y, tamaño = DIMENSION_PALABRA_PRESIONA_G
        gamelib.draw_text(f'Presione {ctes.TECLA_GUARDAR}:', x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COLOR_BLANCO)

        x, y, tamaño = DIMENSION_NOMBRE_POKEMON
        if objeto_equipo.esta_vacio():
            gamelib.draw_text(ctes.TEXTO_NOMBRE_POKEMON, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
            x, y, tamaño = DIMENSION_TEXTO_NO_HAY_PK
            gamelib.draw_text(ctes.TEXTO_NO_HAY_POK, x, y, font = ctes.FUENTE, size = tamaño, italic = False, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
        else:
            pokemon_actual = objeto_equipo.obtener_pokemon_actual()
            gamelib.draw_text(f'{pokemon_actual}', x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
            x, y, tamaño = DIMENSION_TEXTO_MOV
            gamelib.draw_text(ctes.TEXTO_MOV , x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])
            string_movimientos = crear_string_movimientos(objeto_equipo.obtener_movimientos(pokemon_actual))
            x, y, tamaño = DIMENSION_STRING_MOVS
            gamelib.draw_text(string_movimientos, x, y, font = ctes.FUENTE, size = tamaño, italic = True, fill = ctes.COMBINACION_DE_COLORES[colores_actuales][2])

def evaluar_en_ventana_equipo_actual(ev, equipos, equipo_actual, diccionario_pokemons, lista_nombres_pokemones):
    '''Evalua la accion del usuario en la ventana vista equipo actual 
    y retorna la ventana_actual y la lista de equipos'''
    ventana_actual = ctes.VENTANA_EQUIPO_ACTUAL
    objeto_equipo = equipos[equipo_actual]
    pokemon_actual = objeto_equipo.obtener_pokemon_actual()
    
    if ev.type == gamelib.EventType.KeyPress:
        #El usuario presiono una tecla
        if ev.key == ctes.TECLA_VENTANA_ANTERIOR:
            ventana_actual = ctes.VENTANA_VISTA_EQUIPOS

        if ev.key == ctes.TECLA_AGREGAR_POKEMON:
            equipos = agregar_pokemon_a_equipo(objeto_equipo, equipos, diccionario_pokemons, lista_nombres_pokemones)
            objeto_equipo.avanzar_pokemon_actual()

        if ev.key == ctes.TECLA_BORRAR and pokemon_actual:
            print(objeto_equipo.pokemon_actual)
            if verificador_de_accion(mensajes.MENSAJE_VERIFICACION_BORRAR_POKEMON_ACTUAL):
                pokemon_a_eliminar = objeto_equipo.obtener_pokemon_actual()
                objeto_equipo.avanzar_pokemon_actual()
                print(objeto_equipo.pokemon_actual)
                objeto_equipo.eliminar_pokemon(pokemon_a_eliminar)

        if ev.key == ctes.TECLA_AGREGAR_MOV and pokemon_actual:
            equipos = agregar_movimiento_a_pokemon_actual(objeto_equipo, equipos, diccionario_pokemons, lista_nombres_pokemones)
        
        if ev.key == ctes.TECLA_SIGUIENTE:
            equipos = avanzar_a_siguiente_pokemon(objeto_equipo, equipos)

        if ev.key == ctes.TECLA_ANTERIOR:
            equipos = retroceder_a_anterior_pokemon(objeto_equipo, equipos)
        
        if ev.key == ctes.TECLA_BORRAR_MOV and pokemon_actual:
            equipos = borrar_movimiento(objeto_equipo, equipos)
        
        if ev.key == ctes.TECLA_GUARDAR:
            if verificador_de_accion(mensajes.MENSAJE_VERIFICACION_GUARDAR_DATOS):
                manejo_de_archivos.guardar_datos_equipos(ARCHIVO_DATOS_EQUIPOS, equipos)
                gamelib.say(mensajes.MENSAJE_DATOS_GUARDADOS)
        
    if ev.type == gamelib.EventType.ButtonPress:
        #El usuario clickeo

        x, y = ev.x, ev.y
        xi, xf = DIMENSION_BOTON_AGREGAR_MOVIMIENTO_X
        yi, yf = DIMENSION_BOTON_AGREGAR_MOVIMIENTO_Y
        if xi < x < xf and yi < y < yf and pokemon_actual != None:
            equipos = agregar_movimiento_a_pokemon_actual(objeto_equipo, equipos, diccionario_pokemons, lista_nombres_pokemones)
        
        xi, xf = DIMENSION_BOTON_BORRAR_MOVIMIENTO_X
        yi, yf = DIMENSION_BOTON_BORRAR_MOVIMIENTO_Y
        if xi < x < xf and yi < y < yf and pokemon_actual != None:
            equipos = borrar_movimiento(objeto_equipo, equipos)

        xi, xf = DIMENSION_BOTON_AGREGAR_POKEMON_X
        yi, yf = DIMENSION_BOTON_AGREGAR_POKEMON_Y
        if xi < x < xf and yi < y < yf:
            equipos = agregar_pokemon_a_equipo(objeto_equipo, equipos, diccionario_pokemons, lista_nombres_pokemones)
            objeto_equipo.avanzar_pokemon_actual()

        xi, xf = DIMENSION_BOTON_BORRAR_POKEMON_X
        yi, yf = DIMENSION_BOTON_BORRAR_POKEMON_Y
        if xi < x < xf and yi < y < yf and pokemon_actual:
            if verificador_de_accion(mensajes.MENSAJE_VERIFICACION_BORRAR_POKEMON_ACTUAL):
                pokemon_a_eliminar = objeto_equipo.obtener_pokemon_actual()
                objeto_equipo.avanzar_pokemon_actual()
                objeto_equipo.eliminar_pokemon(pokemon_a_eliminar)
        
        xc, yc, radio = ctes.DIMENSION_OVALO_ANTERIOR_VENTANA
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            ventana_actual = ctes.VENTANA_VISTA_EQUIPOS

        xc, yc, radio = ctes.DIMENSION_OVALO_ANTERIOR
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            equipos = retroceder_a_anterior_pokemon(objeto_equipo, equipos)

        xc, yc, radio = ctes.DIMENSION_OVALO_SIGUIENTE
        if esta_dentro_circuferencia(x, y, xc, yc, radio):
            equipos = avanzar_a_siguiente_pokemon(objeto_equipo, equipos)

    return ventana_actual, equipos
