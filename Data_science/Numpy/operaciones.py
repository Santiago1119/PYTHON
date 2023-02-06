# -*- coding: utf-8 -*-

"""
Las listas de python no pueden operar sus valores

lista = [1, 2]
print(lista * 2)

Out: [1, 2, 1, 2]


Con numpy se puedes realizar estas operaciones, y tambien se pueden realizar 
operaciones entre arreglos o matrices, pero deben ser del mismo tamaño

Podemos sacar el producto punto de una matriz con 

o podemos hacerla con un arroba en medio de dos matrices

"""

import numpy as np

arr = np.arange(0, 10)
arr2 = arr.copy()

print(arr + 2)
print(arr * 2)
# print(1 / arr)
print(arr + arr2)

matriz = arr.reshape(2, 5)
matriz2 = matriz.copy()

print(matriz + matriz2)
print(matriz - matriz2)

producto_punto = np.matmul(matriz, matriz2.T)

print(f'\nProducto punto de 2 matrices \n {producto_punto} \n')

print(matriz @ matriz2.T)

