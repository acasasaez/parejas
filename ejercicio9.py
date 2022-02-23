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
realización
    mientras que
        i ≤ I_MAX et Resultado = AUSENTE
        invariante
            (∀k ∈ Z)(I_MIN ≤ k < i => Resultado = AUSENTE) <=> (∀k ∈ Z)
            (I_MIN ≤ k < i => ítem(diccionario[k], 1) ≠ inicial
        variante de control
            I_MAX – i + 1
    repetir
        si
            ítem(diccionario[i], 1) = inicial
        entonces
            afirmación
                i ≤ I_MAX
                (∀k ∈ Z)(I_MIN ≤ k < i => Resultado = AUSENTE) et
                ítem(diccionario[i], 1) = inicial
            Resultado ← i
            afirmación
                i ≤ I_MAX
                Resultado = i ≠ AUSENTE
        fin si
        i ← i + 1
        afirmación
            i ≤ I_MAX + 1
            Resultado = i o Resultado = AUSENTE
    fin repetir
