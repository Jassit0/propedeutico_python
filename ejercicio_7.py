# EJERCICIO 7- Crea ejemplos utilizando todos los tipos de operadores de Python 

#OPERADORES DE ASIGNACIÓN
numero = 30
numero += 5 #sumar 5
print(numero)

numero -=3 #al número anterior restar 3
print(numero)

numero *=4
print(numero) #múltiplicar por 4

numero /= 2 #dividir entre 2
print(numero)

numero %=5 #modulo 
print(numero)

numero **=2 #Exponente 
print(numero)

numero //=4 #división
print(numero)

print("---------------------")



#OPERADORES DE COMPARACIÓN
edad1 = 36
edad2 = 29

igualdad = edad1 == edad2  
print(igualdad)

diferencia = edad1 != edad2
print(diferencia)

menor = edad1 < edad2 #¿29 es menor a 36? Falso
print(menor)

mayor = edad1 > edad2
print(mayor)

menor_igual = edad1 <= edad2
print(menor_igual)

mayor_igual = edad1 >= edad2
print(mayor_igual)

print("------------")



#OPERADORES LÓGICOS 
# (se utiliza para combinar declaraciones condicionales)
distancia1 = 532 
distancia2 = 354

comparacion1 = distancia1 == distancia2 and distancia1 > distancia2
print(comparacion1)

comparacion2 = distancia1 == distancia2 or distancia1 > distancia2
print(comparacion2)

comparacion3 = not distancia2 >= distancia1
print(comparacion3)
print("-----------------")



#OPERADORES DE IDENTIDAD 
"""
compara dos variables, no sólo por su valor 
(como en el caso de la comparación) sino que
comprueba que sean o no, exactamente el mismo objeto
"""
tamaño1 = 57
tamaño2 = 43

comparacion_is = tamaño1 is tamaño2
print(comparacion_is)

comparacion_isnot = tamaño1 is not tamaño2
print(comparacion_isnot)
print("----------------------")



#OPERADORES DE PERTENENCIA (se utilizan para comprobar si una secuencia almacena un valor partícular)
saludo = "Hola soy Jasso"

pertenencia = "Hola" in saludo
print(pertenencia)

noPertenecia = "Mundo" not in saludo
print(noPertenecia)

noPertenecia2 = "soy" not in saludo
print(noPertenecia2)
print("-------------------------")



#OPERADORES DE BITWISE (PARA COMPARAR BINARIOS)
tamaño1 = 90
tamaño2 = 45
print(bin(tamaño1))
print(bin(tamaño2))

resultado1 = tamaño1 & tamaño2
print(bin(resultado1))

resultado2 = tamaño1 | tamaño2
print(bin(resultado2))

resultado3 = tamaño1 ^ tamaño2
print(bin(resultado3))

resultado4 = ~ tamaño1 #(not), invierte los bits
print(bin(resultado4))

resultado5 = tamaño1 << 2 #es más usado para el manejo de imagenes
print(bin(resultado5))

resultado6 = tamaño1 >> 2
print(bin(resultado6))

print("---------------------")