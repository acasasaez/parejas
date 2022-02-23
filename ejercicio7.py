from xml.sax.handler import EntityResolver
from ejercicio10 import Entrada


Algoritmo cifra: 
    #La cifra que representa el entero n en base < 37
Entrada
    n:ENTERO 

Resultado: CARACTER 

Precondicion
    0<= n <= 36

Constantes 
    cifras: TABLA [CARACTER] [1] <- ["0", "1",...,"9",...,"A",...,"Z"]

Realización 
    Resultado <- cifras [abs(n)]

Postcondicion
    n<10 => Resultado = caracter (codigo("0")+n)
    n>=10 => Resultado = caracter (codigo("A")+n-10)

fin cifra 

Algoritmo conversion2E
    #La representacion de "n" en base "BASE"
Entrada 
    n:ENTERO 
    BASE: ENTERO 

Resultado: CADENA 

Variable 
   dividiendo: ENTERO  <- abs (n) 
   q,r: ENTERO 
        #Generan las series de los cocientes ylos restos ded dividendo por BASE
    k: ENTERO     

Inicializacion 
   Resultado  <- CADENA_VACIA
   k <- 0

Realizacion
    hasta que dividiendo < BASE 
    invariante 
    #(H): la siguiente division a realizar es
    #la de "dividiendo" por "BASE";
    #el resultado parcial es Resultado
    #k es el número de divisiones realizadas 


        dividiendo = abs(n)* BASE**-k 
    variante de control 
        cociente (dividendo, BASE)

    reptir 
        q <- cociente (dividendo, BASE)
        r <- resto (diviendo, BASE)

        afirmacion 
        #(H): la siguiente división a realizr es la 
        #de "q" por "BASE"; el resultado parcial es 
        #Resultado a aumentar de "r" en cifra 
        #El número de divisiones realizadas es k+1

            dividiendo = abs(n)* BASE**-k -1

        Resultado  <- SEPARADOR  ⊕ cadena (cifra(r))
                              ⊕ Resultado 
        afirmacion
        #(H): la siguiente division a realizar es la de q por 
        # por "BASE"; el resultado parcial es 
        #Resultado
        #EL número de divisiones realizadas es k+1

            dividendo = abs(n) * BASE**-k-1
            q = abs(n) * BASE ** -k
        k <- k +1
        dividendo <-q
        afirmacion 
        #(H): la siguiente division a realizar es la 
        #de "dividendo" por "BASE"; el resultado parcial es
        # Resultado  
        #El numero de divisiones efectuadas es k 
            dividiendo = abs(n) * BASE*-K 
    fin repetir 

    #Aumentar Resultado en la ultima cifra...
    Resultado <- cadena(cifra(dividiendo))⊕ Resultado 
    #... y el signo de "n"
    Resultado < - cadena (signo(c(n))) ⊕ Resultado
fin conversion2E 