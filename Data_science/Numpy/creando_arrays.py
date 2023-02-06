# -*- coding: utf-8 -*-

"""
Con la función arange podemos definir un arreglo con valores numericos excluyendo el limite superior 
y como tercer parametro se le puede pasar como parametro el paso en el que se quiere enlistar


Para crear un array con zeros utilizamos la función np.zeros y el numero de ceros y las dimensiones que necesitamos
esto nos sirve para definir la estructura de un arreglo (Se puede hacer lo mismo con np.ones)

Para crear un array con valores dentro de un rango utilizamos linspace, y tambien podemos especificar cuantos valores
necesitamos dentro de ese rango

Para crear una matriz con la diagonal principal en 1 utilizamos la función eye y el tamaño de la matriz

Para crear un valor aleatorio entre 0 y 1 utilizamos random.rand, si le especificamos un valor numerico nos crea un arreglo
con el numero de valores aleatorios especificados, si le pasamos dos parametros nos retorna una matriz y si le pasamos tres
o más parametros nos retorna un tensor

Para crear un valor aleatorio entero entre valores especificados utilizamos random.randint, si queremos que introduzca los valores
dentro de una matriz o un tensor especificamos una tupla con el tamaño que la estructura que deseemos (El limite superior se excluye)

"""

import numpy as np

lista = np.arange(0, 11, 2)
print(lista)

zeros = np.zeros((10, 10))
print(zeros)

linspace = np.linspace(0, 10, 100)
print(linspace)

eye = np.eye(4)
print(eye)

aleatorio = np.random.rand(4, 4, 4, 4)
print(aleatorio)

int_aleatorio = np.random.randint(1, 10,(10, 10))
print(int_aleatorio)