# Juego de totito en terminal
Para jugar deberás ingresar un número entero de 1-9 en cada turno que se te solicita.

## Funcionamiento
El script es modular. Se definió una función para imprimir la tabla, para los turnos del usuario, para los turnos del oponente (pc), para verificar (en función del signo que se le pasa) al ganador y para verificar si la casilla ya está marcada, respectivamente.

El juego se inicia en la función main que inicia el tablero y con un bucle <code>while</code> se intercambian los turnos y se imprime el resultado.

## Algoritmo
1. Se ejecuta la aplicación (comienza el juego).
2. La aplicación alterna los turnos y determina el resultado:<br>
   2.1. La aplicación solicita al usuario que introduzca su jugada.<br>
   2.2. El usuario introduce el número de casilla a marcar.<br>
   2.3. La aplicación actualiza el tablero.<br>
   2.4. La aplicación verifica si el usuario gana el juego.<br>
   2.5. El oponente (pc) marca una casilla aleatoria que esté disponible.<br>
   2.6. La aplicación actualiza el tablero.<br>
   2.7. La aplicación verifica si el oponente gana el juego.<br>
   2.8. La aplicación imprime el tablero.
3. La aplicación imprime el resultado.