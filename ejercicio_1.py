from book import Libro
import csv
import os

def leer_libro(filename: str) -> list:
    try:
        buffer = []
        with open(filename, 'r') as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                item = Libro(row["id"], row["titulo"], row["genero"], row["isbn"], row["editorial"], row["autor"])
                buffer.append(item)
        return buffer
    except:
        return None

def listar_libros(books):
    for book in books:
        print(book)

def agregar_libro(books):

    titulo= input("Ingrese Titulo: ")
    genero = input("Ingrese Genero: ")
    isbn = input("Ingrese ISBN: ")
    editorial = input("Ingrese Editorial: ")
    autor = input("Ingrese Autor(es): ")

    libro = Libro(id=len(books) + 1, titulo=titulo, genero=genero, isbn=isbn, editorial=editorial, autores=autor)
    books.append(libro)

def eliminar_libro(books, index_list: int) -> bool:
    for book in books:
        if book.get_id() == str(index_list):
            books.remove(book)

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

def buscar_libro_por_autor_editorial_genero(books: list, autor:str = '', editorial:str = '', genero: str = '') -> list:
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

def actualizar_libro(books: list, index, title='', genre='', isbn='', editorial='', author='' ):
    if (index >= len(books)):
        print("Ese ID no existe")
        return
        
    elif title != '':
        libro = buscar_libro_por_isbn_titulo(books, title=title)
        libro.set_titulo(title)
        books[index] = libro
    elif genre != '':
        libro = buscar_libro_por_autor_editorial_genero(books, genero=genre)
        for book in books:
            book.set_genero(genre)
    elif isbn != '':
        libro = buscar_libro_por_isbn_titulo(books, isbn=isbn)
        libro.set_titulo(isbn)
        books[index] = libro
    elif editorial != '':
        libro = buscar_libro_por_autor_editorial_genero(books, editorial=editorial)
        for book in books:
            book.set_genero(editorial)
    elif author != '':
        libro = buscar_libro_por_autor_editorial_genero(books, autor=author)
        for book in books:
            book.set_genero(author)

def guardar_libros(filename, books) -> bool:
    try:
        field_header = ['id' , 'titulo' , 'genero' , 'isbn' , 'editorial' , 'autor']
        with open( filename, 'w', newline='') as csv_file:
            w_csv = csv.writer(csv_file)
            w_csv.writerow(field_header)
            for data in books:
                w_csv.writerow([data.get_id(), data.get_titulo(), data.get_genero(), data.get_isbn(), data.get_editorial(), data.get_autores()])
        csv_file.close()
        return True
    except:
        return False

