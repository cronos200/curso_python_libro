# 1. Mensaje personal: Use una variable para representar el nombre de
# una persona e imprima un mensaje para esa persona. El mensaje debería ser
# sencillo, por ejemplo: "Hola, Eric, ¿te gustaría aprender Python hoy?".
nombre = 'jhon jairo'
mensaje = f'Hola {nombre}, ¿te gustaría aprender Python hoy?'
print(mensaje)
print('--------------------------------------------')

# 2.Grafía de nombres: Use una variable para representar el nombre de
# una persona e imprima ese nombre en minúsculas, mayúsculas y con
# mayúscula inicial.
Mayuscula_nombre = nombre.upper()
print(f'Nombre en mayuscula --> {Mayuscula_nombre}')
minuscula_nombre = nombre.lower()
print(f'Nombre en minuscula --> {minuscula_nombre}')
nombre_mayu_inicial = nombre.title()
print(f'Nombre con la primera letra en mayuscula --> {nombre_mayu_inicial}')
print('--------------------------------------------')

# 3.Cita célebre: Busque una cita de un personaje al que admire. Imprima
# la cita y el nombre del autor. La salida debería tener un aspecto similar a
# esto, incluidas las comillas:
# Albert Einstein once said, "A person who never made a mistake never
# tried anything new."
nombre_autor = 'Albert Einstein'
cita_autor ="""Plantear nuevas preguntas, nuevas posibilidades, considerar los viejos \nproblemas desde un nuevo ángulo, requiere imaginación creativa y marca un avance real en la ciencia."""
print(f'El celebre {nombre_autor} dejo estas palabras: \n"{cita_autor}"')
print('--------------------------------------------')

# 4.Cita célebre 2: Repita el ejercicio 2-5, pero, esta vez, represente el
# nombre de la persona usando una variable llamada famous_person. Después,
# componga el mensaje y represéntelo con una nueva variable llamada
# message. Imprima su mensaje.
famous_person = nombre_autor
message = cita_autor
print(f'El celebre {famous_person} dejo estas palabras: \n"{message}"')
print('--------------------------------------------')

# 5.Eliminar espacios de nombres: Use una variable para representar
# el nombre de una persona e incluya algunos caracteres de espacio en blanco
# al principio y al final del nombre. Asegúrese de usar cada combinación de
# caracteres, "\t" y "\n", al menos una vez. Imprima el nombre una vez, de
# modo que se muestren los espacios de alrededor.
# A continuación, imprima el nombre usando cada una de las tres funciones
# que hemos visto: lstrip(), rstrip() y strip().
nombre_5 = '\t\t\tJhon Jairo\n\n\n'
print(nombre_5)
print(nombre_5.lstrip())
print(nombre_5.rstrip())
print(nombre_5.strip())
print('--------------------------------------------')

# 6. Extensiones de archivos: Python cuenta con el método
# removesuffix(), que funciona exactamente igual que el método
# removeprefix(). Asigne el valor 'python_notes.txt' a una variable llamada
# filename. A continuación, utilice el método removesuffix() para mostrar el
# nombre de archivo sin la extensión de archivo, como ocurre con algunos
# exploradores de archivo.
filename = 'python_notes.txt'
filename_suffis = filename.removesuffix('.txt')
print(f'El metodo removesuffix() elimina el sufijo que tiene el nombre del archivo {filename_suffis}')

