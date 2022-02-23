## Parejas
Nuestra dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/acasasaez/parejas)
https://github.com/acasasaez/parejas .
En este repositorio resolveremos diferentes ejercicios sobre el capítulo «Estructuras elementales».


# Ejercicio 7: Edición de un número entero
En este ejercicio nos piden escribir un algoritmo iterativo que transforme un número entero n cualquiera en su representación en una base B ≥ 2 cualquiera.
El pseudocódigo es el siguiente:
```
from xml.sax.handler import EntityResolver
from ejercicio10 import Entrada


Algoritmo cifra: 
    #La cifra que representa el entero n en base < 37
    Entrada:
        n:ENTERO 

    Resultado: CARACTER 

    Precondicion:
        0<= n <= 36

    Constantes: 
        cifras: TABLA [CARACTER] [1] <- ["0", "1",...,"9",...,"A",...,"Z"]

    Realización :
        Resultado <- cifras [abs(n)]

    Postcondicion:
        n<10 => Resultado = caracter (codigo("0")+n)
        n>=10 => Resultado = caracter (codigo("A")+n-10)

    fin cifra 

Algoritmo conversion:
    #La representacion de "n" en base "BASE"
    Entrada :
        n:ENTERO 
        BASE: ENTERO 

    Resultado: CADENA 

    Variable: 
        dividiendo: ENTERO  <- abs (n) 
        q,r: ENTERO #Generan las series de los cocientes y los restos del dividendo por BASE
        k: ENTERO     

    Inicializacion: 
        Resultado  <- CADENA_VACIA
        k <- 0

    Realizacion:
        hasta que dividiendo < BASE 
        invariante 
        #(H): la siguiente division a realizar es
        #la de "dividiendo" por "BASE";
        #el resultado parcial es Resultado
        #k es el número de divisiones realizadas 


        dividiendo = abs(n)* BASE**-k 
    variante de control: 
        cociente (dividendo, BASE)

    repetir:
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
    fin de conversion
```

# Ejercicio 8: Análisis de una cadena de caracteres
En este ejercicio nos piden que dada una cadena de caracteres con distintas partes separadas por un carácter separador específico, se quieren separar las distintas partes y situarlas en una tabla de cadenas de caracteres. El pseudocódigo es el siguiente:
```
Algoritmo descomponer:
  # Descompone `ca' en `componentes' en `dimensión' cadenas
  # separadas por `separador'.
    Entrada:
        ca : CADENA # La cadena a descomponer
        separador : CARACTER # El carácter que separa las cadenas
        componentes : TABLA[CADENA] # Los componentes de `ca'
        dimensión : ENTERO # La cantidad de componentes
    Precondición:
        ca ≠ NULO
        separador ≠ NULO
        está_definido(componentes)
    Variable:
        L : ENTERO # La longitud de `ca'
        k : ENTERO # Última ocurrencia del `separador' encontrada
        i : ENTERO # Índice del siguiente componente a registrar
        r : ENTERO # Posición siguiente ocurrencia del `separador'
    Inicialización:
        L ← longitud(ca) # Índice del último carácter
        k ← 0
            # Índice de la última ocurrencia del `separador'
            # encontrada
        i ← 1 # Índice del siguiente componente a registrar
        r ← posición(ca, 1, L)
            # Búsqueda de la primera ocurrencia de `separador'
    mientras que:
        k < L y r ≠ AUSENTE
        invariante: (H)
        variante de control: L - k
        repetir:
            afirmación
                ítem(ca, k) = separador y ítem(ca, r) = separador
                # Se copia la cadena `ca' entre los caracteres
                # de índices k+1 y r-1
                componentes[i] ← sub_cadena(ca, k+1, r-1)
                dimensión ← i
            afirmación
                componer(componentes, 1, i, separador) = sub_cadena(ca, 1, r–1)
                    # componentes[1..i] contiene descomposición de ca[1..r-1]
                dimensión = i
                ítem(ca, k) = separador
                    # es la penúltima ocurrencia de `separador'
                ítem(ca, r) = separador
                    # es la última ocurrencia de `separador'
                #Ajusta la cantidad de componentes
                i ← i+1
            afirmación
                componer(componentes, 1, i-1, separador) = sub_cadena(ca, 1, r–1)
                    # componentes[1..i-1] contiene descomposición de ca[1..r-1]
                dimensión = i-1
                # La última ocurrencia encontrada de `separador' en el índice k
                k ← r
            afirmación
                componer(componentes, 1, i-1, separador) = sub_cadena(ca, 1, k–1)
                    # componentes[1..i-1] contiene descomposición de ca[1..k-1]
                dimensión = i-1
                ítem(ca, k) = separador y ítem(ca, r) = separador
                    # es la última ocurrencia de `separador'
                r ← posición(ca, k+1, L)
            afirmación
                componer(componentes, 1, i-1, separador) = sub_cadena(ca, 1, k–1)
                    # componentes[1..i-1] contiene descomposición de ca[1..k-1]
                dimensión = i-1
                ítem(ca, k) = separador
                r = posición(ca, k+1, L, separador)
        fin mientras que
    si:
        k < L
        entonces:
            afirmación
                r = AUSENTE
                componentes[i] ← sub_cadena(ca, k+1, L)
                dimensión ← i
        fin si
    postcondición:
        # `ca' y `separador' no se modifican
        antiguo(ca) = ca
        antiguo(separador) = separador
        # el tamaño de `componentes' es suficiente
        índice_min(componentes) + dimensión – 1≤ índice_max(componentes)
        # Solo se modifican las `dimensión' primeras celdas de
        # `componentes'
        son_idénticas
            (
            componentes,
            índice_min(componentes) + dimensión,
            índice_max(componentes),
            antiguo(componentes),
            índice_min(componentes) + dimensión,
            índice_max(componentes)
            )
        # `ca' es igual a la composición de las `dimensión' primeras
        # celdas de `componentes'
        ca = componer(
            sub_tabla(
                componentes,
                índice_min(componentes),
                índice_min(componentes) + dimensión – 1
                    ),
            separador
            )
