'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''
from funciones import *

def starwars_app():
    lista_personajes = cargar_json('./data.json')
    normalizar_lista(lista_personajes)
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        while(not(es_valida_opcion_menu_ingresada(respuesta))):
            print('\t--------ERROR: Opcion ingresada no valida-------\n')
            print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
            respuesta = input()
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")
            lista_personajes = ordenar_lista_por_key(lista_personajes, 'height')
            mostrar_lista(lista_personajes)
        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")
            mostrar_mas_alto_cada_genero(lista_personajes)
        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")
            lista_personajes = ordenar_lista_por_key(lista_personajes, 'mass')
            mostrar_lista(lista_personajes)
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")
            buscar_personaje(lista_personajes)
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
            guardar_archivo(lista_personajes, 'data.csv')
        elif(respuesta=="6"):
            break


starwars_app()

