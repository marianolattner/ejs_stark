import re
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe : str) -> str: 
    """_summary_
    extrae las iniciales del heroe que se le pase y las une con un punto
    Args:
        nombre_heroe (str): recibe el nombre de un heroe en formato string

    Returns:
        str: devuelve el resultado de la extraccion
    """
    if nombre_heroe == "":
        resultado = "N/A"
    else:
        nombre_heroe = re.sub("-", " ", nombre_heroe)
        palabras = re.split(" ", nombre_heroe)
        iniciales = []

        for palabra in palabras:
            if palabra == "the":
                continue
            inicial = palabra[0].upper()
            iniciales.append(inicial)

        resultado = '.'.join(iniciales) + "."
        return resultado


def obtener_dato_formato(dato :str) -> str :
    """_summary_
    pasa todo el dato a minuscula y cambia los espaciones por guiones bajos si los tiene

    Args:
        dato (str): recibe el dato que quiere cambiarle el formato

    Returns:
        str: devuelve el resultado de lo hecho
    """
    if type(dato) != str :
        resultado =  False
    else :
        dato = dato.lower()
        resultado = re.sub(" ", "_", dato)
        return resultado


def stark_imprimir_nombre_con_iniciales(dic : dict) : 
    """_summary_
    imprime el nombre del heroe junto a sus iniciales

    Args:
        dic (dict): diccionario de un heroe

    Returns:
        str: devuelve el nombre del heroe con sus iniciales
    """
    if type(dic) == dict and "nombre" in dic.keys() : 
        print(f"* {dic['nombre']} ({extraer_iniciales(dic['nombre'])})")
        retorno = True
    else:
        retorno = False
    return retorno


def stark_imprimir_nombres_con_iniciales(lista_heroes : list) :
    """_summary_
    imprime el nombre de todos los heroes junto a sus iniciales

    Args:
        lista_heroes (list): lista de diccionario con todos los heroes 
    Returns:
        bool: retorna true si se pudo realizar la funcion y false en caso contrario
    """
    if len(lista_heroes) != 0 and type(lista_heroes) == list :
        for personaje in lista_heroes :
            stark_imprimir_nombre_con_iniciales(personaje)
        retorno = True
    else :
        retorno = False
    return retorno


def generar_codigo_heroe(dic, id):
    """_summary_
    genera un codigo de heroe segun su genero y el id que se le pasa

    Args:
        dic (dict): diccionario de un heroe
        id (int): numero que identifica al heroe

    Returns:
        _type_: devuelve el codigo generado
    """
    if (dic["genero"] != "M" and dic["genero"] != "F" and dic["genero"] != "NB")  or (dic["genero"] == "") :
        return "N/A"
    else:
        if dic["genero"] == "M":
            primer_numero = 1
        elif dic["genero"] == "F":
            primer_numero = 2
        else:
            primer_numero = 0
        
        id_str = str(id).zfill(7)
        
        codigo = f"{dic['genero']}-{primer_numero}{id_str}"
        return codigo


def extraer_nombre_con_iniciales(dic : dict) :
    """_summary_
    extra el nombre con las iniciales unicamente

    Args:
        dic (dict): diccionario con los datos de un heroe
    """
    return(f"* {dic['nombre']} ({extraer_iniciales(dic['nombre'])})")      

def stark_generar_codigos_heroes (lista_heroes : list) :
    """_summary_
    genera codigos para todos los heroes de la lista

    Args:
        lista_heroes (list): lista de diccionario con los heroes

    Returns:
        _type_: retorna los codigos
    """
    codigos = []
    id = 1
    for heroe in lista_heroes :
        if len(lista_heroes) != 0 and type(heroe) == dict :
            codigo = generar_codigo_heroe(heroe,id)
            nombre_con_iniciales = extraer_nombre_con_iniciales(heroe)
            impresion = f"{nombre_con_iniciales} | {codigo}"
            id += 1
            codigos.append(impresion)
        else :
            retorno = False
    for codigo in codigos :
        retorno = "\n".join(codigos)

    return retorno


def sanitizar_entero(numero_str: str):
    """_summary_
    sanitiza un numero entero

    Args:
        numero_str (str): recibe un string

    Returns:
        str: en caso de contener caracteres no numericos retornara un -1, en caso de que sea un numero negativo un -2 ,en caso de que suceda otro error un -3 y en caso de que no suceda ningun error y sea un numero positivo retornara el numero convertido a entero
    """
    numero_str = numero_str.strip()
    retorno = "-3"
    if re.match(r"^-?\d+$", numero_str):
        if re.match(r"^-", numero_str):
            retorno = "-2"
        else:
            retorno = int(numero_str)
    else:
        retorno = "-1"
    return retorno


