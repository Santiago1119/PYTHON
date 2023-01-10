text = "Ella sabe Python"

#Una forma de acceder al último valor de un string
size = len(text)
print('size: ',size)
print(text[size - 1])

#Una forma más óptima de acceder al ultimo valor de un string
print(text[-1])

#con slice podemos dividir un string en las partes que necesitemos
print(text[0:5])
print(text[10:16])
#Si no le pasamos primer parametro lo toma desde el principio, igual si no le pasas nada de ultimo parametro
print(text[:10])
print(text[5:])
#tambien podemos darle saltos en los que seleccionará
print(text[:15:2])

