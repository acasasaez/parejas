mcd(n, m : ENTERO) : ENTERO
    # El Máximo Común Divisor de `n' y `m'.
precondición
    # Enteros naturales
    n ≥ 0 ; m ≥ 0
    # 0 no tiene máximo divisor
    n ≠ 0 o si no m ≠ 0
variable
    dividendo, divisor, resto : ENTERO
inicialización
    divisor ← n
    resto ← m
realización
    mientras que
        resto > 0
        invariante
            (H): la última división de la serie ha utilizado el
            resto de la división anterior como divisor y
            ha dado resto como resultado.

        variante de control
            resto
    repetir



