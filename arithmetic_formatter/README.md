# Arithmetic_Formater

Crea una función que reciba una lista de cadenas que sean problemas aritméticos y devuelva los problemas ordenados verticalmente y uno al lado del otro. La función debe tomar opcionalmente un segundo argumento. Cuando el segundo argumento se establezca como True, se deberán mostrar las respuestas.

## Reglas
La función devolverá la conversión correcta si los problemas suministrados están correctamente formateados, de lo contrario, devolverá una cadena que describe un error significativo para el usuario.

* Situaciones que devolverán un error:
  * Si hay demasiados problemas suministrados a la función. El límite es cinco, cualquier cosa más regresará: `Error: Too many problems`.
  * Los operadores apropiados que la función aceptará son suma y resta. La multiplicación y la división devolverán un error. Otros operadores que no se mencionan en este punto no tendrán que ser probados. El error devuelto será: `Error: Operator must be '+' or '-'`.
  * Cada número (operando) debe contener solo dígitos. De lo contrario, la función devolverá: `Error: Numbers must only contain digits`.
  * Cada operando (también conocido como número en cada lado del operador) tiene un máximo de cuatro dígitos de ancho. De lo contrario, la cadena de error devuelta será: `Error: Numbers cannot be more than four digits`.

* Si el usuario proporcionó el formato correcto de los problemas, la conversión que devuelva seguirá estas reglas:
  * Debe haber un solo espacio entre el operador y el más largo de los dos operandos, el operador estará en la misma línea que el segundo operando, ambos operandos estarán en el mismo orden proporcionado (el primero será el superior y el segundo el inferior).
  * Los números deben estar alineados a la derecha.
  * Debe haber cuatro espacios entre cada problema.
  * Debe haber guiones en la parte inferior de cada problema. Los guiones deben recorrer toda la longitud de cada problema individualmente.

## For example
Function Call:

`arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])`

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
Function Call:

`arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)`
Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
