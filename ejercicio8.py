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