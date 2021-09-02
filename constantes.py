'''Defino constantes a utilizar'''

# Constantes sobre las ventanas
# Pre = El ancho y alto de la ventana tienen que mantener esa relacion para que funcione
ANCHO_VENTANA = 800
ALTO_VENTANA = ANCHO_VENTANA*0.625
DISTANCIA_ENTRE_OPCIONES_COLOR = ALTO_VENTANA*0.09
VENTANA_INICIAL = 'VENTANA INICIAL'
VENTANA_VISTA_POKEMONS = 'VENTANA VISTA POKEMONES'
VENTANA_VISTA_EQUIPOS = 'VENTANA VISTA EQUIPOS'
VENTANA_EQUIPO_ACTUAL = 'VENTANA VISTA EQUIPO ACTUAL'
VENTANA_COLORES = 'VENTANA VISTA COLORES'
SALIR = 'SALIR DE LA POKEDEX'

# Constantes sobre los colores
COLOR_ROSA = 'pink'
COLOR_ROJO = '#d12013'
COLOR_CELESTE = '#5dc9c2'
COLOR_NEGRO_SUAVE = '#1c1f1e'
COLOR_AZUL = '#2c41e6'
COLOR_AMARILLO = '#ebe534'
COLOR_BLANCO = 'white'
COLOR_VERDE = '#13c902'
COLOR_VERDE_OSCURO = '#0b8500'
COLOR_NARANAJA = '#ff8d03'
COLOR_VERDE_CLARO = '#a0f25c'
COLOR_NEGRO = 'black'
COLOR_GRIS = 'grey'
BARRA = '/'

# Constantes sobre el texto a dibujar
FUENTE = 'MS Gothic'
SALTO_DE_LINEA = '\n'
TEXTO_HP = 'Hp: '
TEXTO_ATK = 'Atk: '
TEXTO_DEF = 'Def: '
TEXTO_SPA = 'Spa: '
TEXTO_SPD = 'Spd: '
TEXTO_SPE = 'Spe: '
TEXTO_POKEDEX = 'POKEDEX'
SIMBOLO_INFORMACION = '[I]'
TEXTO_POKEMONES = 'POKEMONES'
TEXTO_EQUIPOS = 'EQUIPOS'
TEXTO_INFORMACION_FUNCIONES_TECLAS = """' p ' para ir a  ver los pokemones // ' e ' para ir a  ver los equipos \n ' esc ' para cerrar // 'c' para cambiar el color de tu pokedex """
TEXTO_BUSCAR = 'BUSCAR'
TEXTO_RANDOM = 'RANDOM'
ENCABEZADO_POKEMONES = ['numero','imagen','nombre','tipos','hp','atk','def','spa','spd','spe']
TEXTO_PALABRA_CREAR = 'CREAR'
TEXTO_PALABRA_BORRAR = 'BORRAR'
TEXTO_CREA_TUS_EQUIPOS = '¡Crea equipos con tus pokemons favoritos!'
TEXTO_NOMBRE_EQUIPO = 'NOMBRE EQUIPO'
TEXTO_PRESIONE_ESPACIO = 'PRESIONE ESPACIO PARA VER EQUIPO'
TEXTO_AGREGAR_MOVIMIENTO = 'AGREGAR\nMOVIMIENTO'
TEXTO_BORRAR_POKEMON = 'BORRAR\nPOKEMON'
TEXTO_AGREGAR_POKEMON = 'AGREGAR\nPOKEMON'
TEXTO_BORRAR_MOVIMIENTO = 'BORRAR\nMOVIMIENTO'
TEXTO_EQUIPO_SINGULAR = 'EQUIPO = '
TEXTO_NOMBRE_POKEMON = 'NOMBRE POKEMON'
TEXTO_NO_HAY_POK = 'NO HAY POKEMONES'
TEXTO_MOV = 'MOVIMIENTOS: '
TEXTO_COLORES = 'COLORES'
TEXTO_ELIGE_COLORES = 'Elige una de las opciones(color principal, color secundario, letras)'
TEXTO_OPCION = 'OPCION'
TEXTO_OPCIONES_EN_VENTANA_COLORES = 'Aprete el numero de la opción, o la tecla "Escape" para volver'

