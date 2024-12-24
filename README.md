# Sudoku Solver using Backtracking Algorithm

## Descripción

Este proyecto contiene un solucionador de Sudoku utilizando el algoritmo de **Backtracking**. El código resuelve un tablero de Sudoku incompleto de forma eficiente respetando las reglas del juego. Además, incluye una interfaz gráfica interactiva para que los usuarios puedan jugar, verificar y resolver el Sudoku.

## Ejecución del Programa

1. **Ejecuta el archivo principal**:
    Para iniciar la aplicación, ejecuta el archivo `main.py`:
    ```bash
    python main.py
    ```

2. **Seleccionar dificultad**:
    Al ejecutar el programa, se abrirá una ventana que te pedirá seleccionar un nivel de dificultad para el Sudoku (Fácil, Medio, Difícil). Esto determina la cantidad de celdas vacías que se generarán en el tablero de Sudoku.

3. **Jugar el Sudoku**:
    El programa generará un tablero con celdas vacías que puedes completar. También podrás verificar la validez de tu solución usando el botón **"Verificar"**.

4. **Resolver el Sudoku**:
    Si deseas que el programa resuelva el Sudoku automáticamente, puedes presionar el botón **"Resolver"**. Esto hará que el algoritmo de backtracking complete el tablero de forma automática.

5. **Nuevo Juego**:
    Si quieres empezar un nuevo juego, presiona el botón **"Nuevo Juego"** para generar un nuevo tablero con un nivel de dificultad seleccionado.

## Archivos del Proyecto

- **`generador_sudoku.py`**: Este archivo contiene funciones que generan el tablero de Sudoku completo y lo hacen incompleto para crear un desafío para el jugador. La función `generar_tablero_completo()` crea un tablero válido y `eliminar_numeros()` elimina una cantidad específica de celdas para crear el tablero.
  
- **`solucionador_sudoku.py`**: Contiene la implementación del algoritmo de backtracking para resolver el Sudoku. La función principal `resolver_sudoku(tablero)` es recursiva y encuentra la solución del tablero al probar diferentes combinaciones de números.

- **`interfaz.py`**: Este archivo define la interfaz gráfica utilizando Tkinter. Se crea un tablero visual que permite al usuario ingresar los números, y los números existentes se muestran con un tamaño de fuente grande para indicar que son valores predefinidos. Las celdas editables permiten al usuario ingresar respuestas.

- **`main.py`**: Es el archivo principal que se ejecuta cuando el proyecto es iniciado. Este archivo organiza la interacción entre la interfaz gráfica, el generador y solucionador de Sudoku. Es el punto de entrada de la aplicación.

## Funcionalidad

1. **Generación del tablero**:
   El tablero se genera de forma aleatoria y se crea un Sudoku incompleto eliminando una cantidad seleccionada de celdas.

2. **Algoritmo de backtracking**:
   El algoritmo de backtracking se encarga de resolver el Sudoku. Se prueba con diferentes números hasta encontrar una solución válida. Si un número no puede colocarse de forma válida, retrocede y prueba con otro.

3. **Interfaz gráfica**:
   La interfaz gráfica permite al usuario interactuar con el tablero. Las celdas predefinidas (números dados) se muestran en un tamaño de fuente grande, mientras que las celdas editables tienen un tamaño de fuente más pequeño. El usuario puede escribir los números directamente en las celdas.

4. **Verificación y resolución**:
   Los botones de verificación y resolución permiten al jugador comprobar si su solución es válida o dejar que el programa resuelva el Sudoku automáticamente.
