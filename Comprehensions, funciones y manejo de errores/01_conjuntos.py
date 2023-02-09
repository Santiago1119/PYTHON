# -*- coding: utf-8 -*-
"""
Los conjuntos se pueden modificar
No tienen un orden específico
No se permiten duplicados

Se crean con corchetes, pero los sets no tienen llaves
se puede crear un elemento con cualquier tipo de dato dentro de un conjunto
un diccionario tambien se puede convertir a una lista


"""

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]

set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)