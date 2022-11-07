import requests

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