# -*- coding: utf-8 -*-

"""
Para hacer condiciones sobre una columna invocamos la columna del dataframe 
y agregamos la condicion, y retornada una serie con valores booleanos 

se puede pasar como busqueda a un dataframe una condicion, y esta solo
mostrara los registros que cumplan la condición

Podemos crear más de una condición de filtrado



Para negar una condición utilizamos la birgulilla "~"

"""

import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)
df_books = df_books.dropna()
df_books['Year'] = df_books['Year'].astype('int64')

older_than = df_books['Year'] > 2016
print(f'Año superior a 2016: \n {df_books[older_than]}')
genre_fiction = df_books['Genre'] == 'Fiction'

print(f'Año superior a 2016 y de genero de ficción: \n {df_books[genre_fiction & older_than]}')

print(f'Año inferior a 2016: \n {df_books[~older_than]}')