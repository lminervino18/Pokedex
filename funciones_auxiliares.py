import gamelib
import mensajes

def verificador_de_accion(cadena):
    '''Recibe una cadena, se la muestra al usuario, le pide una respuesta
    y retorna si esa respuesta es 's' '''
    respuesta = gamelib.input(cadena)
    return respuesta == 's'

def siguiente_indice(actual, maximo):
    '''Recibe un indice y un maximo y avanza al siguiente
    teniendo en cuenta que si llego al maximo, vuelve al principio'''
    return (actual + 1) % maximo

def anterior_indice(actual, maximo):
    '''Recibe un indice y un minimo y retrocede al anterior
    teniendo en cuenta que si llego al principio, va al final'''
    return (actual - 1 + maximo) % maximo

def buscar_pokemon(cadena, valor_por_defecto, lista_nombres_pokemones):
    '''Recibe una cadena que igreso el usuario, un valor por defecto y una lista con los nombres
    de los pokemons, si la cadena es un numero retorna el indice al que hace referencia y si la cadena
    es el nombre del Pokemon retorna el indice correspondiente. Si lo que el usuario ingreso es
    incorrecto retorna el valor por defecto '''
    cantidad_pokemones = len(lista_nombres_pokemones)
    if not cadena:
        return valor_por_defecto
    if cadena.isdigit() and int(cadena) in range(cantidad_pokemones):
        return int(cadena) - 1
    if cadena in lista_nombres_pokemones:
        return lista_nombres_pokemones.index(cadena)
    gamelib.say(mensajes.MENSAJE_DATO_NO_EXISTE)
    return valor_por_defecto

def esta_dentro_circuferencia(x, y, x_centro, y_centro, radio):
    '''Recibe una coordenada coordenada x y una coordenada y y se fija si esta dentro de la 
    circunferencia con centro de coordenadas x_centro e y_centro y de radio pasado por parametro'''
    return (x - x_centro)**2 + (y - y_centro)**2 <= radio**2

def elegir_elemento_lista(lista, string):
	string_opciones = ''
	for indice, elemento in enumerate(lista):
		string += f'{indice+1}: {elemento}\n'
	mensaje = string + '\n' f'Ingrese el numero de la opcion correcta\n{string_opciones}' 
	while True:
		numero_elegido = gamelib.input(mensaje)
		if not numero_elegido:
			return 
		if numero_elegido.isnumeric() and 0 <= int(numero_elegido) - 1 < len(lista):
			break
		gamelib.say('Lo que ingresaste no es correcto, vuelve a intentarlo')
	
	return lista[int(numero_elegido)-1]
