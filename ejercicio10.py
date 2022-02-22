from decimal import MIN_EMIN
from http.client import INSUFFICIENT_STORAGE
from re import I
from readline import replace_history_item
from socket import VMADDR_CID_HOST
from tkinter import N, Variable
from unicodedata import name
from xml.sax.handler import EntityResolver
from pkg_resources import NullProvider, PkgResourcesDeprecationWarning


Clase Persona 
    id: ENTERO 
    edad: ENTERO 
    identidad: IDENTIDAD 

    padre: ENTERO 
    madre: ENTERO 
fin Persona 

#Lista de personas entre 20 y 30 años
Algoritmo:
    Constantes:
    familias: TABLA[Persona]
    edad_MIN: ENTERO 
    edad_MAX: ENTERO 

    Resultado: TABLA [1,500]

    Precondicion:
        familias  ≠ NULO 
        edad_MIN ≠ NULO
        edad_MAX ≠ NULO
    
    Constantes
        MIN: ENTERO <- indice_min (familias)
        MAX: ENTERO <- indice_max (familias)
        MIN_EDADES: ENTERO <- indice_min(resultado)
        MAX_EDAES: ENTERO <- indice_max (resultado)
        INFINITO: ENTERO <- ENTERO_MIN
        HUÉRFANO: ENTERO <- INFINITO
        BORRADO: ENTERO <- HUERFANO + 1
        VACIO:ENTERO <-  HUERFANO +2

    Variable
        i: ENTERO 
        j: ENTERO 
    
    Inicialización 
    i: MIN 
    j: MIN_EDADES 
    Resultado [MIN_EDADES] <-  VACIO
    afirmación 
    i > MIN Y j > MIN_EDADES => 
    Las celdas de sub_tabla(Resultado, MIN_EDADES, j - 1)
    se inicializan con los identificadores de las celdas de sub_tabla (familias, MIN,i- 1)
    donde los identificadores no son ni BORRADO ni VACIO y la edad está entre edad_MIN y edad_MAX 

    Realización 
    hasta que 
        familias[i].id = VACIO 
        o si no i > MAX
        invariante 
            ???
        variante de control
            MAX - i+1
        
    repetir 
        si 
            familias[i].identificador ≠ BORRADO 
          y entonces 
            edad_MIN <= familias[i].edad<= edad_MAX
        entonces
            Resultado[j] <- familias [i].id
            j <- j + 1
        fin si 
        i <- i +1
    fin repetir 

    postcondición
    #Resultado está VACIO cuando los límites de edad no están en orden
    edad_MIN> edad_MAX => Resultado[1] = VACIO
    (∀ k ∊ Z) (
        indice_min(Resultado)<=k<=indice_max(Resultado) =>
        Resultado[k]es el identificador de una persona de edad entre edad_MIN y edad_MAX
    )
fin edades 

#Envejecer a todas las personas registradas
Algoritmo:
    Entrada 
        familias: TABLA[Persona]

    Precondicion 
        familias ≠ NULO 

    Constante 
        MIN: ENTERO <- indice_min (familias)
        MAX: ENTERO <- indice_max (familias)
        INFINITO: ENTERO <- ENTERO_MIN
        HUÉRFANO: ENTERO <- INFINITO
        BORRADO: ENTERO <- HUERFANO + 1
        VACIO:ENTERO <-  HUERFANO +2

    Variable
        i: ENTERO 

    Inicializacion
        i <- MIN 

    Realizacion 
        hasta que 
            familias[i].id = VACIO 
          o si no 
            i > MAX
            invariante
                ???
            variante de control 
                MAX - i + 1
        repetir 
            si 
                familias.[i].id ≠ BORRADO
            entonces 

                familias[i].edad <- familias[i].edad + 1
            fin si
            i <- i +1 
        fin repetir 

        Postcondicion 
        Se han incrementado todos los atributos edad a las celdas no VACIO y no BORRADO

#Lista de personas huérfanas menores de 15 años 
Algoritmo
    Entrada 
    familias: TABLA[Persona]
    Resulatado: TABLA [ENTERO][1,500]

    Precondicion 
    familias ≠ NULO 

    Constantes
        MIN: ENTERO <- indice_min (familias)
        MAX: ENTERO <- indice_max (familias)
        MIN_HUERF: ENTERO <- indice_min(resultado)
        MAX_HUERF: ENTERO <- indice_max (resultado)
        INFINITO: ENTERO <- ENTERO_MIN
        HUÉRFANO: ENTERO <- INFINITO
        BORRADO: ENTERO <- HUERFANO + 1
        VACIO:ENTERO <-  HUERFANO +2

    Variable
    i: ENTERO 
    j:ENTERO 

    Inicializacion 
    i <-MIN 
    j <- MIN_HUERF
    resultado [j] <- VACIO 

    Realizacion 
    hasta que 
        familias [i].id = VACIO 
    o si no 
        i > MAX 

        invariante 
            ???
        variante de control 
            MAX - i +1

    repetir 
        si 
            familias[i].id ≠ BORRADO
        y entonces 

            (familias[i].padre = HUERFANO
            o
            familias[i].madre = HUERFANO)
        entonces 
            Resultado[j] <- familias[i].id
        fin si 
        i <- i +1

    fin huerfanos 