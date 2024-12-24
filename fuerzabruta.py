from solucionador_sudoku import es_valido
N=9
# Algoritmo de Fuerza Bruta
def resolver_sudoku_fuerza_bruta(tablero):
    for fila in range(N):
        for columna in range(N):
            if tablero[fila][columna] == 0:  # Celda vacía
                for num in range(1, 10):
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num  # Colocamos el número
                        if resolver_sudoku_fuerza_bruta(tablero):
                            return True
                        tablero[fila][columna] = 0  # Retrocedemos
                return False
    return True
