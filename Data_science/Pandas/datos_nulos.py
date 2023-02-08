# -*- coding: utf-8 -*-

"""
Podemos ejecutar la función "isnull()" de pandas, la cual retorna un
dataframe con valores booleanos y con el cual podemos identificar
si hay algun valor nulo o no

Con 'fillna()' podemos encontrar los valores nulos dentro de un dataframe
y reemplazarlos con un número o con un string

Con "interpolate()" podemos hacer que analice el dataframe y si la columna es 
de tipo numerico crea una secuencia numerica, no afecta a los string y los deja
en null

Con "dropna() podemos borrar todas las filas que tengan un valor vacío"


"""


import pandas as pd
import numpy as np

dictionary = {'Col1': [1, 2, 3, np.nan],
              'Col2': [3, np.nan, 6, 7],
              'Col3': ['a', 'b', 'c', None]}

df_vacio = pd.DataFrame(dictionary)

print(df_vacio)
print(f'es nulo?: \n {pd.isnull(df_vacio)}')
print(f'reemplazado: \n {df_vacio.fillna("Missing")}')
print(f'seguir serie numerica: \n {df_vacio.interpolate()}')
print(f'borrar vacios: \n {df_vacio.dropna()}')

