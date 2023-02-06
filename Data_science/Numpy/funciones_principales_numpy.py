# -*- coding: utf-8 -*-

"""
Con max podemos saber cual es el numero más grande en el arreglo, y podemos pasarle un parametro
entre 0 y 1 especificar el axis (0: columnas 1: filas) para que saque los máximos por filas o por columnas

Con argmax podemos saber el indice del valor más grande, tambien podemos especificarle un axis entre
0 y 1 (0: columnas 1:filas)

Con min podemos saber cual es el numero más pequeño en el arreglo, y podemos pasarle un parametro
entre 0 y 1 especificar el axis (0: columnas 1: filas) para que saque los minimos por filas o por columnas

Con ptp odemos saber la diferencia que hay entre el mayor valor y el menor valor, y podemos pasarle un parametro
entre 0 y 1 para especificar el axis(0:columnas 1:filas)

Podemos saber el percentil con la función np.percentile

Podemos ordenar de menor a mayor los numeros en el arreglo con .sort

Podemos sacar la mediana con la función median

Podemos calcular la desviación estandar con la función std

Podemos calcular la varianca con la función var

Podemos calcular la media (promedio) con la funcion mean

Podemos concatenar dos arreglos con la función concatenate, los arreglos a concatenar deben tener las mismas dimensiones 
o arrojará error

En numpy existe algo que se llama transpuesta, y consiste en cambiarle la forma a un arreglo de dos o más dimensiones
y podemos especificarlo en la operacion concat con un .T

"""


import numpy as np

arr = np.random.randint(1,20, 10)
matriz = arr.reshape(2, 5)

print(f'matriz base: \n {matriz} \n')

print(f'array base: \n {arr} \n')

max_matriz = matriz.max(1)
argmax = matriz.argmax(1)

print(f'valores máximos de las filas de la matriz {max_matriz} \n')
print(f'posiciones de los valores máximos de las filas de la matriz {argmax} \n')


min_matriz = matriz.min(1)
argmin = matriz.argmin(1)

print(f'valores minimos de las filas de la matriz {min_matriz} \n')
print(f'posiciones de los valores minimos de las filas de la matriz {argmin} \n')

pick_to_pick = matriz.ptp(1)
print(f'diferencia entre el mayor valor y el menor valor por filas {pick_to_pick}')

percentile = np.percentile(arr, 50)
print(f'\npercentil del 50% {percentile} \n')

arr.sort()
print(f'\narreglo ordenado de menor a mayor \n percentile{arr}')

median = np.median(arr)
print(f'\nmediana de un arreglo o una matriz \n{median}')

desviacion_estandar= np.std(arr)
print(f'\ndesviacion estandas del arreglo o matriz \n{desviacion_estandar}')

varianza = np.var(arr)
print(f'\nla varianza es {varianza}')

media = np.mean(arr)
print(f'\nLa media de los valores es {media}')

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

print(f'\nArreglo concatenado \n{np.concatenate((a, b), axis=0)}')

transpuesta = np.concatenate((a, b.T), axis=1)
print(f'\nArreglo con Transpuesta \n{transpuesta}')




