import requests

def generar_info(index: int):
    pass

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

def listar_por_habilidad():
    pass

def listar_por_habitad():
    pass

def listar_por_tipo():
    pass

if __name__ == "__main__":
    pass