if __name__ == "__main__":
    menu_principal = """
    \t\tBienvenido al menu principal
    Escriba la letra de la opcion que desee realizar: 
        A - Cargar libros de archivo
        B - Listar libros
        C - Agregar libro
        D - Eliminar libro
        E - Buscar libros por codigo ISBN o por titulo
        F - Ordenar libros por titulo
        G - Buscar libros por autor, editorial o genero
        H - Buscar libros por numero de autores
        I - Editar libro
        J - Guardar libros en archivo
    Presione S para salir del programa
    """
    
    submenu_e = """
    \t\tSeleccionaste: Buscar libros por codigo ISBN o por titulo
    Escriba la letra de la opcion que desee realizar: 
        A - Buscar por titulo
        B - Buscar por ISBN
    Presione R para regresar al menu principal
    """

    submenu_g = """
    \t\tSeleccionaste: Buscar libros por autor, editorial o genero
    Escriba la letra de la opcion que desee realizar: 
        A - Buscar por autor
        B - Buscar por editorial
        C - Buscar por genero
    Presione R para regresar al menu principal
    """

    submenu_i = """
    \t\tSeleccionaste: Editar libro
    Escriba la letra de la opcion que desee realizar:
        A - Editar titulo
        B - Editar genero
        C - Editar ISBN
        D - Editar editorial
        E - Editar autor/autores
    Presione R para regresar al menu principal
    """
    libros: list = []
    loaded: bool = False

    while True:
        os.system('cls')
        print(menu_principal)
        selection = input(">> ").lower()

        if selection == 's':
            break
        
        elif selection == 'a':
            os.system('cls')
            print("\t\tSeleccionaste: Cargar libros de archivo")
            try:
                libros = leer_libro('example_libro.csv')
                loaded = True
                print("OK")
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        elif selection == 'b':
            os.system('cls')
            print("\t\tSeleccionaste: Listar libros")
            if not loaded:
                print("Aun no se han cargado los archivos en disco")
            try:
                listar_libros(libros)
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        elif selection == 'c':
            os.system('cls')
            print("\t\tSeleccionaste: Agregar libro")
            if not loaded:
                print("Aun no se han cargado los archivos en disco")
            try:
                agregar_libro(libros)
                print("OK")
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        elif selection == 'd':
            os.system('cls')
            print("\t\tSeleccionaste: Eliminar libro")
            if not loaded:
                print("Aun no se han cargado los archivos en disco")
            try:
                listar_libros(libros)
                index = int(float(input("Escriba el id(numero) del libro que desea eliminar: ")))
                eliminar_libro(libros, index_list=index)
                print("OK")
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        elif selection == 'e':
            while True:
                os.system('cls')
                print(submenu_e)
                if not loaded:
                    print("Aun no se han cargado los archivos en disco")
                sub_selection = input(">> ")
                if sub_selection == 'r':
                    break

                if sub_selection == 'a':
                    os.system('cls')
                    print("\t\tSeleccionaste: Buscar por Titulo")
                    listar_libros(libros)
                    titulo = input("Ingrese el titulo del libro: ")
                    libro = buscar_libro_por_isbn_titulo(libros, title=titulo)
                    print("Encontraste: ")
                    print(libro)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'b':
                    os.system('cls')
                    print("\t\tSeleccionaste: Buscar por ISBN")
                    listar_libros(libros)
                    isbn = input("Ingrese ISBN: ").upper()
                    libro = buscar_libro_por_isbn_titulo(libros, isbn=isbn)
                    print("Encontraste: ")
                    print(libro)
                    input("Presione cualquier tecla para regresar")

        elif selection == 'f':
            os.system('cls')
            print("\t\tSeleccionaste: Ordenar libros por titulo")
            if not loaded:
                print("Aun no se han cargado los archivos en disco")
            try:
                libros = ordenar_libros(libros)
                print("OK")
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        elif selection == 'g':
            while True:
                os.system('cls')
                print(submenu_g)
                if not loaded:
                    print("Aun no se han cargado los archivos en disco")
                sub_selection = input(">> ")
                if sub_selection == 'r':
                    break
                if sub_selection == 'a':
                    os.system('cls')
                    print("\t\tSeleccionaste: Buscar por autor")
                    listar_libros(libros)
                    autor = input("Ingrese autor: ")
                    libro = buscar_libro_por_autor_editorial_genero(libros, autor=autor)
                    print("Encontraste: ")
                    print(libro)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'b':
                    os.system('cls')
                    print("\t\tSeleccionaste: Buscar por editorial")
                    listar_libros(libros)
                    editorial = input("Ingrese editorial: ")
                    libro = buscar_libro_por_autor_editorial_genero(libros, editorial=editorial)
                    print("Encontraste: ")
                    print(libro)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'c':
                    os.system('cls')
                    print("\t\tSeleccionaste: Buscar por genero")
                    listar_libros(libros)
                    genero = input("Ingrese genero: ")
                    libro = buscar_libro_por_autor_editorial_genero(libros, genero=genero)
                    print("Encontraste: ")
                    print(libro)
                    input("Presione cualquier tecla para regresar")

        elif selection == 'h':
            os.system('cls')
            print("\t\tSeleccionaste: Buscar libros por numero de autores")
            if not loaded:
                print("Aun no se han cargado los archivos en disco")
            try:
                os.system('cls')
                print("\t\tSeleccionaste: Buscar por numero de autores")
                listar_libros(libros)
                no_autores = int(float(input("Ingrese numero de autores: ")))
                libro = buscar_libro_por_no_autores(libros, no_autores)
                print("Encontraste: ")
                print(libro)
                input("Presione cualquier tecla para regresar")
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        elif selection == 'i':
            while True:
                os.system('cls')
                print(submenu_i)
                if not loaded:
                    print("Aun no se han cargado los archivos en disco")
                sub_selection = input(">> ")
                if sub_selection == 'r':
                    break
                if sub_selection == 'a':
                    os.system('cls')
                    print("\t\tSeleccionaste: Editar titulo")
                    listar_libros(libros)
                    index = input("Ingrese el id(numero) del libro: ")
                    titulo = input("Ingrese el titulo nuevo: ")
                    actualizar_libro(libros, index=index, title=titulo)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'b':
                    os.system('cls')
                    print("\t\tSeleccionaste: Editar genero")
                    listar_libros(libros)
                    index = input("Ingrese el id(numero) del libro: ")
                    genero = input("Ingrese el nuevo genero: ")
                    actualizar_libro(libros, index=index, genre=genero)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'c':
                    os.system('cls')
                    print("\t\tSeleccionaste: Editar ISBN")
                    listar_libros(libros)
                    index = input("Ingrese el id(numero) del libro: ")
                    isbn = input("Ingrese nueva ISBN: ")
                    actualizar_libro(libros, index=index, isbn=isbn)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'd':
                    os.system('cls')
                    print("\t\tSeleccionaste: Editar editorial")
                    listar_libros(libros)
                    index = input("Ingrese el id(numero) del libro: ")
                    editorial = input("Ingrese editorial: ")
                    libro = actualizar_libro(libros, index=index, editorial=editorial)
                    input("Presione cualquier tecla para regresar")

                if sub_selection == 'e':
                    os.system('cls')
                    print("\t\tSeleccionaste: Editar autor(es)")
                    listar_libros(libros)
                    index = input("Ingrese el id(numero) del libro: ")
                    autores = input("Ingrese nuevos autor(es): ")
                    libro = actualizar_libro(libros, index=index, author=autores)
                    input("Presione cualquier tecla para regresar")

        elif selection == 'j':
            os.system('cls')
            print("\t\tSeleccionaste: Guardar libros en archivo")
            if not loaded:
                print("Aun no se han cargado los archivos en disco")
            try:
                guardar_libros('example_libro.csv', libros)
                print("OK")
            except:
                print("Error cargando archivo")
            input("Presione cualquier tecla para regresar")

        else:
            continue