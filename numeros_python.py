# 1.Número ocho: Escriba operaciones de suma, resta, multiplicación y
# división que den como resultado el número 8. Asegúrese de incluir sus
# operaciones en llamadas a print() para ver los resultados. Debería crear
# cuatro líneas con este aspecto:
# Suma: 5 + 2 + 1 = 8
num_suma1, num_suma2, num_suma3 = 5, 2, 1
print(f'La suma de los numeros es: {num_suma1 + num_suma2 + num_suma3}')
# Resta: 10 - 1 - 1 = 8
num_resta1, num_resta2, num_resta3 = 10, 1, 1
print(f'La resta de los numeros es: {num_resta1 - num_resta2 - num_resta3}')
# Multiplicación: 2 * 2 * 2 = 8
num_mult1, num_mult2, num_mult3 = 2, 2, 2
print(f'La multiplicacion de los numeros es: {num_mult1 * num_mult2 * num_mult3}')
# División: 16 / 2 / 1 = 8
num_div1, num_div2, num_div3 = 16, 2, 1
print(f'La division de los numeros es: {num_div1 / num_div2 / num_div3}')
print('------------------------------------------------------------')


# 2.Número favorito: Use una variable para representar su número
# favorito. A continuación, usando esa variable, cree el mensaje que revele su
# número favorito e imprímalo.

# Asigno mi variable de número favorito a una variable. Luego, en la variable numero_pedido, le pido al usuario que introduzca un número mediante el método input(), el cual sirve para recibir cualquier número o carácter que el usuario introduzca. El int() antes del input() sirve para castear (cambiar un valor string a un valor int).
# Se declara el bucle while con una condición: mientras numero_pedido no sea igual a 31, el programa entrega un mensaje de "número inválido" y solicita nuevamente que introduzca un número. Esto se repetirá hasta que el usuario acierte con el número favorito. Cuando esto ocurra, se ejecuta una condicional donde, si numero_pedido es igual a numero_favorito, se arroja un mensaje que felicita al usuario por encontrar el número favorito.
numero_favorito = 31
numero_pedido = int(input('Introduce el numero que creas que es mi favorito: '))
while numero_pedido != 31:
    print('El numero que selecionaste no es mi numero favorito: ')
    numero_pedido = int(input('Introduce el numero que creas que es mi favorito: '))
    if numero_pedido == 31:
        print(f'El numero que selecionaste {numero_pedido} es mi numero favorito felicitaciones')