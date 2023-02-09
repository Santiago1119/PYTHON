# -*- coding: utf-8 -*-
"""
List comprehension es un termino que se utiliza para realizar listas
con iteraciones en una sola linea de código

el elemento_lista y el elemento_iterado son el mismo, y al elemento_lista
se le pueden aplicar cambios y este será el resultado reflejado en la lista 
que estamos creando con list comprehesion

[elemento_lista for elemento_iterado in objeto_iterable]

dentro de esa compresión de lista tambien puedo agregar una condición después de la
iteración la cual indica que solo se pueden agregar los elementos a la lista si 
esa condición se comple

[elemento_lista for elemento_iterado in objeto_iterable if elemento_iterado (condicion)]

"""

numbers = []
for element in range(1, 11):

    numbers.append(element * 2)
    
print(numbers)

number_v2 = [element * 2 for element in range(1, 11) if element % 2 == 0]

print(number_v2)

number_v3 = [element ** 2 for element in range(10, 21) if element % 2 != 0]
print(number_v3)