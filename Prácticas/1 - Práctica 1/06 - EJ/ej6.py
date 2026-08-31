from pwn import *
import hashlib

con = remote("ic.catedras.linti.unlp.edu.ar", 11006)

con.readuntil("Tienen un segundo para mandarme el hash MD5 (32 caracteres) de la siguiente palabra:\n")

palabra = con.readline().strip() # No hace falta el decode porque hashlib funciona con bytes

palabra_md5 = hashlib.md5(palabra).hexdigest()

con.send(palabra_md5) # Ya es un string pq le hicimos el hexdigest

print(con.readall())