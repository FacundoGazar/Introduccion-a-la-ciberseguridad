from pwn import *

con = remote("ic.catedras.linti.unlp.edu.ar", 10002)

con.readuntil("Bienvenidos! Resuelvan estas sumas para obtener la flag!:\n")

while True:
    try:
        cuenta = con.readline()
        print(type(cuenta))
        print(cuenta) # vemos la cuenta

        cuenta = cuenta.decode() # La pasamos a string

        cuenta = cuenta.split() # La pasamos a lista con cada uno de los elementos de la cuenta

        num_uno = int(cuenta[0]) # Convertimos el primer numero a entero
        op = cuenta[1] # Guardamos el operador
        num_dos = int(cuenta[2]) # Convertimos el segundo numero a entero

        # Según el operador, hago lo que deba hacer.
        if op == "+":
            resultado = num_uno + num_dos
        elif op == "-":
            resultado = num_uno - num_dos
        elif op == "*":
            resultado = num_uno * num_dos
        else:
            resultado = num_uno / num_dos

        con.send((str(resultado) + "\n").encode())

        con.readuntil("Correcto! A resolver!:\n")
    except Exception as e:
        print(e)
        break

print(con.readall())