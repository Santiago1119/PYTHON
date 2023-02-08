# -*- coding: utf-8 -*-
"""
Con concat podemos concatenar dataframes, por defecto este concatena por el axis 0:filas
y todos los datos tendran en index que tenian en su dataframe original, y para solucionar esto utilizamos
"ignore_index=True" para que en el nuevo dataframe tengan indices por defecto

Tambien se le puede especificar el axis por el cual queremos que haga la concatenación, 
si elegimos 1 este ampliará de forma horizontal, osea aumentará el número de columnas

Merge nos sirve para juntar dos dataframes dependiendo de unas una columna en común, si las columnas no tienen
el mismo nombre hay que especificar la columna que ira a la izquierda y la columna que ira a la derecha,
en caso de que dos columnas no tengan el mismo valor el valor se excluirá del merge

Si queremos modificar este comportamiento podemos hacerlo con la propiedad "how=" el valor por defecto es "inner"
el cual solo trae los valores que tengan el mismo nombre de columnas, podemos asignar el valor "left" el cual 
traera todos los valores de la izquierda y donde no sean iguales las columnas a la derecha pondrá NaN o "right" que
hace lo mismo que left

Con "join" se puede hacer lo mismo que con merge pero especificando los indices de los dataframes
tambien se le puede dar la propiedad "how=" con los valores left, right, join y outer


"""

import pandas as pd

df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
              'B':['B0', 'B1', 'B2', 'B3'],
              'C':['C0', 'C1', 'C2', 'C3'],
              'D':['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
              'B':['B4', 'B5', 'B6', 'B7'],
              'C':['C4', 'C5', 'C6', 'C7'],
              'D':['D4', 'D5', 'D6', 'D7']})

print(df1)
print(df2, '\n')

print(pd.concat([df1, df2], ignore_index=True))
print(pd.concat([df1, df2], axis=1))

df_izq = pd.DataFrame({'key':['k0', 'k1', 'k2', 'k3'],
                    'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3']})

df_der = pd.DataFrame({'key_2':['k0', 'k1', 'ks', 'k3'],
                    'C':['C0', 'C1', 'C2', 'C3'],
                    'D':['D0', 'D1', 'D2', 'D3']})

print(df_izq,'\n')
print(df_der)

# print(df_izq.merge(df_der, on='key'))
print(df_izq.merge(df_der, left_on='key', right_on='key_2', how='left'))

df_izq_join = pd.DataFrame({'A':['A1', 'A1', 'A2'],
                    'B':['B0', 'B1', 'B2']},
                    index=['k0', 'k1', 'k2'])

df_der_join = pd.DataFrame({'C':['C0', 'C1', 'C2'],
                    'D':['D0', 'D1', 'D2']},
                    index=['k0', 'k2', 'k3'])

print(df_izq_join.join(df_der_join, how="left"))









