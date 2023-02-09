#los string son cadenas de caracteres, los cuales se pueden almacenar dentro de variables e imprimirlas
name = "Santiago"
last_name = "Gonzalez Parra"

print(name)
print(last_name)

#Tambien se pueden almacenar variables dentro de una variable que contenga string como tipo de dato

full_name = name + " " + last_name

print(full_name)

#Tambien cuando se necesiten comillas dobles o simples de deben usar las comprarias para definir el string porque si no lo hacemo python pensará que estamos abriendo y cerrando la cadena de caracteres

entre_comillas = "I'm Santiago"
print(entre_comillas)

entre_comillas_dos = 'she said "Hello"'
print(entre_comillas_dos)


#se le pueden dar formatos a las variables a la hora de imprimirlas con la siguiente sintaxis

template = "Hola, mi nombre es: " + name + " y mi apellido es: " + last_name
print(template)

#Otra forma de realizar esta acción es con la función format, pasandole como parámetros los valores que se desean según la posición de las llaves vacias

template_dos = "Hola, mi nombre es: {} y mi apellido es: {}".format(name,last_name)
print(template_dos)

#Aunque hay una forma de realizar esta acción con mayor eficiencia y facilidad

template_tres = f"Hola, mi nombre es: {name} y mi apellido es: {last_name}"
print(template_tres)
