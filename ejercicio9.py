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
postcondición
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

Algoritmo insertar 
inserción(palabra : PALABRA ; diccionario : TABLA[PALABRA])
    # Insertar `palabra' en `diccionario'.
Precondición
    palabra ≠ NULO
    está_definido(diccionario)
    no está_completo(diccionario)
realización
    # Buscar la primera celda libre en `diccionario'
    k ← libre(diccionario)
    # Guardar palabra en la celda de índice k
    diccionario[k] ← palabra
    # Buscar la posición de inserción de la `palabra' en orden
    # alfabético en `diccionario'
    posición ← coloca(palabra, diccionario)
    # Realiza la inserción efectiva
    insertar(k, diccionario, posición)
postcondición
    # `diccionario' (ya) no está vacío
    no está_vacío(diccionario)
    # `palabra' está colocada en una celda de la tabla efectiva
    palabra ∈ sub_tabla
        (
            diccionario,
            índice_min(diccionario) + 1,
            índice_max(diccionario)
        )
Resultado
    Solo se modifican la celda insertada y las dos celdas
    que la rodean en el orden alfabético
fin inserción

