# Práctica 1 - Ciberseguridad

## Ejercicio 8

Crackear usando hashcat o johntheripper el siguiente hash md5 con salt:

> 85f978e2c12fedbf8869b219a1b2576a

- Pista: Formato MD5($salt. $pass) 
- Pista: Usa como salt el prefijo “IntroCiberseguridad” 
- Pista: rockyou.txt

## Solucion:

    john-sse2.exe --format=dynamic_4 --wordlist=rockyou.txt hash.txt
    
    Using default input encoding: UTF-8
    Loaded 1 password hash (dynamic_4 [md5($s.$p) (OSC) 128/128 SSE2 4x3])
    Warning: no OpenMP support for this hash type, consider --fork=4
    Press 'q' or Ctrl-C to abort, almost any other key for status
    welovejesus      (user)
    1g 0:00:00:00 DONE (2026-08-30 22:54) 6.451g/s 4877Kp/s 4877Kc/s 4877KC/s william62..weirdass
    Use the "--show --format=dynamic_4" options to display all of the cracked passwords reliably
    Session completed
