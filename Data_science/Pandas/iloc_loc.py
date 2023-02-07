# -*- coding: utf-8 -*-

"""
Puedo hacer slicing de un dataframe y este me retornará las filas del dataframe

Si quiero filtrar por una columna solo es necesario que ponga el nombre de la columna
Entre corchetes cuadrados, pero si quiero filtrar por dos o más columnas tengo que poner
dos corchetes cuadrados para que no genere error

Para filtrar por filas utilizamos loc, con loc podemos hacer un slicing y retornará desde la posicion inicial
hasta la posición final, sin excluir ninguna, tambien podemos especificarle de que "label" (columna)
queremos los datos de esas filas, tambien podemos realizar la misma operación a todos los elementos de una columna

Para filtrar por filas y columnas de forma mas sencilla que con LOC utilizamos ILOC, del mismo modo que con loc,
pero no tendremos que especificar el nombre de las columnas, solo sus indices, en el caso de ILOC este excluye el límite superior

"""

import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)

print(f'Filtrando 4 filas de un dataframe: \n {df_books[0:4]}')
print(f'Filtrando una columna de un dataframe: \n {df_books["Name"]}')
print(f'Filtrando varias columnas de un dataframe: \n {df_books[["Name", "Author"]]}')
print(f'Filtrando varias filas con LOC: \n {df_books.loc[0:4]}')
print(f'filtrando varias filas con LOC y LABELS(COLUMNAS): \n {df_books.loc[0:4, ["Name", "Author"]]}')
print(f'operando con una columna de un dataframe: \n {df_books.loc[:, ["Reviews"]]* -1}')
print(f'validando que sea de un autor : \n {df_books.loc[:, ["Author"]] == "JJ Smith"}')
print(f'Filtrando con ILOC: \n {df_books.iloc[0:3, 0:3]}')