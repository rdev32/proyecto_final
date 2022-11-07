import requests
import os

def generar_info(index: int):
    req = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(index))
    with req as data:
        nombre = data.json()["name"]
        url = data.json()["sprites"]["front_default"]
        lista = []
        
        for v in req.json()["abilities"]:
            lista.append( v["ability"]["name"] )
            
        yield nombre, url, lista

def show_pokemones(lista, int_start = 0, int_max = 20):
    for i in range(int_start, min(int_start + int_max, len(lista))):
        for l1 in generar_info(lista[i]):
            print(f"Nombre: {l1[0]}\nURL: {l1[1]}\nHabilidades:", *l1[2], "\n")


def listar_por_generacion(int_gen: int) -> list:
    req = requests.get("https://pokeapi.co/api/v2/generation/" + str(int_gen))
    with req as data:
        lista = []
        json = data.json()
        for result in json["pokemon_species"]:
            lista.append( result["url"].split("/")[-2] )
        return list(set(lista))

def listar_por_forma(shape_str: str) -> list:
    req = requests.get("https://pokeapi.co/api/v2/pokemon-shape/" + shape_str)
    with req as data:
        lista = []
        json = data.json()

        for result in json["pokemon_species"]:
            lista.append( result["url"].split("/")[-2] )
        return list(set(lista))

def listar_por_habilidad(ability: str) -> list:
    req = requests.get("https://pokeapi.co/api/v2/ability/" + ability)
    with req as data:
        lista = []
        json = data.json()
        for result in json["pokemon"]:
            lista.append( result["pokemon"]["url"].split("/")[-2] )
        return list(set(lista))

def listar_por_habitad(habitat: str) -> list:
    req = requests.get("https://pokeapi.co/api/v2/pokemon-habitat/" + habitat)
    with req as data:
        lista = []
        json = data.json()
        for result in json["pokemon_species"]:
            lista.append( result["url"].split("/")[-2] )
        return list(set(lista))

def listar_por_tipo(tipo: str) -> list:
    req = requests.get("https://pokeapi.co/api/v2/type/" + tipo)
    with req as data:
        lista = []
        json = data.json()
        for result in json["pokemon"]:
            lista.append( result["pokemon"]["url"].split("/")[-2] )
        return list(set(lista))


menu_principal = """
    1. Listar pokemons por generación
    2. Listar pokemons por forma
    3. Listar pokemons por habilidad.
    4. Listar pokemons por habitat
    5. Listar pokemons por tipo
"""

sugerencias = [ "Sugerencias: 1, 2, 3, 4 ...", "Sugerencias: ball, fish, blob, arms ..." , "Sugerencias: stench, static, sturdy, limber ...", "Sugerencias: cave, forest, rare, sea ...", "Sugerencias: normal, water, ice, dark, fire ..." ]

menu_level = 0

def Ejecutar_Listado(menu_level, param, list_start):
    current_list = []
    if (menu_level == 1):
        current_list = listar_por_generacion(int(param))
    elif (menu_level == 2):
        current_list = listar_por_forma(param)
    elif (menu_level == 3):
        current_list = listar_por_habilidad(param)
    elif (menu_level == 4):
        current_list = listar_por_habitad(param)
    elif (menu_level == 5):
        current_list = listar_por_tipo(param)
    
    show_pokemones(current_list,list_start, 5)
    
def menu_show(number):
    next = 0
    param = ''
    while True:
        menu_level = number
        if (next == 0):
            param = input(sugerencias[menu_level - 1] + "\nEscriba la sugerencia o escriba S para regresar al menu principal: ").lower()

            if param == 's':
                menu_level = 0
                break
            
        Ejecutar_Listado(menu_level, param, next)
        
        ipt = input("Escriba A para listar los siguientes o S para salir al menu: ").lower()
        os.system('cls')
        
        if (ipt == "a"): 
            next += 5
        elif (ipt == "s"):
            menu_level = 0
            break

        
if __name__ == "__main__":
    while True:
        if (menu_level == 0):
            ipt = input(menu_principal + "Ingrese el numero de la opcion o escriba S para salir: ").lower()
            if (ipt == '1' or ipt == '2' or ipt == '3' or ipt == '4' or ipt == '5'):
                os.system('cls')
                menu_show( int(ipt))
            elif (ipt == "s"):
                break