def sanitizar_flotante(numero_str : str) :
    """_summary_
    sanitiza un flotante

    Args:
        numero_str (str): recibe un string 

    Returns:
        _type_: si contiene caracteres no numericos retornara un -1, en el caso en que sea un numero negativo retornara un -2, si ocurren otros errores que no permiten convertirlo a entero debera retornar un -3  y en caso de que sea un numero flotante positivo se retornara el mismo convertido a flotante
    """
    numero_str = numero_str.strip()
    retorno = "-3"
    if re.match(r"[0-9]+\.[0-9]+", numero_str):
        if re.match(r"^-", numero_str) :
            retorno = "-2"
        else :
            retorno = float(numero_str)
    else :
        retorno = "-1"
    return retorno
        

# 3.3. Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
# ● valor_str: un string que representa el texto a validar
# ● valor_por_defecto: un string que representa un valor por defecto
# (parámetro opcional, inicializarlo con ‘-’)
# La función deberá analizar el string recibido y determinar si es solo texto (sin
# números). En caso de encontrarse números retornar “N/A”
# En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un
# espacio
# El espacio es un caracter válido
# En caso que se verifique que el parámetro recibido es solo texto, se deberá
# retornar el mismo convertido todo a minúsculas
# En el caso que el texto a validar se encuentre vacío y que nos hayan pasado
# un valor por defecto, entonces retornar el valor por defecto convertido a
# minúsculas
# Quitar los espacios en blanco de atras y adelante de ambos parámetros en
# caso que los tuviese

def sanitizar_string(valor_str, valor_por_defecto='-'):
    """_summary_
    sanitiza un string, es decir, lo pasa todo a minusculas y valida que sea solamente un string

    Args:
        valor_str (_type_): representa el texto a validar
        valor_por_defecto (str, optional): _description_. Defaults to '-'.

    Returns:
        _type_: devuelve el string sanitizado y si no se pudo sanitizar retorna N/A
    """
    valor_str = re.sub(r"^\s+|\s+$", "", valor_str)
    valor_por_defecto = re.sub(r"^\s+|\s+$", "", valor_por_defecto)
    
    if re.match(r"^[A-Za-z\s]*$", valor_str):
        valor_str = re.sub(r"/", " ", valor_str)
        retorno = valor_str.lower()
    elif valor_str == '' and valor_por_defecto:
        return valor_por_defecto.lower()
    else :
        retorno = "N/A"
    
    return retorno


def sanitizar_dato(heroe : dict , clave : str , tipo_dato : str) :
    """_summary_
    sanitiza cualquier tipo de dato

    Args:
        heroe (dict): diccionario de heroe
        clave (str): clave que quiere sanitizarse
        tipo_dato (str): puede ser string, entero o flotante

    Returns:
        bool: devuelve true si se pudo sanitizar y false si no se pudo
    """
    tipo_dato = tipo_dato.lower()
    
    if (tipo_dato == "entero" or tipo_dato == "flotante" or tipo_dato == "string") :
        if clave  in heroe.keys() :
            if tipo_dato == "entero" :
                heroe[clave] = sanitizar_entero(heroe[clave])
            elif tipo_dato == "flotante" :
                heroe[clave] = sanitizar_flotante(heroe[clave])
            elif tipo_dato == "string" :
                heroe[clave] = sanitizar_string(heroe[clave])
            retorno = True
        else :
            print("La clave especificada no existe en el héroe")
            retorno = False
    else :
        print("Tipo de dato no reconocido")
        retorno = False
    return retorno


def stark_normalizar_datos(lista_heroes: list):
    """_summary_
    normaliza todos los datos

    Args:
        lista_heroes (list): lista de diccionario
    """
    if len(lista_heroes) != 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe, "altura", "flotante")
            sanitizar_dato(heroe, "peso", "flotante")
            sanitizar_dato(heroe, "color_ojos", "string")
            sanitizar_dato(heroe, "color_pelo", "string")
            sanitizar_dato(heroe, "fuerza", "entero")
            sanitizar_dato(heroe, "inteligencia", "string")
        print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía")



def stark_imprimir_indice_nombre(lista_heroes: list):
    """_summary_
    La función muestra por pantalla cada una de las palabras de cada uno
    de los nombres que existan en el data_stark separado por un guion entre
    cada una de las palabras ignorando las palabras que digan “the”

    Args:
        lista_heroes (list): lista de diccionario
    """
    nombres = []
    for heroe in lista_heroes:
        nombre = heroe["nombre"]
        palabras = re.split(" ", nombre)
        for palabra in palabras:
            if palabra != "the": 
                nombres.append(palabra)
    
    resultado = "-".join(nombres) 
    print(resultado)
        


def generar_separador (patron : str , largo : int , imprimir = True ) :
    """_summary_
    genera un separador con el patron y el largo especificado dando la opcion de imprimir o no(imprime por defecto)

    Args:
        patron (str): el patron que se va a usar de separador
        largo (int): la cantidad de veces que quiere que se repita el patron
        imprimir (bool, optional):  Defaults to True. si esta en true imprime el separador y sino no

    Returns:
        str: devuelve el separador generado
    """
    if (len(patron) > 0 and len(patron) < 3) and (type(largo) == int) and (largo > 0 and largo < 236) :
        retorno = patron * largo
        if imprimir :
            print(retorno)
    else :
        retorno = "N/A"
    return retorno


