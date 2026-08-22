from pwn import *
# Para debug del socket utilizamos:
# context.log_level = 'debug'
# Nos conectamos utilizando remote
con = remote("ic.catedras.linti.unlp.edu.ar", 10001)
# para quitar el texto que no nos interesa (banner),
# leemos hasta justo antes de la cuenta, es decir, hasta ":\n"
con.readuntil("resolver esta cuenta:\n")
# Leemos hasta el salto de línea, la cuenta deseada
cuenta = con.readline()
print(type(cuenta))
print(cuenta)
# Pasamos los bytes a string, para poder realizar la cuenta
cuenta = cuenta.decode()
# Ahora toca resolver la operación
#resultado = str(eval(cuenta))
# No nos tentemos de usar eval para resolver la operación, es muy poderoso pero
# también peligroso si aceptamos y evaluamos cadenas que provienen de una fuente
# que no es de confianza. Por ejemplo si recibimos el string "2+3", eval lo
# convertirá en una expresión y la ejecutará devolviendo el resultado correcto,
# pero si recibimos "__import__('os').system(...)" eval también la ejecutará,
# logrando así el atacante lanzar comandos en nuestro sistema operativo.
# Para evitar usar eval podríamos parsear la información.
# Split convierte una cadena de texto en una lista, utilizando como separador los
# espacios en blanco
cuenta = cuenta.split() # ['297', '+', '155']
# Convierto a entero los operandos
op1 = int(cuenta[0])
op2 = int(cuenta[2])
operador = cuenta[1]
# Sumo multiplico o resto según el operador
if operador == '+':
    resultado = op1 + op2
elif operador == '*':
    resultado = op1 * op2
else:
    resultado = op1 - op2
# Enviamos la respuesta de la cuenta, como bytes:
con.send((str(resultado) + "\n").encode())
# Imprimimos toda la respuesta del servidor
print(con.readall())