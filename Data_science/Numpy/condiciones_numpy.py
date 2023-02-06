# -*- coding: utf-8 -*-

"""
Se pueden hacer condiciones y estas retornan valores booleanos
Estas se pueden utilizar para hacer slicing dependiendo de la condición

Tambien se pueden modificar los valores de un arreglo si cumplen con una condición dada

Otra funcion muy util de numpy tambien es np.where(condicion, valor si, valor si la condicion no se cumple)

"""


import numpy as np

arr = np.linspace(1,10,10, dtype='int8')
indices_cond = arr > 5
print(f'Numeros mayores que 5 y menores que 9 {arr[(arr > 5) & (arr < 9)]}')

arr[arr > 5] = 99
print(f'Numeros mayores que 5 ahora serán 99 {arr}')

print(f'Numeros iguales a 99 {arr[arr == 99]}')


