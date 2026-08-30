# Práctica 1 - Ciberseguridad

## Ejercicio 5

> Averigue el mensaje al que se le aplicó la función de hash para generar los siguientes resúmenes: 
> Pista: Deduzca la función de hash a partir del formato (longitud) del resumen o hash. Submitear con IC{}

- 63a9f0ea7bb98050796b649e85481845
	- Como tiene 32 caracteres intuí que era MD5. Le hice el lookup y me devolvió "root"
- 1ae49b084c84a479e2a05be693fe7625d861007d
	- Busqué qué hash devuelve un resumen de 40 caracteres y es SHA-1. Le hice lookup y me devolvió "P4$sw0Rd"
- 796DD619207C4E357FD432FDF962C958BA1DF4CD6785246937223BC8DC4FBF01794EBFF0159A175D9BE65B8EA4E7F46B80CCFFA4ED2A21773D358C523DDDD382
	- Busqué qué hash devuelve un resumen de 128 caracteres y es SHA-512. Le hice lookup y me devolvió "!!!gotosleep!!!