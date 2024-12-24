import timeit
from heuristicas import resolver_sudoku_con_heuristicas
from generador_sudoku import generar_tablero_completo
from fuerzabruta import resolver_sudoku_fuerza_bruta

N = 9

# Test de ambos enfoques
def probar_algoritmos():
    tablero = generar_tablero_completo()  # Crear un tablero Sudoku
    
    # Medir el tiempo de ejecución con backtracking mejorado
    start = timeit.default_timer()  # Comienza el temporizador
    resolver_sudoku_con_heuristicas(tablero)
    end = timeit.default_timer()  # Finaliza el temporizador
    print(f"Backtracking con heurísticas: {end - start} segundos")
    
    # Medir el tiempo de ejecución con fuerza bruta
    start = timeit.default_timer()  # Comienza el temporizador
    resolver_sudoku_fuerza_bruta(tablero)
    end = timeit.default_timer()  # Finaliza el temporizador
    print(f"Fuerza bruta: {end - start} segundos")

probar_algoritmos()