fin descomponer
```

# Ejercicio 9: Búsqueda de palabras en un diccionario
En este ejercicio nos piden dada una tabla de palabras en español. Las palabras se guardan en una tabla llamada diccionario. Se utilizan otras dos tablas para recorrer el diccionario. Para cada palabra, una tabla llamada siguiente da el número de la celda ocupada por la palabra que le sigue en orden alfabético en el diccionario. La tabla anterior también da, para cada palabra, el número de la celda del diccionario que contiene la palabra anterior en orden alfabético. A la primera palabra de la lista ordenada le corresponde un número de celda del anterior igual a índice_min(diccionario) - 1. Igualmente, a la última palabra de la lista ordenada le corresponde un número de celda de la siguiente igual al mismo valor. El pseudocódigo es el siguiente:
```
Algoritmo índice_palabra
    # La primera palabra de `diccionario' que empieza por
    # `inicial'.
    Entrada:
        inicial : CARACTER
            # La inicial a buscar
        diccionario : TABLA[CADENA]
            # Objetivo de la búsqueda
    Resultado : ENTERO
    Precondición:
        es_alfabético(inicial)
        está_definido(diccionario)
    Constante:
        I_MIN : ENTERO ← índice_min(diccionario)
        I_MAX : ENTERO ← índice_max(diccionario)
        AUSENTE : ENTERO ← ???
    Variable:
        i : ENTERO # Índice siguiente celda a observar
    Inicialización:
        i ← I_MIN
        Resultado = AUSENTE # Todavía no se ha encontrado     nada
    Realización:
        mientras que:
            i ≤ I_MAX et Resultado = AUSENTE
            invariante:
                (∀k ∈ Z)(I_MIN ≤ k < i => Resultado = AUSENTE) <=> (∀k ∈ Z)
                (I_MIN ≤ k < i => ítem(diccionario[k], 1) ≠ inicial
            variante de control:
                I_MAX – i + 1
        repetir:
            si:
                ítem(diccionario[i], 1) = inicial
            entonces:
                afirmación:
                    i ≤ I_MAX
                    (∀k ∈ Z)(I_MIN ≤ k < i => Resultado = AUSENTE) et
                    ítem(diccionario[i], 1) = inicial
                    Resultado ← i
                afirmación:
                    i ≤ I_MAX
                    Resultado = i ≠ AUSENTE
                fin si
            i ← i + 1
            afirmación:
                i ≤ I_MAX + 1
                Resultado = i o Resultado = AUSENTE
            fin repetir
    postcondición:
        # AUSENTE si no hay palabra con la inicial `inicial' en
        # sub_tabla(
                        # diccionario,
                        # índice_min(diccionario),
                        # índice_max(diccionario)
                    # )
        Resultado = AUSENTE => (∀k ∈ Z)
            (
            índice_min(diccionario) ≤ k ≤ índice_max(diccionario) =>
            ítem(diccionario[k], 1) ≠ inicial
            )
        # Resultado es el índice de una palabra de inicial `inicial' en
        # sub_tabla(
        # diccionario,
        # índice_min(diccionario),
        # índice_max(diccionario)
        # )
        Resultado ≠ AUSENTE =>
            (
                índice_min(diccionario) ≤ Resultado ≤índice_max(diccionario)
            y
                ítem(diccionario[Resultado], 1) = inicial
            )
fin índice_palabra

tipo PALABRA estructura
    anterior : ENTERO
        # El índice de la palabra que precede a esta palabra
    siguiente : ENTERO
        # El índice de la palabra siguiente
    palabra : CADENA
fin PALABRA
```

# Ejercicicio 10: Representar los miembros de una familia
En este ejercicio nos piden que a partir de una ta habla formada por familias con 1000 componentes numerados desde 1 tenemos que hacer diversas tareas. El pseudocódigo es el siguiente:
```
from decimal import MIN_EMIN
from http.client import INSUFFICIENT_STORAGE
from re import I
from readline import replace_history_item
from socket import VMADDR_CID_HOST
from tkinter import N, Variable
from unicodedata import name
from xml.sax.handler import EntityResolver
from pkg_resources import NullProvider, PkgResourcesDeprecationWarning


Clase Persona:
    id: ENTERO 
    edad: ENTERO 
    identidad: IDENTIDAD 

    padre: ENTERO 
    madre: ENTERO 
fin Persona 

#Lista de personas entre 20 y 30 años
Algoritmo edades:
    Entrada:
        familias: TABLA[Persona]
        edad_MIN: ENTERO 
        edad_MAX: ENTERO 

    Resultado: TABLA [1,500]

    Precondicion:
        familias  ≠ NULO 
        edad_MIN ≠ NULO
        edad_MAX ≠ NULO
    
    Constantes:
        MIN: ENTERO <- indice_min (familias)
        MAX: ENTERO <- indice_max (familias)
        MIN_EDADES: ENTERO <- indice_min(resultado)
        MAX_EDAES: ENTERO <- indice_max (resultado)
        INFINITO: ENTERO <- ENTERO_MIN
        HUÉRFANO: ENTERO <- INFINITO
        BORRADO: ENTERO <- HUERFANO + 1
        VACIO:ENTERO <-  HUERFANO +2

    Variable:
        i: ENTERO 
        j: ENTERO 
    
    Inicialización: 
        i: MIN 
        j: MIN_EDADES 
        Resultado [MIN_EDADES] <-  VACIO
        afirmación: 
            i > MIN Y j > MIN_EDADES => 
            Las celdas de sub_tabla(Resultado, MIN_EDADES, j - 1)
            se inicializan con los identificadores de las celdas de sub_tabla (familias, MIN,i- 1)
            los identificadores no son ni BORRADO ni VACIO y la edad está entre edad_MIN y edad_MAX 

    Realización: 
        hasta que: 
            familias[i].id = VACIO 
            o si no i > MAX
            invariante 
           
            variante de control:
                MAX - i+1
        
        repetir: 
            si: 
                familias[i].identificador ≠ BORRADO 
              y entonces: 
                edad_MIN <= familias[i].edad<= edad_MAX
            entonces:
                Resultado[j] <- familias [i].id
                j <- j + 1
            fin si 
            i <- i +1
        fin repetir 

    Postcondición:
        #Resultado está VACIO cuando los límites de edad no están en orden
        edad_MIN> edad_MAX => Resultado[1] = VACIO
        (∀ k ∊ Z) (
            indice_min(Resultado)<=k<=indice_max(Resultado) =>
            Resultado[k]es el identificador de una persona de edad entre edad_MIN y edad_MAX
        )
    fin edades 

#Envejecer a todas las personas registradas
Algoritmo envejecer:
    Entrada: 
        familias: TABLA[Persona]

    Precondicion: 
        familias ≠ NULO 

    Constante: 
        MIN: ENTERO <- indice_min (familias)
        MAX: ENTERO <- indice_max (familias)
        INFINITO: ENTERO <- ENTERO_MIN
        HUÉRFANO: ENTERO <- INFINITO
        BORRADO: ENTERO <- HUERFANO + 1
        VACIO:ENTERO <-  HUERFANO +2

    Variable:
        i: ENTERO 

    Inicializacion:
        i <- MIN 

    Realizacion: 
        hasta que:
            familias[i].id = VACIO 
          o si no: 
            i > MAX
            invariante:
                variante de control: 
                    MAX - i + 1
        repetir: 
            si: 
                familias.[i].id ≠ BORRADO
            entonces: 
                familias[i].edad <- familias[i].edad + 1
            fin si
            i <- i +1 
        fin repetir 

    Postcondicion: 
        Se han incrementado todos los atributos edad a las celdas no VACIO y no BORRADO
    fin envejecer

#Lista de personas huérfanas menores de 15 años 
Algoritmo huerfanos:
    Entrada 
        familias: TABLA[Persona]
        Resulatado: TABLA [ENTERO][1,500]

    Precondicion: 
        familias ≠ NULO 

    Constantes:
        MIN: ENTERO <- indice_min (familias)
        MAX: ENTERO <- indice_max (familias)
        MIN_HUERF: ENTERO <- indice_min(resultado)
        MAX_HUERF: ENTERO <- indice_max (resultado)
        INFINITO: ENTERO <- ENTERO_MIN
        HUÉRFANO: ENTERO <- INFINITO
        BORRADO: ENTERO <- HUERFANO + 1
        VACIO:ENTERO <-  HUERFANO +2

    Variable:
        i: ENTERO 
        j:ENTERO 

    Inicializacion: 
        i <-MIN 
        j <- MIN_HUERF
        resultado [j] <- VACIO 

    Realizacion: 
        hasta que: 
             familias [i].id = VACIO 
          o si no: 
            i > MAX 

            invariante: 

                variante de control: 
                    MAX - i +1

        repetir: 
            si: 
                familias[i].id ≠ BORRADO
              y entonces: 

                (familias[i].padre = HUERFANO
                  o
                familias[i].madre = HUERFANO)
            entonces: 
              Resultado[j] <- familias[i].id
            fin si 
            i <- i +1
        fin repetir 
    Postcondicion:
        Se han registrado en Resultado los identificadores de todos los
        HUERFANOS de las celdas ni VACIO ni BORRADO
    fin huerfanos 

Algoritmo padre:
# El identificador del padre de `identidad'.
    hasta que:
        familias[i].identificador = VACIO
      o si no
        i > MAX
    repetir:
        si:
            familia[i].identificador ≠ BORRADO
      y entonces:
        (   
            familia[i].identidad.nombre = identidad.nombre
        y
            familia[i].identidad.apellido = identidad.apellido
        )
    entonces:
        Resultado[j, 1] ← familia[i].identificador
        Resultado[j, 2] ← familia[i].padre
        j ← j + 1
        fin si
    i ← i + 1
    fin repetir
    variable:
        identidad : IDENTIDAD
        # La identidad para la que se busca el `padre'
        los_padres : MATRIZ[ENTERO][1, MAX_HOMONIMOS][1,2]
        # Los identificadores del `padre' de las personas de

    # identidad 'Jaime MARTIN'. Supone como máximo MAX_HOMONIMOS
    # en la base para `identidad'.
    realización:
        identidad.nombre ← 'Jaime'
        identidad.apellido ← 'MARTIN'
        los_padres ← padre(familias, identidad)

Algoritmo hermandades(identidad, familias):
    # Los identificadores de los hermanos y hermanas de `identidad'.
    Entrada:
        identidad : IDENTIDAD # Persona para la que buscan hermanos
        familias : TABLA[PERSONA] # La tabla a observar
        Resultado : ???
    constante:
        MAX_HOMONIMOS : ENTERO ← ???
        MAX_HERMANOS : ENTERO ← ???

        # Los identificadores de los hermanos y hermanas de una `identidad'
    Resultado : MATRIZ[ENTERO][1, MAX_HOMONIMOS][1, MAX_HERMANOS]

    inicialización:
        Resultado[1,1] ← VACIO # Todavía no hay hermanos registrados
algoritmo hermandades:

    variable:
        identidad : IDENTIDAD
        # La identidad para la que se busca el `padre'
        los_padres : MATRIZ[ENTERO][1, MAX_HOMONIMOS][1,2]
        # Los identificadores del `padre' de estas personas
        un_padre:ENTERO
        # El identificador de un `padre' de la matriz `los_padres'
    realización:
        los_padres ← padre(familias, identidad)
        Hasta que i > MAX_HOMONIMOS o si no los_padres[i,1] = VACIO 
        repetir:
            afirmación:
                i ≤ MAX_HOMONIMOS
                los_padres[i, 1] ≠ VACIO
                identificador ← los_padres[i, 1]
                # Identificador de `identidad' para la que buscan hermanos
                un_padre ← los_padres[i, 2]
                # El padre para el que se buscan los hijos
                Resultado[i] ← unos_hermanos(familias, identificador, un_padre)
                # Cálculo de los hermanos asociados a `identificador'
                i ← i + 1
            fin repetir
    Resultado[i,1] ← VACIO # Marca el final de los datos de la matriz
Algoritmo unos_hermanos:
    # Calcula los hermanos de padre `padre' de los hermanos de
    # `identificador'
    Entrada:
        familias : TABLA[PERSONA]
        identificador : ENTERO # Persona para la que queremos hermanos
        padre : ENTERO # Identificador del padre de los hermanos
        Resultado : TABLA[ENTERO] # Identificadores miembros de los hermanos
    constante:
        MAX : ENTERO ← índice_max(familias)
    variable:
        persona : ENTERO # Un identificador de persona
        i : ENTERO # siguiente hermano/a a registrar
    inicialización:
        Resultado[1] ← identificador
        i ← 1 # Índice del último hermano identificado
        j ← índice_min(familias)
    realización:
        persona ← familias[j].identificador
        # siguiente persona a observar en `familias'
        hasta que persona = VACIO o si no j > MAX 
        repetir:
            invariante:
            variante de control:
                MAX – i + 1
            si:
                persona ≠ BORRADO
              y
                familias[j].padre = padre
                entonces:
                    i ← i + 1
                    Resultado[i] ← persona
            fin si
            j ← j + 1
        fin repetir
        Resultado[i + 1] ← VACIO # Marca el final de los hermanos
    postcondición:
fin unos_hermanos
```

# Ejercicio 11: mcd de dos números enteros
En este ejercicio nos piden un algoritmo que permite determinar el máximo común divisor de dos números enteros.
El pseudocódigo es el siguiente:
```
mcd(n, m : ENTERO) : ENTERO
    # El Máximo Común Divisor de `n' y `m'.
precondición:
    # Enteros naturales
    n ≥ 0 ; m ≥ 0
    # 0 no tiene máximo divisor
    n ≠ 0 o si no m ≠ 0
variable:
    dividendo, divisor, resto : ENTERO
inicialización:
    divisor ← n
    resto ← m
realización:
    mientras que:
        resto > 0
        invariante:
            (H): la última división de la serie ha utilizado el
            resto de la división anterior como divisor y
            ha dado resto como resultado.

        variante de control:
            resto
    repetir:
        afirmación:
            resto > 0
            # Preparar la siguiente división
            dividendo ← divisor
            divisor ← resto
             Calcular el siguiente resto
            resto ← dividendo modulo divisor
        afirmación:
            (H) : la última división de la serie ha utilizado el
            resto de la división anterior como divisor y
            ha dado resto como resultado.
        fin repetir
        afirmación:
        resto = 0
        # El resultado es el último resto no nulo
        Resultado ← divisor
    postcondición:
        # El MCD divide `n' y `m'
        resto(n, Resultado) = 0
        resto(m, Resultado) = 0
        # Es el máximo entero que tiene esta propiedad
        (∀k ∈ N)(n ≠ 0 o si no m ≠ 0)
        (k > Resultado => resto(n, k) ≠ 0 o si no resto(m, k) ≠ 0)
fin mcd  

resto_2(a, b : ENTERO) : ENTERO
    # El resto de la división euclidiana de `a' por `b'.
    #
    # b x q ≤ a < b x (q+1) y r = a — b x q =>
    # a — b x (q+1) < 0 et r = a — b x (q+1) + b
    precondición:
        a ≥ 0 ; b > 0
    inicialización:
        Resultado ← a
    realización:
        repetir:
            Resultado ← Resultado – b
        hasta que:
            Resultado < 0
        fin repetir
        afirmación:
            Resultado = a — b x (cociente(a, b) + 1)
        Resultado ← Resultado + b
        afirmación:
            Resultado = a — b x (cociente(a, b) + 1) + b =>
            Resultado = a — b x cociente(a, b)
    postcondición:
        Resultado = a – b x cociente(a, b)
fin resto_2
```

# Ejercicio 12: Cuadrados perfectos y raíz cuadrada entera
En este ejercicio nos piden hacer un algoritmo que establezca la lista de los cuadrados perfectos inferiores a un límite dado y del cálculo de la raíz cuadrada entera de un número entero. El pseudocódigo es el siguiente:
```
Algoritmo raiz_cuadrada_entera:
   #Este algoritmo calcula la raíz cuadrada entera de un número entero n 
  Entrada: 
    n:ENTERO #cálculo de la raíz entera de n entero
    cuadrados: TABLA [ENTERO] #La tabla de los cuadrados   enteros
    raíz: ENTERO #entero "raíz cudrada de n"
  
  Precondicion:
    n>=0

  Postcondición:
    #El número n no se ha modificado 
    antiguo(n)= n
    #Las celdas de la tabla inicial no se han modificado 
    antiguo(
          sub_tabla(cuadrados,
                  antiguo(indice_min(cuadrados))+1,
                  antiguo(cuadrados[indice_min(cuadrados)])
                  ) = sub_tabla(cuadrados,
                  antiguo(indice_min(cuadrados))+1,
                  antiguo(cuadrados[indice_min(cuadrados)])
    #La tabla se amplía si es insuficiente 
      cuadrados[antiguo(indice_min(cuadrados))] < n => cuadrados[indice_min(cuadrados)] >= n
    #En caso contrario no se modifica ni la tabla ni indice_min(cuadrados)
      cuadrados[antiguo(indice_min(cuadrados))] => antiguo(indice_min(cuadrados)) =     indice_min(cuadrados)
    #`raiz`es la raiz cuadrada de `n`
    raiz**2 <= n< (raiz + 1)**2 <=> raiz = √n
  fin raiz_cuadrada_entera


Algoritmo tabla_de_los_cuadrados:
    # La serie en `cuadrados' de los cuadrados perfectos inferiores
    # a `límite'.
  Entrada:
    cuadrados : TABLEAU[ENTERO] # La tabla a inicializar
    límite : ENTERO # El límite superior de los cuadrados a calcular
  precondición:
    límite ≥ 0
    límite ≤ índice_max(cuadrados) x índice_max(cuadrados)
  variable:
    cuadrado : ENTERO # Un cuadrado perfecto k2
    impar : ENTERO # Un impar de la suite 2xk + 1
  inicialización:
    k ← 0 # el entero para el que se calcula el cuadrado
    cuadrado ← 0# cuadrado = k2
    impar ← 1 # impar = 2xk + 1
  realización:
    hasta que:
        cuadrado > límite
    repetir:
        cuadrados[k] ← cuadrado
        cuadrado ← cuadrado + impar
        impar ← impar + 2
        k ← k +1
    fin repetir
  postcondición:
    antiguo(límite) = límite
    (∀k ∈ Z)(índice_min(cuadrados) ≤ k et k2 ≤ límite =>cuadrados[k] = k2 )
  fin tabla_de_los_cuadrados
```
