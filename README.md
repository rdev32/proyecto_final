# Proyecto Final Bootcamp Backend MTPE

## Consideraciones
El trabajo tiene las siguientes consideraciones:

- Deadline: Domingo 6 de Noviembre 11:59 p.m.
- Uso de 1 repositorio github para las 2 tareas. Cada tarea principal es un script (archivo .py). Pueden usar más archivos para complementar u ordenar su código.
- Se van a evaluar los commits, es decir 1 solo commit en total para un repositorio no es aceptado.
- Trabajo en grupo con alumnos de la misma aula (mínimo 2, máximo 3 personas), no se aceptan proyectos individuales.
- Cada alumno debe trabajar en una parte de cada una de las 2 tareas. Es decir, no puede haber 1 alumno que haga solo 1 tarea y el resto haga la otra. Se deben trabajar en ramas y la rama main es la que recibe los aportes de las otras.
- La presentación del trabajo es colocar la URL de su repositorio en: Tarea: URL de Proyecto

## Tareas
Debe desarrollar las siguientes 2 tareas en un repositorio de github. Cada tarea es un archivo .py
### Tarea 1
Se tiene la clase Libro con los siguientes atributos: id, título, género, ISBN, editorial y autor(es). Considerar que un libro puede tener varios autores.

Se solicita escribir un programa en Python que permita registrar libros. Debe utilizar: colecciones (listas, tuplas, etc), funciones y clases de Python.

Dicho programa debe tener un menu (a interactuar en la línea de comando) para:

- Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.
- Opción 2: Listar libros.
- Opción 3: Agregar libro.
- Opción 4: Eliminar libro.
- Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.
- Opción 6: Ordenar libros por título.
- Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.
- Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.
- Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
- Opción 10: Guardar libros en archivo de disco duro (.txt o csv).

Nota: listar libros involucra: título, género, ISBN, editorial y autor(es)

### Tarea 2

La tarea gira en torno a la PokeAPI: https://pokeapi.co/docs/v2 utilizar la API v2 y el paquete requests de Python

Escribir un programa que tenga las siguientes opciones:

- Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.
- Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.
- Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
- Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
- Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.

Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen
