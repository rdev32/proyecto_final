from book import Libro
import os
import json
import csv

class Program():
    def __init__(self, filename):
        self.filename = filename
        self.running: bool = True
        self.menu: dict
        self.commands: list = []
        self.submenu: list = []
        self.on_submenu = False
        self.selection: str

    def init(self):
        self.clear()
        self.load_menues()
        while self.running:
            self.clear()
            self.display()
            self.events()

    def events(self):
        self.selection = input('>> ')[0].lower()
        if self.selection  == 's':
            self.running = False
        elif self.selection == 'e' or 'g' or 'i':
            self.on_submenu = True
            if self.selection == 'r':
                self.on_submenu = not self.on_submenu
        
    def clear(self):
        os.system('cls')

    def display(self):
        if self.on_submenu:
            print(f"\tSeleccionaste: {self.menu[self.selection]['name']}\nEscriba la letra de la opcion que desea realizar:")
            for key, value in zip(self.menu[self.selection]['submenu'].keys(), self.menu[self.selection]['submenu'].values()):
                print(f"{key.upper()} - {value}")
        else:
            print("\tBienvenido al menu principal\nEscriba la letra de la opcion que desea realizar:")
            for key in self.menu:
                print(f"{key.upper()} - {self.menu[key]['name']}")


    def load_menues(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            self.menu = { key: value for key, value in zip(data.keys(), data.values()) }
    
    def load_commands(self):
        cmd = self.menu


def leer_libro():
    if os.path.exists(main_file):
        with open(main_file) as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                obj = Libro(row["ID"], row["Titulo"], row["Genero"], row["ISBN"], row["Editorial"], row["Autor"])
                obj_Libros.append(obj)
        print("Archivo abierto")
    else:
        print("El archivo no existe")

def listar_libros():
    pass

def agregar_libro():
    pass

def eliminar_libro(index_list:int) -> bool:
    if (index_list >= 0 and index_list < len(obj_Libros)):
        obj_Libros.pop(index_list)
        return True
    else:
        return False

def ordenar_libros():
    pass

def buscar_libro_por_isbn_titulo():
    pass

def buscar_libro_por_autor_editorial_genero(autor='', editorial='', genero='') -> list:
    result = []
    for libro in obj_Libros:
        if autor != '' and libro.get_autores().lower().find(autor) != -1:
            result.append(libro)
        elif editorial != ''  and libro.get_editorial().lower() == editorial:
            result.append(libro)
        elif genero != ''  and libro.get_genero().lower() == genero:
            result.append(libro)
    return result

def buscar_libro_por_no_autores(num_autores:int=0) -> list:
    result = []
    for libro in obj_Libros:
        if len(libro.get_autores().split(';')) == num_autores:
            result.append(libro)
    return result

def actualizar_libro():
    pass

def guardar_libros():
    pass

if __name__ == "__main__":
    main_file = 'example_libro.csv'
    obj_Libros = []
    
    program = Program('menu_e1.json')
    program.init()
    del program