mensaje_original = 'Hola mundo de la programación'
print(f'Mensaje original: {mensaje_original}')
mensaje_original = 'SQL bases de datos'
print(f'Mensaje modificado y todo en mayuscula por el \n\tmétodo upper(): {mensaje_original.upper()}')
print(f'Se usa el metodo title() para que cada letra del mensaje sea mayúscula: {mensaje_original.title()}')

print('--------------------------------------------')

espacios_basios = 'Python '
print(f'Espacios basios al final: {espacios_basios}')
solucion =espacios_basios.rstrip()
print(f'eliminamos espacios basios al final con el metodo strip(): {solucion}')


print('--------------------------------------------')

# Eliminacion de prefijos
url = 'https://www.python.org'
print(f'Con prefijo: { url}')
sin_prefijo = url.removeprefix('https://')
print(f'se elimino el prefijo https:// y quedo --> { sin_prefijo}')