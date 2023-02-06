# -*- coding: utf-8 -*-

"""
Los datos solos de cualquier tipo son Scalares

Los Vectores son arreglos de una sola dimension

Las Matrices son arreglos de dos dimensiones

Los Tensores son arreglos de 3 o más dimensiones


Con la propiedad ndim podemos saber el número de dimensiones que tiene un ndArray

Agregando el atributo ndmin a la hora de crear el ndArray podemos especificar el número
de dimensiones que tendra nuestro Array 

Para agregar una dimension a un Array ya existente utilizamos np.expand_dims()

Para eliminar una o más dimensiones a un Array existente utilizamos np.squeeze y numpy
dejará solo las dimensiones que se esten utilizando y las que sobren las eliminará

"""

import numpy as np

scalar = np.array(42)
print(scalar.ndim)

vector = np.array([1, 2, 3])
print(vector.ndim)

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz.ndim)

tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]])
print(tensor.ndim)

estructura_ndmin = np.array([1, 2, 3], ndmin=10)
print(estructura_ndmin)

estructura_ndmin = np.expand_dims(estructura_ndmin, axis=0)
print(estructura_ndmin)

estructura_ndmin = np.squeeze(estructura_ndmin)
print(estructura_ndmin)
