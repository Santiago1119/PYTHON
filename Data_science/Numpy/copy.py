# -*- coding: utf-8 -*-

"""
Al igualar variable a un arreglo las dos apuntaran a la misma dirección en memoria
Por lo cual si hago un cambio en uno tambien se cambiará el otro

Para poder trabajar sin tener que perder los datos utilizamos .copy()

"""


import numpy as np

arr = np.arange(0, 11)

trozo_arr = arr[0:6]
trozo_arr[:] = 0

print(trozo_arr)
print(arr)

arr_copy = arr.copy()
arr_copy[:] = 100

print(arr_copy)
print(arr)