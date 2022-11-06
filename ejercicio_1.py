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


def leer_libro(filename: str) -> list:
    try:
        lista = []
        with open(filename) as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                obj = Libro(row["id"], row["titulo"], row["genero"], row["isbn"], row["editorial"], row["autor"])
                lista.append(obj)
        return lista
    except:
        return None

def listar_libros():
    pass

def agregar_libro():
    pass

def eliminar_libro(index_list: int, books: list = None) -> bool:
    if (index_list >= 0 and index_list < len(books)):
        books.pop(index_list)
        return True
    else:
        return False

def ordenar_libros():
    pass

def buscar_libro_por_isbn_titulo():
    pass

def buscar_libro_por_autor_editorial_genero(autor:str = '', editorial:str = '', genero: str = '', books: list = None) -> list:
    result = []
    for book in books:
        if autor != '' and book.get_autores().lower().find(autor) != -1:
            result.append(book)
        elif editorial != ''  and book.get_editorial().lower() == editorial:
            result.append(book)
        elif genero != ''  and book.get_genero().lower() == genero:
            result.append(book)
    return result

def buscar_libro_por_no_autores(num_autores: int = 0, books: list = None) -> list:
    result = []
    for book in books:
        if len(book.get_autores().split(';')) == num_autores:
            result.append(book)
    return result

def actualizar_libro():
    pass

def guardar_libros(filename: str, books: list = None) -> bool:
    try:
        field_header = ['id' , 'titulo' , 'genero' , 'isbn' , 'editorial' , 'autor']
        with open( filename, 'w') as csv_file:
            w_csv = csv.writer(csv_file)
            w_csv.writerow(field_header)
            for data in books:
                w_csv.writerow([data.get_id(), data.get_titulo(), data.get_genero(), data.get_isbn(), data.get_editorial(), data.get_autores()])
        csv_file.close()
        return True
    except:
        return False

if __name__ == "__main__":
    program = Program('menu_e1.json')
    program.init()
    del program