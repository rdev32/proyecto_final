from book import Libro
import os
import json

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
    pass

def listar_libros():
    pass

def agregar_libro():
    pass

def eliminar_libro():
    pass

def ordenar_libros():
    pass

def buscar_libro_por_isbn_titulo():
    pass

def buscar_libro_por_autor_editorial_genero():
    pass

def buscar_libro_por_no_autores():
    pass

def actualizar_libro():
    pass

def guardar_libros():
    pass

if __name__ == "__main__":
    program = Program('menu_e1.json')
    program.init()
    del program