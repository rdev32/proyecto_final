from book import Libro
import csv

def leer_libro(filename):
    buffer = []
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            item = Libro(row["id"], row["titulo"], row["genero"], row["isbn"], row["editorial"], row["autor"])
            buffer.append(item)
    return buffer

def listar_libros(books):
    for book in books:
        print(book)

def agregar_libro(books):

    titulo= input("Ingrese Titulo")
    genero = input("Ingrese Genero")
    isbn = input("Ingrese ISBN")
    editorial = input("Ingrese Editorial")
    autor = input("Ingrese Autor(es)")

    libro = Libro(id=len(books) + 1, titulo=titulo, genero=genero, isbn=isbn, editorial=editorial, autores=autor)
    books.append(libro)

def eliminar_libro(index_list: int, books):
    if (index_list >= 0 and index_list < len(books)):
        books.pop(index_list)

def ordenar_libros(books: list):
    return sorted(books, key=lambda book: book.get_titulo())

def buscar_libro_por_isbn_titulo(books, isbn = '', title = ''):
    ref: Libro
    if isbn != '':
        for book in books:
            if book.get_isbn() == isbn:
                ref = book
    elif title != '':
        for book in books:
            if book.get_titulo() == title:
                ref = book
    return ref

def buscar_libro_por_autor_editorial_genero(books, autor='', editorial='', genero='') -> list:
    result = []
    for libro in books:
        if autor != '' and libro.get_autores().lower().find(autor) != -1:
            result.append(libro)
        elif editorial != ''  and libro.get_editorial().lower() == editorial:
            result.append(libro)
        elif genero != ''  and libro.get_genero().lower() == genero:
            result.append(libro)
    return result

def buscar_libro_por_no_autores(books, num_autores: int = 0) -> list:
    result = []
    for libro in books:
        if len(libro.get_autores().split(',')) == num_autores:
            result.append(libro)
    return result

def actualizar_libro(books: list, index):

    titulo= input("Ingrese Titulo")
    genero = input("Ingrese Genero")
    isbn = input("Ingrese ISBN")
    editorial = input("Ingrese Editorial")
    autor = input("Ingrese Autor(es)")

    libro = Libro(id=index, titulo=titulo, genero=genero, isbn=isbn, editorial=editorial, autores=autor)
    
    books[index] = libro

def guardar_libros(filename, books) -> bool:
    try:
        field_header = ['ID' , 'Titulo' , 'Genero' , 'ISBN' , 'Editorial' , 'Autor']
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
    libros = leer_libro('example_libro.csv')
    listar_libros(libros)
    libros = ordenar_libros(libros)
    listar_libros(libros)
    print(buscar_libro_por_isbn_titulo(libros, isbn='122-444-222'))
