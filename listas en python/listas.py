animales = ['perro', 'gato', 'conejo', 'cabra', 'conejo', 'caballo']
print(animales) # se imprime la lista de animales en el mismo formato
print(animales[3]) # se imprime el elemento en la posición 3 (cabra)
print(animales[1].upper())  # se imprime el elemento en la posicion 1 (gato) y con el metodo upper() lo covertimos a mayuscula como lo vimos en los atiriores capitulos
print(animales[1:6:2])

frutas = ['manzana', 'banana', 'naranja', 'uva', 'pera', 'mandarina', 'coco']
frutas_preferidas = f'Estas son mis frutas favoritas: {', '.join(frutas[0:3])}'
print(frutas_preferidas)

# #Ejercicios
# 3-1. Nombres: Guarde los nombres de unos cuantos amigos en una lista llamada nombres. Imprima el nombre de cada persona accediendo al elemento correspondiente de la lista, de uno en uno.
# 3-2. Saludos: Empiece con la lista del ejercicio 3-1, pero, en vez de solo
# imprimir el nombre de cada persona, imprímales un mensaje. El texto debería
# ser el mismo, pero cada mensaje debería personalizarse e incluir el nombre
# de la persona.
nombres = ['Ana', 'Carlos', 'David', 'Elena', 'Fernando']
for nombre in nombres:
    print(f'Hola como estas {nombre.upper()}?')

print('-----------------------------------------------------------------------')


# 3-3. Su propia lista: Piense en su medio de transporte favorito, como la
# moto o el coche, y haga una lista que incluya varios ejemplos. Use la lista
# para imprimir una serie de frases sobre esos elementos, como "Me gustaría
# tener una moto Honda".

motos = ['Honda', 'Yamaha', 'Harley-Davidson', 'Kawasaki', 'Suzuki']
print(f'Lista de motos original --> {motos}')
motos[1] = 'AKT'
print(f'Lista de motos modificadas en la posición 1 --> {motos}')
for moto in motos:
    print(f'Me gustaría tener una moto {moto}')