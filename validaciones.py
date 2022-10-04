import re

def es_valido_archivo(nombre_archivo:str):
    return (re.search('.json$|.csv$', nombre_archivo) != None)

def es_lista_valida(lista:list):
    return ((type(lista) == type(list())) and  (len(lista) > 0))

def es_valida_opcion_menu_ingresada(respuesta:str):
    return (re.search('^[1-6]$', respuesta) != None)

def existe_personaje(personaje:str, lista_nombres:list):
    existe = False
    
    for nombre in lista_nombres:
        if(nombre == personaje):
            existe = True
            break
        
    return existe
