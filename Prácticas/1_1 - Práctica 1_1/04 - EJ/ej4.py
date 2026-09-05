from pwn import *

def rot(n, frase):
    from string import ascii_lowercase as lc # Solo usa minusculas

    tabla = str.maketrans(lc, lc[n:] + lc[:n]) # Creamos la tabla indicando el intercambio de letras
    return frase.translate(tabla) # Usamos esa tabla aplicando el translate

con = remote("ic.catedras.linti.unlp.edu.ar", 11004)

con.readuntil("Bienvenidos! Tienen un segundo para realizar el ROT ")

linea = con.readline() # Aca leemos el n del ROT
n = linea.decode().strip()[0] # Como la linea seguía vamos a tomar solamente la pos del n

frase = con.readline().decode().rstrip("\n") # Leemos la frase y le sacamos el \n

frase_rot = rot(int(n), frase)

con.send(str(frase_rot + "\n").encode())

print(con.readall())