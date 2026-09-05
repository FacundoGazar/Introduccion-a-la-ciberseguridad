from pwn import *
from sympy import factorint

con = remote("ic.catedras.linti.unlp.edu.ar", 11017)
con.readuntil("Intente desencriptar el siguiente texto:\n")

# Solamente nos interesan los numeros, los decodeamos y pasamos a int
n = int(con.readline().strip().split()[1].decode())
e = int(con.readline().strip().split()[1].decode())
c = int(con.readline().strip().split()[1].decode())

print(n)
print(e)
print(c)

p, q = factorint(n).keys()

phi = ((p - 1) * (q - 1)) # Sabiendo p y q sacamos phi(n)

d = pow(e, -1, phi) # Ahora con phi(n) sacamos d

mensaje = pow(c, d, n)
mensaje = mensaje.to_bytes((mensaje.bit_length() + 7) // 8, byteorder="big")

con.send(mensaje)

print(con.readall())