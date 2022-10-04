from validaciones import *
import json

def cargar_json(nombre_archivo:str):
    lista = []
    if(es_valido_archivo(nombre_archivo)):
        with open(nombre_archivo, 'r') as archivo:
            lista = json.load(archivo)['results']
    return lista

def guardar_archivo(lista:list, nombre_archivo:str):
    if(es_valido_archivo(nombre_archivo)):
        mensaje = ''
        with open(nombre_archivo, 'w') as archivo:
            for item in lista:
                for key in item:
                    mensaje += ' {0}: {1} | '.format(key.capitalize(), item[key])
                mensaje += '\n'
                archivo.writelines(mensaje)
                mensaje = ''
                
def normalizar_lista(lista:list):
    if(es_lista_valida(lista)):
        for item in lista:
            item["height"] = int(item["height"])
            item["mass"] = int(item["mass"])
            
def buscar_max(lista:list, key:str):
    retorno = -1
    
    if(es_lista_valida(lista)):
        index = 0
        for i in range(len(lista)):
            if(lista[i][key] > lista[index][key]):
                index = i
        retorno = index
        
    return retorno

def ordenar_lista_por_key(lista:list, key:str):
    lista_copia = lista.copy()
    lista_ordenada = []
    while(len(lista_copia) > 0):
        index = buscar_max(lista_copia, key)
        lista_ordenada.append(lista_copia.pop(index))
    
    return lista_ordenada

def mostrar_lista(lista:list):
    if(es_lista_valida(lista)):
        mensaje = ''
        for item in lista:
            for key in item:
                mensaje += ' {0}: {1} | '.format(key.capitalize(), item[key])
            mensaje += '\n'
        print(mensaje)

def mostrar_mas_alto_cada_genero(lista:list):
    if(es_lista_valida(lista)):
        lista_ordenada_por_altura = ordenar_lista_por_key(lista, 'height')
        
        mas_alto_M =  buscar_mas_alto_por_genero(lista_ordenada_por_altura, 'male')
        mas_alto_F =  buscar_mas_alto_por_genero(lista_ordenada_por_altura, 'female')
        mas_alto_N_A =  buscar_mas_alto_por_genero(lista_ordenada_por_altura, 'n/a')
        
        print('El masculino mas alto es: {0}, el femenino mas alto es: {1}, el sin genero mas alto es: {2}\n'. format(mas_alto_M, mas_alto_F, mas_alto_N_A))
          
def buscar_mas_alto_por_genero(lista_ordenada:list, genero:str):
    retorno = ''
    if(es_lista_valida(lista_ordenada)):
        for item in lista_ordenada:
            if(item['gender'] == genero):
                retorno = item['name']
                break
        
    return retorno

def devolver_lista_nombres(lista:list):
    lista_nombres = []
    if(es_lista_valida(lista)):
        for item in lista:
            lista_nombres.append(item['name'])
    return lista_nombres

def pedir_nombre_del_personaje():
    return input('Por favor ingrese el personaje que desea buscar: ')

def devolver_personaje(nombre:str, lista:list):
    for item in lista:
        if(item['name'] == nombre):
            return item
    
def mostrar_personaje(personaje:dict):
    for key in personaje:
        print('\t{0}: {1}'.format(key.capitalize(), personaje[key]))
    print('\n')

def buscar_personaje(lista:list):
    if(es_lista_valida(lista)):
        nombre_personaje = pedir_nombre_del_personaje()
        while(not(existe_personaje(nombre_personaje, devolver_lista_nombres(lista)))):
            print('\t--------ERROR: Personaje ingresado no valido-------\n')
            nombre_personaje = pedir_nombre_del_personaje()
            
    personaje = devolver_personaje(nombre_personaje, lista)
    mostrar_personaje(personaje)