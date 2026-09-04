
# Práctica 1_2 - Ciberseguridad

## Ejercicio 13

Resolver el reto alojado en el puerto 11012 del sitio ic.catedras.linti.unlp.edu.ar

## Solución

Cuando nos conectamos al reto, nos responde esto:
> Bienvenidos! Intente desencriptar el siguiente texto:
             p=40725388636704146708901285915535935367861928658369537192137462386253998280434057
                                                                                                q=41473570330844245109494691507507618336494717937813001220688787318868537850244569
                                                           e=65537
                                                                   c=340537277112296493976532986316069068825837077983634694833848998931824354804483231957363674299331093665789885016532252737289524676010253887313831849066380624371

Cada vez que nos conectamos cambian los datos. Voy a usar pwntools para leer los datos y calcular rapidamente lo solicitado.

```Python
from  pwn  import  *

con  =  remote("ic.catedras.linti.unlp.edu.ar", 11012)
con.readuntil("Intente desencriptar el siguiente texto:\n")

p  =  int(con.readline().decode().strip().split()[1])
q  =  int(con.readline().decode().strip().split()[1])
e  =  int(con.readline().decode().strip().split()[1])
c  =  int(con.readline().decode().strip().split()[1])

n  =  p  *  q
phi  = ((p  -  1) * (q  -  1))
d  =  pow(e, -1, phi)

mensaje  =  pow(c, d, n)
mensaje  =  mensaje.to_bytes((mensaje.bit_length() +  7) //8, byteorder="big")

con.send(mensaje.decode() +  "\n")
print(con.readall())
```

## Flag: IC{rsa_4_aaaall}