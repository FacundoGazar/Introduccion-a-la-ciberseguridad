from pwn import *

con = remote("ic.catedras.linti.unlp.edu.ar", 11012)
con.readuntil("Intente desencriptar el siguiente texto:\n")

p = int(con.readline().decode().strip().split()[1])
q = int(con.readline().decode().strip().split()[1])
e = int(con.readline().decode().strip().split()[1])
c = int(con.readline().decode().strip().split()[1])

n = p * q

phi = ((p - 1) * (q - 1))

d = pow(e, -1, phi)

mensaje = pow(c, d, n)

mensaje = mensaje.to_bytes((mensaje.bit_length() + 7) //8, byteorder="big")

con.send(mensaje.decode() + "\n")

print(con.readall())