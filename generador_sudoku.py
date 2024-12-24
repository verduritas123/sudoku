import random
from solucionador_sudoku import resolver_sudoku

N = 9

# Generar un tablero completo
def generar_tablero_completo():
    tablero = [[0] * N for _ in range(N)]
    resolver_sudoku(tablero)
    return tablero

# Generar un tablero incompleto con celdas vacías
def eliminar_numeros(tablero, celdas_a_eliminar):
    celdas = [(i, j) for i in range(N) for j in range(N)]
    random.shuffle(celdas)
    for _ in range(celdas_a_eliminar):
        fila, col = celdas.pop()
        tablero[fila][col] = 0
    return tablero
