# -*- coding: utf-8 -*-

"""
Podemos eliminar las columnas de un dataframe con drop y tambien podemos especificar el axis
(0: fila 1: columna), este comando mostrara un dataframe sin la columna o fila especificada
pero si queremos que se borre del dataframe original debemos usar la propiedad adicionar "inplace=True"
mbien como primer parametro de drop se puede pasar una lista como elementos a eliminar

Para borrar filas de un dataframe tambien se utiliza drop pero indicando el indice de la fila con 
el axis en 0 y para guardar los cambios hechos en el dataframe original debemos utilizar la propiedad
"inplace=True", tambien como primer parametro de drop se puede pasar una lista como elementos a eliminar

TAMBIEN SE PUEDE HACER CON UNA TUPLA, OSEA QUE SI PASAMOS UN RANGE COMO PARAMETRO DE DROP FUNCIONARÁ


Para agregar columnas a un dataframe puedo hacerlo como en un diccionario, se pasa el nombre de la columna
nueva en llaves cuadradas y con una función de numpy puedo asigar todos los valores de las filas del dataframe como
NaN

Tambien se puede a partir de un vector ya existente crear una nueva columna, y debe ser igual a la cantidad de filas que hay en 
el dataframe


Para agregar filas utilizamos concat| y este agregará las cosas a nivel de filas

"""


import pandas as pd
import numpy as np

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)

print(df_books.loc[0:10, ['Name', 'Author']])

columna_eliminada = df_books.drop(['Name', 'Genre'], axis=1).head(2)
print(columna_eliminada)

df_books.drop([0, 1, 2], axis=0, inplace=True)
print(df_books)

df_books['New_column'] = np.nan
print(df_books)

data = np.arange(0,df_books.shape[0])
print(data)

df_books['Rango'] = data
print(df_books)

df_books = pd.concat([df_books, df_books])
print(df_books)

