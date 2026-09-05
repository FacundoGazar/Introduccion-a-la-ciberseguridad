# Práctica 1 - Ciberseguridad

## Ejercicio 10

Cifrado XOR El siguiente es el resultado de cifrar un string utilizando XOR y codificando luego la salida en hex. El cifrado XOR utilizó una clave de 1 byte (1 carácter). Programar un script para encontrar la clave utilizada y develar el mensaje original. 
- Pista: Usar fuerza bruta para probar todas las posibles claves.

> 193877243277343e31253677343839770f18056c773b3677313b363077333277322423327725322338773224771e142c0666333613380834673908220d6325082f6725762a

## Solucion:

```Python
cifrado_hexa  =  "193877243277343e31253677343839770f18056c773b3677313b363077333277322423327725322338773224771e142c0666333613380834673908220d6325082f6725762a"
cifrado_bytes  =  bytes.fromhex(cifrado_hexa) # Lo pasamos a bytes para hacer el xor

for  key  in  range(256):
	descifrado  =  bytes([b  ^  key  for  b  in  cifrado_bytes])  
	try:
		texto  =  descifrado.decode('utf-8')
		if  'IC'  in  texto  and  texto.isprintable():
		print(f"Mensaje: {texto}\n")
	except  UnicodeDecodeError:
		continue
```

Flag: IC{Q1daDo_c0n_uZ4r_x0r!}