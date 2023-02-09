# -*- coding: utf-8 -*-
"""
Con "union" podemos combinar dos set que tenemos por separado,
otra forma de realizar esta unión sin necesidad de ejecutar el metodo "union"
es hacerlo con el operador de unión (|)

Con "intersection" tenemos los datos en comun que tienen los dos conjuntos
en un nuevo conjunto sin repeticiones, otra forma de realizar la intersección sin necesidad
de ejecutar el metodo "intersection" es hacerlo con el operador de intersección (&)

Con "difference" podemos saber cuales son los datos unicos del set, respecto a otro set

Con "symmetric_difference" podemos saber cuales son los valores que no se repiten en los dos conjuntos
en caso de repetirse no los muestra, otra forma de realizar la diferencia simetrica sin necesidad
de ejecutar el metodo "symmetric_difference" es hacerlo con el signo de intercalación(^)


"""
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
set_x = {'col', 'arg'}

set_c = set_a.union(set_b, set_x)
print(set_c)
print(set_a | set_b)

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

