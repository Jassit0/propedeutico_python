# EJERCICIOS DE LA SEMANA DEL 14 AL 20 DE JULIO 


"""
EJERCICIO 1- Crea un repositorio en GitHub, en este repositorio guardarás todos tus ejercicios
Nota: el paso 1 se cumple una vez creado el repositorio
"""


# EJERCICIO 2- Crea un coentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado
# URL del sitio de Python: https://www.python.org/


# EJERCICIO 3- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje
# Los comentarios en Python comienzan con el carácter numeral conocido como gato
"Las cadenas de texto se pueden delimitar con comillas simples ó dobles"
"""
Las comillas 
tripes permiten que
las cadenas de texto 
ocupen más de una línea
"""


# EJERCICIO 4- Crea una variable (y una constante si el lenguaje lo soporta)

nombre_padawan = "Jacqueline Jasso"

"""
En python, las constantes son usualmente declaradas y asignadas en un módulo. 
El módulo significa un nuevo archivo que contiene variables, funciones, etc.
Por lo tanto, en Python no se tiene una sintaxis dedicada para la declaración de constantes, 
en otras palabras, no existen constantes en el sentido estricto de la palabra. 
Lo que se puede realizar es usar una variable y asumir que nunca va a cambiar
"""
# ejemplo de variable 
PI = 3.1416
print(PI)
print("-----------------")



#EJERCICIO 5 Crea variables representando todos los tipos de datos primitivos del lenguaje

#dato numerico 
int = 10, 45, 23 #enteros
float = 2.5 #flotante
complex = 2j #complejo
print(int)
print(float)
print(complex)
print("-----------------")

#dato boleano
sith = True
jedi = False
print(True)
print(False)
print("-----------------")

#dato texto 
nombre = "maestra Naye" #cadenas de texto (strings)
grupo = "1" #todo lo que está entre comillas es un tipo de string
print(grupo)
print(type(grupo))
print("-----------------")

#dato none (representan la ausencia de un valor)
nada = None
print(nada)
print("-----------------")


"""
COLECCIONES
Además de los tipos de datos básicos, en Python se cuenta 
con tipos más complejos que se denominan colecciones,
ya que son tipos de datos que sirven para agrupar elementos. 
En Python existen tres colecciones básicas: 
las listas (list), las tuplas (tuple) y los diccionarios (dictionary).
"""
#listas
lista = ["hola", 5, 3.2, True, None]
print(lista)
print(type(lista))

#tupla
tuple = ("hola", 5, 3.2, True, None)
tupla = "hola", 5, 3.2, True, None
print(type(tuple))
print(type(tupla))

#diccionario 
diccionario = {"nombre": "Jasso", "edad" : 29, "lenguaje" : "Python"}
print(diccionario)



"""
CONJUNTOS 
Un conjunto es una colección desordenada de elementos únicos, 
es decir, que no se repiten. 
En Python existen los sets y los frozensets. 
"""

#conjuntos
conjuntos = {"hola", 5, 3.2, True, None}
print(type(conjuntos))

print("-------------------------------")





# EJERCICIO 6- Imprime por terminar el texto "¡Hola, Python!"
print("¡Hola, Python!")


