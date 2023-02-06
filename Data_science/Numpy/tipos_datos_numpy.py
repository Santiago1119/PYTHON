# -*- coding: utf-8 -*-

import numpy as np

"""

Cuando creemos un array numpy elegira el tipo de dato que mejor se desempeñe dependiendo de los datos del array
Pero podemos modificar el tipo de dato con el atributo dtype='tipo de dato'

"""
arr = np.array([0,1,2,3,4], dtype = 'int64' )
print(arr.dtype)

#Si queremos modificar el tipo de dato de un arreglo ya existente lo podemos hacer con ".astype('tipo de dato')"

arr = arr.astype(np.float64)
print(arr.dtype)

#Podemos convertir arreglo a practicamente cualquier tipo de dato que maneje numpy como bool o string
#En el caso de los bool los ceros siempre seran Falsos, los demás numeros seran True
arr = arr.astype(np.bool_)
print(arr)
print(arr.dtype)


#Un string
arr = arr.astype(np.string_)
print(arr.dtype)





