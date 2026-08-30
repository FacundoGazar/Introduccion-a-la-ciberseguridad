from pwn import *
import base64

con = remote("ic.catedras.linti.unlp.edu.ar", 11002)

con.readuntil("Tienen un segundo para encodear en base64 esta palabra:\n")

linea = con.readline() # Leemos la palabra
linea = linea.decode() # La pasamos a string
palabra = linea.strip().encode() # Le sacamos el \n del final y la encodeamos


print(type(palabra))
print(palabra)

palabra_base64 = base64.b64encode(palabra) # Palabra en base64

print(type(palabra_base64))
print(palabra_base64)

con.send((str(palabra_base64.decode()) + "\n").encode()) # Enviamos la palabra en base64

print(con.readall())