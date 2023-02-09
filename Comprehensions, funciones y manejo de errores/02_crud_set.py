# -*- coding: utf-8 -*-
"""
con len podemos saber el tamaño de un set

con el operador in podemos determinar si hay algún elemento
en especifico dentro del set y esto nos dará un valor booleano

con add podemos agregar un elemento al set

podemos agregar más de un elemento con update en un set con los
valores que deseamos agregar

para eliminar un elemento del conjunto se utiliza remove, si el elemento
que se especifica no existe manda error diciendo que no existe el elemento
si queremos evitar este comportamiento podemos utilizar discard, el cual si 
el elemento existe lo elimina, pero sino simplemento no hace nada

con clear se borran todos los elementos del conjunto

"""

set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)

print(size)

print('col' in set_countries)
print('pe' in set_countries)

set_countries.add('pe')
print(set_countries)

set_countries.update({'ar', 'ecu', 'pe'})
print(set_countries)

set_countries.remove('col')
print(set_countries)

set_countries.discard('ar')
print(set_countries)

set_countries.clear()
print(set_countries)


