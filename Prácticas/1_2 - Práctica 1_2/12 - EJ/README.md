
# Práctica 1_2 - Ciberseguridad

## Ejercicio 12

Revele el mensaje cifrado con RSA:
>p=1411681044962247700471424630708374925648758544093881877
q=1025477764739116170232001755962926569489838949121232767
e=65537
C=244800329353906336350382253088680972646706962639783844335948234085022348400763256559770095538177770365047075

## Solución

Para descifrar un mensaje en RSA tenemos que hacer un:
> M = C ^ d mod n

Pero primero necesitamos *d* y *n*. Por suerte en el ejercicio ya nos dan *p*, *q*, *e* y *C*. Con esos datos ya podemos obtener lo que necesitamos.

> n = p x q
> d = inverso modular de e mod phi(n)
> phi(n) = (p - 1) x (q - 1) <- eso seria muy complejo computacionalmente de calcular sin saber p y q

Con ese planteo sólo quedaría codear en python un script para que calcule todo y traduzca el resultado en un string.
```Python
p=1411681044962247700471424630708374925648758544093881877
q=1025477764739116170232001755962926569489838949121232767
e=65537
C=244800329353906336350382253088680972646706962639783844335948234085022348400763256559770095538177770365047075

n  =  p  *  q
phi  = ((p  -  1) * (q  -  1))
d  =  pow(e, -1, phi)

mensaje  =  pow(C, d, n)
mensaje  =  mensaje.to_bytes((mensaje.bit_length() +  7) //8, byteorder="big")

print(mensaje.decode())
```
## Flag: IC{sabiendo_P_y_Q_es_muy_facil}