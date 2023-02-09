#CRUD EN PYTHON
#CREAR:
numbers = [1, 2, 3, 4, 5]


#LEER
print(numbers[1])


#ACTUALIZAR
numbers[-1] = 10
print(numbers)


#Para agregar un elemento al final de la lista utilizamos append
numbers.append(700)
print(numbers)


#Utilizamos insert para especificar una posición de creación y un elemento a crear
numbers.insert(0, 'hola')
print(numbers)


#podemos sumar listas a otras listas
tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)


#podemos preguntar la posición de un elemento en específico
index = new_list.index('todo 2')
new_list[index] = 'holaDos'
print(new_list)


#podemos eliminar un elemento en específico de una lista
new_list.remove('todo 1')
print(new_list)


#podemos eliminar el ultimo elemento de una lista con pop o tambien podemos específicarle una posición en específico
new_list.pop()
print(new_list)

#podemos voltear una lista
new_list.reverse()
print(new_list)

#podemos ordenar todo en orden numérico o alfabetico con sort pero no las dos al tiempo

string = ["re", "ab", "eb"]
string.sort()
print(string)
