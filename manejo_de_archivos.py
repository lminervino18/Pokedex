import csv
from Equipo import Equipo_pk

ENCABEZADO_ARCHIVO_EQUIPOS = 'nombre;pokemon,movimientos;pokemon,movimientos;pokemon,movimientos\n'
DELIMITADOR_ARCHIVOS_CSV = ';'
DELIMITADOR_TIPOS = ','
DELIMITADOR_MOVIMIENTOS = ','


def cargar_pokemones(archivo_pokemons, archivo_movimientos):
    '''Recibe el archivo con la informacion de los pokemones y el archivo con sus movimientos
    Abre el archivo, lo lee y retrona una lista con los nombres y un diccionario con sus caracteristicas'''
    diccionario_pokemons = {}
    lista_nombres_pokemones = []
    with open(archivo_pokemons) as fpk:
        fpk_csv = csv.reader(fpk, delimiter = DELIMITADOR_ARCHIVOS_CSV)
        num_e, img_e, _, tip_e, hp_e, atk_e, defs_e, spa_e, spd_e, spe_e = next(fpk_csv)
        for num, img, nom, tip, hp, atk, defs, spa, spd, spe in fpk_csv:
            lista_nombres_pokemones.append(nom)
            diccionario_pokemons[nom] = {num_e: num, img_e: img, tip_e: tip.split(DELIMITADOR_TIPOS), hp_e: hp, atk_e: atk, defs_e: defs, spa_e: spa, spd_e: spd, spe_e: spe}
    with open(archivo_movimientos) as mov:
        mov_csv = csv.reader(mov, delimiter = DELIMITADOR_ARCHIVOS_CSV)
        nom, mov = next(mov_csv)
        for nombre, movimientos in mov_csv:
            if diccionario_pokemons.get(nombre, None):
                diccionario_pokemons[nombre][mov] = movimientos.split(DELIMITADOR_MOVIMIENTOS)
    return lista_nombres_pokemones, diccionario_pokemons

def guardar_datos_equipos(archivo, equipos):
    '''Recibe un archivo destino y la lista con los equipos.
    Crea o modifica el archivo con la informacion de cada equipo en la lista de equipos'''
    with open(archivo, 'w') as w:
        w.write(ENCABEZADO_ARCHIVO_EQUIPOS)
        for equipo in equipos:
            linea = equipo.obtener_nombre()
            if equipo.cantidad_pokemones() != 0:
                linea += f'{DELIMITADOR_ARCHIVOS_CSV}'
            for indice, nombre_pokemon in enumerate(equipo.obtener_pokemons()):
                movimientos = equipo.obtener_movimientos(nombre_pokemon)
                linea += f'{nombre_pokemon}{DELIMITADOR_MOVIMIENTOS}{",".join(movimientos)}'
                if indice != len(equipo.obtener_pokemons()) - 1:
                    linea += DELIMITADOR_ARCHIVOS_CSV
            w.write(f'{linea}\n')
                   
def cargar_equipos(archivo):
    '''Recibe el archivo origen con la informacion de los equipos guardados y retorna una lista
    con los equipos y el equipo actual. Si el archivo no existe retorna una lista de equipos vacia y 
    el equipo actual sin valor'''
    lista_equipos = []
    try:
        with open(archivo) as f:
            csv_reader = csv.reader(f, delimiter = DELIMITADOR_ARCHIVOS_CSV)
            next(csv_reader)
            for equipo in csv_reader:
                if len(equipo) == 0:
                    continue
                equipo_nuevo = Equipo_pk(equipo[0])
                for pokemon in equipo[1:]:
                    pokemon = list(pokemon.split(DELIMITADOR_MOVIMIENTOS))
                    nombre_pokemon = pokemon[0]
                    equipo_nuevo.agregar_pokemon(nombre_pokemon, pokemon[1])
                    for movimiento in pokemon[2:]:
                        equipo_nuevo.agregar_movimiento(nombre_pokemon, movimiento)
                equipo_nuevo.avanzar_pokemon_actual()
                lista_equipos.append(equipo_nuevo)
        if len(lista_equipos) == 0:
            equipo_actual = None
        else:
            equipo_actual = 0
        return lista_equipos, equipo_actual
        
    except:
        equipo_actual = None
        return lista_equipos, equipo_actual   
    