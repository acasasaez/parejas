Algoritmo raiz_cuadrada_entera
   #Este algoritmo calcula la raíz cuadrada entera de un número entero n 
Entrada 
  n:ENTERO #cálculo de la raíz entera de n entero
  cuadrados: TABLA [ENTERO] #La tabla de los cuadrados   enteros
  raíz: ENTERO #entero "raíz cudrada de n"
  
Precondicion
  n>=0

Postcondición
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