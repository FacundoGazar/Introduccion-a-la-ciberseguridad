# Práctica 1 - Ciberseguridad

## Ejercicio 6

Resolver el reto alojado en el puerto 11006 del sitio ic.catedras.linti.unlp.edu.ar

Hago:

    telnet ic.catedras.linti.unlp.edu.ar 11006

y me devuelve:

	 Bienvenidos! Tienen un segundo para mandarme el hash MD5 (32 caracteres) de la siguiente palabra:
                                                         loveme
                                                               Mmmm tardaste mucho amiguito

Siempre me pide hacer el MD5 de una palabra.

Hice este código para mandarle el MD5 de la palabra:

```Python
from  pwn  import  *
import  hashlib

con  =  remote("ic.catedras.linti.unlp.edu.ar", 11006)
con.readuntil("Tienen un segundo para mandarme el hash MD5 (32 caracteres) de la siguiente palabra:\n")

palabra  =  con.readline().strip() # No hace falta el decode porque hashlib funciona con bytes

palabra_md5  =  hashlib.md5(palabra).hexdigest()

con.send(palabra_md5) # Ya es un string pq le hicimos el hexdigest

print(con.readall())
```
Respuesta del servidor: 
> b'Correcto! la flag es IC{4gu4nt44444444444hhhhh_cr4ck3r!}'