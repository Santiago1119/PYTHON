# -*- coding: utf-8 -*-

"""
Con shape podemos saber que cuantos elementos tiene el arreglo con el que estoy trabajando y en que dimensiones están

(filas, columnas)

Con reshape podemos cambiar la forma del arreglo a la que le pasemos por parametro, la nueva forma del arreglo 
debe tener el mismo tamaño al arreglo existente, y se pueden cambiar las formas del arreglo distintas veces
A la hora de hacer reshape podemos pasar un tercer parametro especificando como que lenguaje quiere que se realice
el reshape 

Reshape con C:
    Cuando se realiza un reshape con c este llena el nuevo arreglo por filas

Reshape con fortrant:
    Cuando se realiza un reshape con Fortrant llena el nuevo arreglo por columnas


(filas, columnas)

"""

import numpy as np

arr = np.random.randint(1, 10, (3, 2))
print(f'shape -> {arr.shape}')

print(f'array original -> \n {arr}')

arr = arr.reshape(1,6)
print(f'array reshapre -> \n {arr}')

arr = arr.reshape(2,3)
print(f'array nuevo reshapre -> \n {arr}')

arr = arr.reshape(1,6)

arr = np.reshape(arr,(2,3), 'C')
print(f'array reshape en C -> \n {arr}')

arr = arr.reshape(1,6)

arr = np.reshape(arr,(2,3), 'F')
print(f'array reshape en F -> \n {arr}')
