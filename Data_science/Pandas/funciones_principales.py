# -*- coding: utf-8 -*-
"""
con "head()" podemos ver los primeros valores del dataframe, por defecto son 5 valores
pero podemos especificarle cuantos queremos ver

con "tail()" podemos ver los ultimos valores del dataframe, por defecto son 5 valores
pero podemos especificarle cuantos queremos ver

con "info()" podemos ver los detalles del dataframe, el nombre de cada columna y su indice,
cuantos valores contiene y que tipo de dato almacena cada columna, tambien podemos ver el espacio
el memoria que ocupa el dataframe

con "describe()" en caso de las columnas numericas podemos ver cuantas filas tenemos, el promedio de la columna,
la desviación estandar, el valor minimo, los percentiles 25, 50 -> (mediana), 75, y el valor máximo

con "memory_usage() podemos ver cuanta memoria esta consumiendo cada columna en especifico y 
se utiliza a la hora de estar optimizando algo en específico"

con "value.count()" cuenta cuantas veces esta cada valor en la columna que se le especifica

con "drop_duplicates()" eliminamos todos los duplicados en un dataframe y le podemos especificar el parametro keep="last"
para que borre el primer duplicado en lugar del ultimo

con "sort_values()" le especificamos una columna por la cual queremos que se ordene el dataframe, por defecto ordena
de menor a mayor, pero si le pasamos el parametro "ascending=False" lo ordenará de mayor a menor

"""

import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)


print(df_books.head(2))
print(df_books.info())
print(df_books.memory_usage(deep=True))
print(df_books['Author'].value_counts())

print(df_books)
df_books = pd.concat([df_books[:], df_books.loc[0:2]], ignore_index=True)

print(df_books.drop_duplicates()) 

print(df_books.sort_values('Year'))
