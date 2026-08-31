from pwn import *
import hashlib

def buscar_pass(primeras_cien, hash_server):
    for password in primeras_cien:
        # La hasheo y hago hexdigest para compararla con el hash del server
        pass_hasheada = hashlib.sha256(password.encode()).hexdigest()

        if pass_hasheada == hash_server:
            return password

primeras_cien = []

with open("rockyou.txt", "r", encoding="utf-8") as f:
    for _ in range(100): # Leemos solamente las primeras 100 como decia la pista
        primeras_cien.append(f.readline().strip()) 

con = remote("ic.catedras.linti.unlp.edu.ar", 11007)

con.readuntil("primeras 100 del diccionario rockyou.txt):\n")

hash_server = con.readline().decode().strip() # Leemos el hash que nos envió el server

con.send(buscar_pass(primeras_cien, hash_server) + "\n")

print(con.readall())