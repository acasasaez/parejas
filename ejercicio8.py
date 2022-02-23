Algoritmo descomponer
  # Descompone `ca' en `componentes' en `dimensión' cadenas
  # separadas por `separador'.
Entrada
  ca : CADENA # La cadena a descomponer
  separador : CARACTER # El carácter que separa las cadenas
  componentes : TABLA[CADENA] # Los componentes de `ca'
  dimensión : ENTERO # La cantidad de componentes
precondición
  ca ≠ NULO
  separador ≠ NULO
  está_definido(componentes)
variable
  L : ENTERO # La longitud de `ca'
  k : ENTERO # Última ocurrencia del `separador' encontrada
  i : ENTERO # Índice del siguiente componente a registrar
  r : ENTERO # Posición siguiente ocurrencia del `separador'
inicialización
    L ← longitud(ca) # Índice del último carácter
    k ← 0
        # Índice de la última ocurrencia del `separador'
        # encontrada
    i ← 1 # Índice del siguiente componente a registrar
    r ← posición(ca, 1, L)
        # Búsqueda de la primera ocurrencia de `separador'
mientras que
    k < L y r ≠ AUSENTE
    invariante
        (H)
    variante de control
        L - k