def generar_encabezado(titulo : str) :
    """_summary_
    genera un encabezado

    Args:
        titulo (str): el encabezado que se quiere generar

    Returns:
        _type_: devuelve el encabezado con los separadores y el titulo
    """
    titulo = titulo.upper()
    separador = generar_separador("*", 149, False)
    encabezado = f"{separador}\n{titulo}\n{separador}"
    return encabezado


def imprimir_ficha_heroe(heroe : dict) : 
    """_summary_
    imprime la ficha del heroe con los encabezados necesarios

    Args:
        heroe (dict): diccionario del heroe
    """
    indice = lista_personajes.index(heroe) 
    encabezado_principal = (generar_encabezado("principal"))
    nombre = heroe["nombre"]
    identidad_secreta = heroe["identidad"]
    consultora = heroe["empresa"]
    codigo = generar_codigo_heroe(heroe,indice + 1) 

    principal = f"NOMBRE DEL HÉROE: {obtener_dato_formato(nombre)}({extraer_iniciales(nombre)}) \nIDENTIDAD SECRETA: {obtener_dato_formato(identidad_secreta)} \nCONSULTORA: {obtener_dato_formato(consultora)} \nCÓDIGO DE HEROE: {codigo}"

    encabezado_fisico = generar_encabezado("FISICO")
    fisico = f"ALTURA: {heroe['altura']} \nPESO: {heroe['peso']} \nFUERZA: {heroe['fuerza']} N"

    encabezado_señas_particulares = generar_encabezado("SEÑAS PARTICULARES")
    señas_particulares = f"COLOR DE OJOS: {heroe['color_ojos']} \nCOLOR DE PELO: {heroe['color_pelo']}"

    mensaje = f"{encabezado_principal}\n"
    mensaje += f"{principal}\n"
    mensaje += f"{encabezado_fisico}\n"
    mensaje += f"{fisico}\n"
    mensaje += f"{encabezado_señas_particulares}\n"
    mensaje += f"{señas_particulares}\n"
    print(mensaje)


def stark_navegar_fichas(lista_heroes : list) :
    """_summary_
    permite navegar en todas las fichas de los heroes

    Args:
        lista_heroes (list): lista de diccionarios
    """
    posicion = 0
    imprimir_ficha_heroe(lista_heroes[posicion])
    while True :
        numero_seleccionado = input("1- Ir a la izquierda \n2- Ir a la derecha \n3-Salir\n")
        match numero_seleccionado :
            case "1" :
                if posicion == 0 :
                    posicion = len(lista_heroes) - 1
                    
                else :
                    posicion -= 1
                imprimir_ficha_heroe(lista_heroes[posicion])
            case "2" :
                if posicion == len(lista_heroes) - 1 :
                    posicion = 0
                else :
                    posicion += 1
                imprimir_ficha_heroe(lista_heroes[posicion])
            case "3" : 
                break
            case default :
                numero_seleccionado = input(" 1- Ir a la izquierda \n2- Ir a la derecha \n3-Salir\n")


def imprimir_menu () :
    """_summary_
    imprime las opciones del menu
    """
    print("1-Imprimir la lista de nombres junto con sus iniciales \n2-Imprimir la lista de nombres y el código del mismo \n3-Normalizar datos\n4-Imprimir índice de nombres \n5-Navegar fichas \n6-Salir \n")

def menu_principal() :
    """_summary_
    imprime las opciones de menu y deja elegir una opcion

    Returns:
        int: devuelve la opcion elegida
    """
    imprimir_menu()
    opcion = input("elija una opcion (1/2/3/4/5/6)\n")
    return opcion

def ejecutar_menu_principal(lista_heroes : list) :
    """_summary_
    ejecuta el menu principal

    Args:
        lista_heroes (list): lista de diccionario
    """
    bandera_normalizado = False
    while True :
        opcion = menu_principal()
        match opcion :
            case "1" :
                if bandera_normalizado :
                    stark_imprimir_nombres_con_iniciales(lista_heroes)
                else :
                    print("datos no normalizados, por favor normalicelos")
            case "2" :
                if bandera_normalizado :
                    print(stark_generar_codigos_heroes(lista_heroes))
                else :
                    print("datos no normalizados, por favor normalicelos")
            case "3" :
                try :
                    stark_normalizar_datos(lista_heroes)
                    bandera_normalizado = True
                except AttributeError :
                    print("datos ya normalizados")
            case "4" :
                if bandera_normalizado :
                    stark_imprimir_indice_nombre(lista_heroes)
                else :
                    print("datos no normalizados, por favor normalicelos")
            case "5" :
                if bandera_normalizado :
                    stark_navegar_fichas(lista_heroes)
                else :
                    print("datos no normalizados, por favor normalicelos")
            case "6" :
                break
            case default :
                print("numero no valido, elija otro")