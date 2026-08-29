# Práctica 1 - Ciberseguridad

## Ejercicio 3

> Revele los siguientes mensajes. Para cada uno, indique qué cifrado se utilizó y si es de transposición o sustitución. Puede utilizar el sitio http://rumkin.com/tools/cipher/

- }r4tnelac_a_0dnazepmE{CI
	- Este mensaje fue sencillo de revelar porque se nota que está escrito al revés. Nosotros siempre usamos una flag que dice IC{xxx} y acá se ve como CI es lo último. Simplemente lo leí al revés: IC{Empezand0_a_calent4r}. Se trata de un cifrado de transposición.

- DX{ZNO0 NZ zhKdzuv v Xjhkg1xvM}
	- Intuyo que es cifrado césar con un offset arbitrario. Como no se dijo que la flag estaba distinta entonces cuento el offset para que la D sea la I (5). Se trata de un cifrado de sustitución: La flag es: IC{EST0 SE emPieza a Compl1caR} 

- pp epnwfus dvjipèym jx ln dtjcefv jfxrhw rq hkmmwjetfd wpvkla ij teznfxgymx t ceuced hgs knkielb féwcy ntwdaoos pwvva hfiekghvgz csf kacwe, wpctiif kejyd hg cqljeèrf, byp wg baf hfqw poexl. mq hzfslhz hg cqljeèvm rv yp jqkwrdp oi dyuaqyztmóv flqrsm utcibwjlfévpkt. rlc jvhr! nh nqfx et tg{g1k3plz3_wzc3w} . arjyí czí! Pista: passphrase:le chiffre indechiffrable
	- La pista dice algo en italiano asi que se me vino a la mente probar el cifrado vigenere. Uso la passphrase como la key.  el cifrado vigenère es un cifrado basado en diferentes series de caracteres o letras del cifrado césar formando estos caracteres una tabla, llamada tabla de vigenère, que se usa como clave. el cifrado de vigenère es un cifrado de **sustitución** simple polialfabético. muy bien! la flag es ic{v1g3ner3_rul3s} . seguí así! Se trata de un cifrado de sustitución como bien dice el mensaje.

- Militar exfiltration. An unauthorized encoded message was sent this morning. This may be very dangerous. Based on previous SIGINT our cryptographers have been told that to read it "a rail fence is needed". Can you help us read the message? TSaeile nh umrnrwl ev tnoebi laao
	- En el texto dice "a rail fence is needed" así que eso nos da una pista de que se tiene que usar rail fence cipher. Pego el texto en una tool que permite descifrar, marco que uso 3 railes y ya nos da la flag: The Submariner will leave at noon. Se trata de un cifrado de transposición.