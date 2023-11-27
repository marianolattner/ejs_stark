from data_stark import *
import json

def leer_archivo(nombre_archivo: str):
    """_summary_
    abre un archivo y lo lee
    Args:
        nombre_archivo (str): nombre y extensión del archivo a leer

    Returns:
        _type_: si se pudo leer el archivo devuelve un string con la informacion del mismo y si no devuelve false
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            retorno = archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        retorno = False
    return retorno


def guardar_archivo(nombre_archivo: str, contenido_a_guardar: str):
    """_summary_
    crea el archivo con el nombre pasado por parametro y con el contenido pasado por parametro en caso de que no exista y en caso de existir lo sobreescribe
    Args:
        nombre_archivo (str): nombre con el cual se guardará el archivo junto con su extensión
        contenido_a_guardar (str): contenido a guardar en dicho archivo

    Returns:
        bool: retornara true si no hubo errores y false en el caso contrario
    """
    try:
        with open(nombre_archivo, "w+", encoding="utf-8") as archivo:
            archivo.write(contenido_a_guardar)
            print(f"Se creó el archivo: {nombre_archivo}")
            retorno = True
    except Exception as e :
        print(f"Error al crear el archivo: {nombre_archivo}")
        retorno = False
    return retorno


def generar_csv(nombre_archivo: str, lista: list):
    """_summary_
    guarda en un string la información en formato csv con la cabecera correspondiente.
    Args:
        nombre_archivo (str): nombre y extension del archivo csv de los superheroes(ruta absoluta o relativa)
        lista (list): _description_

    Returns:
        _type_: _description_
    """
    if len(lista) == 0:
        retorno = False
    else:
        str = ""
        dict_1 = lista[0]
        indice = len(dict_1) - 1
        i = 0
        for llave in dict_1:
            if i != indice:
                str += f"{llave},"
            else:
                str += llave
            i += 1
        for dict in lista:
            i = 0
            str +="\n"
            for llave in dict_1:
                if i != indice:
                    str += f"{dict[llave]},"
                else:
                    str += dict[llave]
                i += 1
        guardar_archivo(nombre_archivo, str)
        retorno = True
    return retorno


def leer_csv(nombre_archivo: str):
    """_summary_
    genera una lista de superhéroes en base al contenido de ese archivo csv que se le paso
    Args:
        nombre_archivo (str): nombre y extensión de donde se ubica el archivo a leer (Ruta absoluta o relativa)

    Returns:
        _type_: retorna la lista de diccionarios si es que existe elarchivo y sino retorna False.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lista_lineas = archivo.readlines()
    except Exception:
        retorno = False
    lista_stripeada = []
    for linea in lista_lineas:
        lista_stripeada.append(linea.strip())
    lista_retorno = []
    lista_llaves = lista_stripeada[0].split(",")
    primera_linea = True
    for linea in lista_stripeada:
        if not primera_linea:
            dict = {}
            lista_esta_linea = linea.split(",")
            i = 0
            for llave in lista_llaves:
                dict[llave] = lista_esta_linea[i]
                i += 1
            lista_retorno.append(dict)
        primera_linea = False
    retorno = lista_retorno
    return retorno
    
    


def generar_json(nombre_archivo: str, lista: list, nombre_lista: str):
    """_summary_
    guarda en un diccionario de una sóla clave la lista de superhéroes
    Args:
        nombre_archivo (str): nombre y extensión de donde se ubica el archivo a guardar (Ruta absoluta o relativa)
        lista (list): lista de diccionario de superheroes
        nombre_lista (str): nombre de la lista que sera la clave del json
    """
    if len(lista) != 0:
        dict = {nombre_lista: lista}
        with open(nombre_archivo, "w+", encoding="utf-8") as archivo:
            json.dump(dict, archivo, indent=4, ensure_ascii=False)