#Constantes sobre las combinaciones de colores
COMBINACION_DE_COLORES = ((COLOR_ROJO, COLOR_CELESTE, COLOR_NEGRO_SUAVE), (COLOR_AMARILLO, COLOR_AZUL, COLOR_NEGRO), (COLOR_AZUL, COLOR_BLANCO, COLOR_NEGRO_SUAVE), (COLOR_VERDE, COLOR_VERDE_OSCURO, COLOR_BLANCO), (COLOR_NARANAJA , COLOR_VERDE_CLARO, COLOR_NEGRO), (COLOR_NEGRO, COLOR_GRIS, COLOR_BLANCO))
CANTIDAD_COLORES = len(COMBINACION_DE_COLORES)

#Teclas que utiliza el usuario
TECLA_BORRAR = 'b'
TECLA_BUSCAR = 'b'
TECLA_AGREGAR_POKEMON = 'a'
TECLA_VENTANA_ANTERIOR = 'Escape'
TECLA_SALIR_POKEDEX = 'Escape'
TECLA_VER_EQUIPO_ACTUAL = 'space'
TECLA_SIGUIENTE = 'Right'
TECLA_ANTERIOR = 'Left'
TECLA_POKEMON_RANDOM = 'r'
TECLA_GUARDAR = 'g'
TECLA_AGREGAR_MOV = 'm'
TECLA_BORRAR_MOV = 'n'
TECLA_CREAR_EQUIPO = 'c'
TECLA_VENTANA_COLORES = 'c'
TECLA_VENTANA_POKEMONS = 'p'
TECLA_VENTANA_EQUIPOS = 'e'
TECLAS_NUMEROS_OPCIONES_COLORES = ('1', '2', '3', '4', '5', '6')

#Constantes sobre dimensiones
#Formato 
# RECTANGULO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# RECTANGULO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
# OVALO_X = (COORDENADA_X_INICIO, COORDENADA_X_FINAL)
# OVALO_Y = (COORDENADA_Y_INICIO, COORDENADA_Y_FINAL)
DIMENSION_OVALO_SIGUIENTE_X = (ANCHO_VENTANA*0.85, ANCHO_VENTANA*0.9)
DIMENSION_OVALO_SIG_ANT_Y = (ALTO_VENTANA*0.54, ALTO_VENTANA*0.62)
DIMENSION_OVALO_ANTERIOR_X = (ANCHO_VENTANA*0.1375, ANCHO_VENTANA*0.1875)
DIMENSION_RECTANGULO_INF_DER_X = (ANCHO_VENTANA*0.81375, ANCHO_VENTANA*0.93875)
DIMENSION_RECTANGULO_INF_Y = (ALTO_VENTANA*0.87, ALTO_VENTANA*0.926)
DIMENSION_RECTANGULO_INF_IZQ_X = (ANCHO_VENTANA*0.0625, ANCHO_VENTANA*0.1875)
OVALO_VOLVER_VENTANA_X = (ANCHO_VENTANA*0.015, ANCHO_VENTANA*0.04)
OVALO_VOLVER_VENTANA_Y = (ALTO_VENTANA*0.024, ALTO_VENTANA*0.064)

#FORMATO
#DIMENSION_X = (COORDENAD_X_INICIO, COORDENADA_X_FINAL)
#DIMENSION_Y = (COORDENAD_Y_INICIO, COORDENADA_Y_FINAL)
#DIMENSION_OVALO = (COORDENADA_CENTRO_X, COORDENADA_CENTRO_Y, RADIO)
DIMENSION_OVALO_ANTERIOR_VENTANA = (ANCHO_VENTANA*0.0275, ALTO_VENTANA*0.044, ALTO_VENTANA*0.02)
DIMENSION_OVALO_SIGUIENTE = (ANCHO_VENTANA*0.875, ALTO_VENTANA*0.58, ALTO_VENTANA*0.04) 
DIMENSION_OVALO_ANTERIOR = (ANCHO_VENTANA*0.1625, ALTO_VENTANA*0.58, ALTO_VENTANA*0.04)