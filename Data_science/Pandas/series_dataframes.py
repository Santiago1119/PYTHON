# -*- coding: utf-8 -*-

"""
Una serie es el mismo concepto de un Vector, podemos especificarle a cada elemento de la serie
Un indice por el cual podrémos acceder al mismo de forma más rapida, si no lo especificamos tomará los indices a partir
de 0 como una lista

Podemos transformar un diccionario de Python en una Serie de Pandas simplemente pasandolo como parámetro
de pd.Series(), tambien se puede hacer slicing con las series de Pandas

A la hora de trabajar con Matrices en Pandas utilizamos los DataFrames, podemos pasarle indices personalizados 
o sino los especificamos estos comienzan desde 0

"""

import pandas as pd

jugadores_psg = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'],
                          index=[1,7,10,30]
                          )

print(jugadores_psg[10])


dictionary = {1:'Navas', 7:'Mbappe', 10:'Neymar', 30:'Messi'}
dictionary = pd.Series(dictionary)
print(dictionary)

diccionario_matriz = {'jugador':['Navas', 'Mbappe', 'Neymar', 'Messi'],
                      'altura':[183.0, 170.0, 170.0, 165.0],
                      'goles':[2, 200, 200, 200]}

df_Players = pd.DataFrame(diccionario_matriz, index=[1,7,10,30])

print(df_Players.index)




