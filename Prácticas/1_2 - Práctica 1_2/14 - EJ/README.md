
# Práctica 1_2 - Ciberseguridad

## Ejercicio 14

Revele el mensaje cifrado con RSA, esta vez no tenemos P ni Q. Pista: Hay que factorizar o encontrar un buen lugar donde lo hagan…

> n:1452449184624535635757449085988204487494222248509493899299759
e: 65537 
C:1280743944712857143060627969938538851911171950125979945026152

## Solución

Busqué en factordb.com si alguien ya habia factorizado ese número. Me devolvió lo siguiente:

> n = 1153324775179431312178120797679 * 1259358348907893108175391571521

Es decir, me devolvió p y q. Con eso ya podemos calcular todo.

```Python
n  =  1452449184624535635757449085988204487494222248509493899299759
e  =  65537
c  =  1280743944712857143060627969938538851911171950125979945026152
p  =  1153324775179431312178120797679
q  =  1259358348907893108175391571521

phi  = (p  -  1) * (q  -  1)
d  =  pow(e, -1, phi)  

mensaje  =  pow(c, d, n)
mensaje  =  mensaje.to_bytes((mensaje.bit_length() +  7) //  8, byteorder="big")

print(mensaje.decode())
```

## Flag: IC{factordb_ftw}