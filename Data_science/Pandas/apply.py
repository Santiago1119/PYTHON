# -*- coding: utf-8 -*-
"""
Apply nos sirve para aplicar funciones que nosotros creemos sobre los elementos de las columnas de un dataframe
tambien se pueden aplicar funciones de tipo lambda dentro de apply



"""

import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)

def two_times(value):
    return value * 2

df_books['Rating Two'] = df_books['User Rating'].apply(two_times)

print(df_books['Rating Two'])

df_books['Rating Two'] = df_books.apply(lambda x : x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1)

print(df_books['Rating Two'])
