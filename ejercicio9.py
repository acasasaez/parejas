Algoritmo índice_palabra
    # La primera palabra de `diccionario' que empieza por
    # `inicial'.
Entrada
    inicial : CARACTER
        # La inicial a buscar
    diccionario : TABLA[CADENA]
        # Objetivo de la búsqueda
Resultado : ENTERO
precondición
    es_alfabético(inicial)
    está_definido(diccionario)
constante
    I_MIN : ENTERO ← índice_min(diccionario)
    I_MAX : ENTERO ← índice_max(diccionario)
    AUSENTE : ENTERO ← ???
variable
    i : ENTERO # Índice siguiente celda a observar
inicialización
    i ← I_MIN
    Resultado = AUSENTE # Todavía no se ha encontrado     nada
