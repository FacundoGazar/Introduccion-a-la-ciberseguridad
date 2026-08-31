from pwn import *

con = remote("ic.catedras.linti.unlp.edu.ar", 11015)

con.readuntil("como pista le damos que la primer palabra es:\n")

pista = bytes(con.readline().strip())

print(type(pista))
print(pista)

hexstring = con.readline().strip()
texto_bytes = bytes.fromhex(hexstring) # Pasamos hexa a bytes para hacer XOR

key = bytes([texto_bytes[i] ^ pista[i] for i in range(4)]) # Hacemos el XOR para obtener la key

descifrado = bytes([b ^ key[i % 4] for i, b in enumerate(texto_bytes)])

print(descifrado)

con.send(descifrado.decode() + "\n")

print(con.readall())