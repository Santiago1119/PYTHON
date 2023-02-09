#Las tuplas son uan estructura de datos, se maneja similar a los arreglos pero no son modificables

numbers = (1, 2, 3, 4)
string = ('nico', 'zule', 'santi')
print(numbers)
print(type(numbers))

#Podemos acceder a un valor de la tupla del siguiente modo

print('ultima posición : ', numbers[-1])

#No se pueden agregar más elementos ni modificaciones, solo es una estructura de datos de lectura

#Podemos acceder a la posición del elemento con el método index
print(string)
posicion = string.index('zule')
print(string[posicion])

#Pero a la hora de querer modíficar una tupla podemos transformarla en una lista(arreglo) o podemos crear un arreglo nuevo el cual podrémos modificar

string = list(string)
print(string)
print(type(string))

string = tuple(string)
print(string)
print(type(string))

#-------------------------------------
#Creando una nueva lista a partir de una tupla ya existente

my_list = list(string)
print(my_list)
print(type(my_list))

