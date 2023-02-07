# -*- coding: utf-8 -*-

"""
Cuando un archivo no tenga header se lo puedo especificar con la propiedad header="None"
Y tomará todos los datos de archivo como elementos de dataframe, en este caso los titulos
Estan en la posición 0, tambien puedo predefinir los nombres de las columnas con el atributo
names= y la lista con los nombres de los atributos que quiero colocar

"""


import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', header=0, names=['Namess', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Gender'])

print(df_books)
print(df_books.columns)

df_json = pd.read_json('hpcharactersdataraw_3d934e85-dfa4-42ec-8520-fadfbecae574.json')

print(df_json)