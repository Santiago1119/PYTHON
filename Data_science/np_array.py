# -*- coding: utf-8 -*-

import numpy as np

#Un npArray es una lista super optimizada que puede llegar a ser hasta 50 veces más rapida

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = np.array(lista)

#El tipo de un nd.array es "numpy.ndarray"


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Matriz con numpy
matriz = np.array(matriz)

# print(matriz[0, 1])

#En caso de querer sumar dos listas dentro de una matriz se sumaran de izquierda a derecha en caso de ser numeros
# print(matriz[0] + matriz[1])


#Para hacer slicing en matrices hacemos lo mismo separado por comas, el slicing excluye en ultimo valor

print(matriz[1:, 0:2])
