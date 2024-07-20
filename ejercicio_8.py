"""
EJERCICIO 8 - Utilizando las operaciones con operadores que tú quieras, 
crea ejemplos que representen todos los tipos de estructuras de control
que existan en Python 
"""

#IF
muestra1 = 1582
muestra2 = 1671

if muestra1 == 1582:
    print("La muestra 1 se conformó por 1582 encuestados")

elif muestra2 == 1671:
    print("La muestra 2 se conformó por 1671 encuestados")

else:
    print("No fue el número de encuestados")    
print("----------------------------")



#For
papeleria = ["sacapuntas","lapiz","goma","plumas","tijeras"]

for item in papeleria:
    print(item)
print("----------------------------")


#while (mientras contador sea menor a 16, imprime contador)
contador = 0
while contador < 16:
    print(contador)
    contador += 2


#Try (Intenta)
try:
    if "año" == 2025:
        print("Es el año 2025")
    else:
        print("No es el año 2025")
except Exception: #Si lo anterior no funciona 
    print("Error")
finally:
    print("error")







