from pwn import *

con = remote("ic.catedras.linti.unlp.edu.ar", 11018)
con.readuntil("compartida por Diffie Hellman:\n")

p = int(con.readline().split()[1].decode())
g = con.readline().split() # Leo la linea para pasar a la siguiente pero no necesitamos a g
public_alice = int(con.readline().split()[1].decode())
private_bob = int(con.readline().split()[1].decode())

print(p)
print(public_alice)
print(private_bob)

clave_compartida = pow(public_alice, private_bob, p)

con.send(str(clave_compartida) + "\n")

print(con.readall())