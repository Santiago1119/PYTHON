# -*- coding: utf-8 -*-
"""
funciona igual que list_comprehension

zip hace una unión entre una lista y otra (retorna una tupla)

"""

import random

dictionary = {}

for i in range(1, 11):
    dictionary[i] = i * 2
    
# print(dictionary)

dictionary_v2 = {i: i * 2 for i in range(1, 11)}
# print(dictionary_v2)

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
    
# print(population)

population_v2 = { country: random.randint(1, 100) for country in countries}

# print(population_v2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)