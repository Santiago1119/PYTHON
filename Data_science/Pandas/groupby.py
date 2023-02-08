# -*- coding: utf-8 -*-
"""
Groupby nos sirve para poder agrupar datos y saber algo en especifico de los
mismos, como cuanto da la suma de todos o su promedio, y para esto especificamos
una columna por la cual los querramos agrupar y después de especificar la columna 
especificamos que operación debemos realizar con los datos, puede ser contarlos, sumarlo etc...
(SOLO ES POSIBLE CON FUNCIONES DE AGREGACIÓN)

Al aplicar un groupby la columna por la cual agruparemos se convierte en el indice del dataframe
y podremos acceder a una fila en especifico por la columna que se realizo el agrupamiento con los
datos realizados en el groupby

Si queremos resetear los indices para acceder a las filas por medio de números lo podemos hacer
con el atributo "reset.index()" y en este caso la columna por la cual se filtro pasa a ser parte de
las columnas del dataframe y los nuevos indices seran por defecto (numeros)

Con la función agg podemos especificarle más de una función de agregación, las cuales se aplicaran al
dataframe

"""
import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv', sep=',', header=0)


print(df_books.groupby('Author').sum())

print(df_books.groupby('Author').sum().reset_index())

print(df_books.groupby('Author').sum().loc['Abraham Verghese'])

print(df_books.groupby('Author').sum().agg({'Reviews':['min', 'max'], 'User Rating': 'sum'}))


