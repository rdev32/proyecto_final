import requests

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
            print(l1[0], l1[1], l1[2])


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




menu_principal = f"1. Listar pokemons por generación\n2. Listar pokemons por forma\n3. Listar pokemons por habilidad.\n4.Listar pokemons por habitat\n5.Listar pokemons por tipo\nIngrese una opcion: "

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
    
    show_pokemones(current_list,list_start)
    
def menu_show(number):
    next = 0
    param = ''
    while True:
        menu_level = number
        if (next == 0):
            param = input("Ingrese su busqueda: ").lower()

            if param == 's':
                menu_level = 0
                break
            
        Ejecutar_Listado(menu_level, param, next)
        
        ipt = input("Escriba A para continuar o S para salir al menu`").lower()

        if (ipt == "a"): 
            next += 20
        elif (ipt == "s"):
            menu_level = 0
            break

        
if __name__ == "__main__":
    while True:
        if (menu_level == 0):
            ipt = input(menu_principal)
            if (ipt == '1' or ipt == '2' or ipt == '3' or ipt == '4' or ipt == '5'):
                menu_show( int(ipt))
            elif (ipt == "s"):
                break