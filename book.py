class Libro:
    def __init__(self, id, titulo, genero, isbn, editorial, autores):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autores = autores
        
    def set_id(self, value):
        self.__id = value
    def set_titulo(self, value):
        self.__titulo = value
    def set_genero(self, value):
        self.__genero = value
    def set_isbn(self, value):
        self.__isbn = value
    def set_editorial(self, value):
        self.__editorial = value
    def set_autores(self, value):
        self.__autores = value

    def get_id(self):
        return self.__id
    def get_titulo(self):
        return self.__titulo
    def get_genero(self):
        return self.__genero
    def get_isbn(self):
        return self.__isbn
    def get_editorial(self):
        return self.__editorial
    def get_autores(self):
        return self.__autores
    
    def __del__(self):
        pass