def leer_json(nombre_archivo, nombre_lista):
    """_summary_

    Args:
        nombre_archivo (str): nombre y extensión de donde se ubica el archivo a leer (Ruta absoluta o relativa)
        nombre_lista (str): nombre de la lista a leer

    Returns:
        _type_: Si el archivo existe lee el archivo json y retorna la lista obtenida. Si el achivo no existe retorna False
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = json.load(archivo)
            if nombre_lista in contenido:
                retorno =  contenido
            else:
                print(f"La lista con el nombre '{nombre_lista}' no se encuentra en el archivo.")
                retorno =  False
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        retorno =  False
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON")
        retorno = False
    return retorno


def ordenar_heroes_ascendente(heroes: list, clave: str):
    """_summary_
    ordena los heroes por altura, peso o fuerza de manera ascendente

    Args:
        heroes (list): lista de diccionario de los heroes
        clave (str): clave por la cual se quiere ordenar

    Returns:
        list: devuelve la lista de diccionario ordenada 
    """
    if clave not in ['altura', 'peso', 'fuerza']:
        print("Clave no válida. Las claves válidas son 'altura', 'peso' y 'fuerza'.")


    for i in range(len(heroes) - 1):
        for j in range(i + 1, len(heroes)):
            if float(heroes[i][clave]) > float(heroes[j][clave]):
                aux = heroes[i]
                heroes[i] = heroes[j]
                heroes[j] = aux                
    return heroes


def ordenar_heroes_descendente(heroes: list, clave: str):
    """_summary_
    ordena los heroes por altura, peso o fuerza de manera descendente

    Args:
        heroes (list): lista de diccionario con los heroes
        clave (str): clave por la cual se quiere ordenar

    Returns:
        list: devuelve la lista de diccionario ordenada
    """
    if clave not in ['altura', 'peso', 'fuerza']:
        print("Clave no válida. Las claves válidas son 'altura', 'peso' y 'fuerza'.")


    for i in range(len(heroes) - 1):
        for j in range(i + 1, len(heroes)):
            if float(heroes[i][clave]) < float(heroes[j][clave]):
                aux = heroes[i]
                heroes[i] = heroes[j]
                heroes[j] = aux
                
    return heroes


def ordenar_segun_parametro_asc_o_desc(heroes: list, clave: str, asc_o_desc: str):
    """_summary_
    ordena los heroes por altura, peso o fuerza de la manera que el usuario elija ( ascendente o descendente)

    Args:
        heroes (list): lista de diccionarios con los heroes
        clave (str): clave por la cual se quiere ordenar
        asc_o_desc (str): eleccion de ordenamiento ascendente o descendente

    Returns:
        list: devuelve la lista de diccionario ordenada
    """
    if asc_o_desc != "asc" and asc_o_desc != "desc" :
        print("valor no valido, ingrese 'asc' o 'desc'")
    else:
        if asc_o_desc == "asc":
            ordenar_heroes_ascendente(heroes, clave)
        else:
            ordenar_heroes_descendente(heroes, clave)
    return heroes


def stark_normalizar_datos(lista : list)-> bool :
    """ recibe la lista (de personajes en este caso) y la normaliza para poder trabajar con el tipo de dato que necesitamos
    

    Args:
        lista (list): recibe una lista de personajes

    Returns:
        bool: si se modifico la lista retorna true y sino false
    """
    bandera_cambios = True
    if len(lista) != 0 :
        for personaje in lista :
            if  type(personaje["fuerza"]) != int :
                personaje["fuerza"] = int(personaje["fuerza"])
                bandera_cambios = False
            elif personaje["fuerza"] == "" :
                bandera_cambios = True
            if  type(personaje["altura"]) != float :
                personaje["altura"] = float(personaje["altura"])
                bandera_cambios = False
            elif personaje["altura"] == "" :
                bandera_cambios = True
            if  type(personaje["peso"]) != float :
                personaje["peso"] = float(personaje["peso"])
                bandera_cambios = False
            elif personaje["peso"] == "" :
                bandera_cambios = True
            personaje["color_pelo"] = personaje["color_pelo"].lower()
            personaje["color_ojos"] = personaje["color_ojos"].lower()
    if bandera_cambios :
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")   
        retorno = True
    else:
        print("Datos Normalizados")
        retorno = False
    return retorno

def imprimir_menu() :
    """la funcion imprime el menu
    """
    print("1-Normalizar datos \n2-Generar CSV \n3-Listar heroes del archivo CSV ordenados por altura ASC \n4-Generar JSON \n5-Listar heroes del archivo JSON ordenados por peso DESC \n6-Ordenar Lista por fuerza \n7-Salir")
    
def stark_menu_principal() :
    """la funcion imprime el menu y le permite al usuario elejir una opcion y castearla a entero

    Returns:
        _type_: si la opcion no es valida segun la funcion validar_entero retorna un false y si es valida retorna la opcion
    """
    imprimir_menu()
    opcion = int(input("elija una opcion (1/2/3/4/5/6/7)"))
    return opcion


def stark_imprimir_heroes (lista : list) :
    """ la funcion imprime una lista mientras que no este vacia

    Args:
        lista (list): recibe una lista de personajes

    Returns:
        _type_: en caso de que la lista este vacia retorna false, si no esta vacia devuelve una tabla impresa con todos los personajes de la lista y sus caracteristicas
    """
    if lista == [] :
        return False
    else :
        print("Nombre             | Identidad                     | Empresa       | Altura | Peso   | Genero| Color de ojos           | Color de pelo | Fuerza  | Inteligencia" )
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for personaje in lista:
                print(f"{personaje['nombre']:18} | {personaje['identidad']:29} | {personaje['empresa']:6} | {personaje['altura']:6} | {personaje['peso']:6} | {personaje['genero']:5} | {personaje['color_ojos']:23} | {personaje['color_pelo']:13} | {personaje['fuerza']:7} | {personaje['inteligencia']:4}")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def stark_marvel_app(lista : list ):
    """la funcion se encarga de la ejecucion principal del programa

    Args:
        lista (list): recibe la lista de personajes
    """
    bandera_data_normalizada = False 
    while True :    
        opcion = stark_menu_principal()
        match opcion :
            case 1 : 
                stark_normalizar_datos(lista)
                bandera_data_normalizada = True
            case 2 :
                    if bandera_data_normalizada:
                        archivo_csv = generar_csv("archivo_csv.csv", lista)
                    else:
                        print("datos no normalizados")
            case 3 :
                    if bandera_data_normalizada:
                        lista_csv = leer_csv("archivo_csv.csv")
                        stark_imprimir_heroes(ordenar_heroes_ascendente(lista_csv, "altura")) 
                    else:
                        print("datos no normalizados")
            case 4 :
                    if bandera_data_normalizada:
                        archivo_json = generar_json("archivo_json.json", lista, "heroes")
                    else:
                        print("datos no normalizados")
            case 5 :
                    if bandera_data_normalizada:    
                        dict_json = leer_json("archivo_json.json", "heroes")
                        lista_json = dict_json["heroes"]
                        stark_imprimir_heroes(ordenar_heroes_descendente(lista_json, "peso"))
                    else:
                        print("datos no normalizados")
            case 6 :
                    if bandera_data_normalizada:
                        eleccion = input("quiere ordenar de forma ascendente o descendente (asc o desc) ")
                        stark_imprimir_heroes(ordenar_segun_parametro_asc_o_desc(lista, "fuerza", eleccion))
                    else:
                        print("datos no normalizados")
            case 7 :
                    break 
            case default:
                print("opcion ingresada no valida, por favor ingrese un numero valido")