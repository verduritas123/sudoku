N = 9

# Comprobar si un número puede colocarse en una celda
def es_valido(tablero, fila, columna, num):
    if num in tablero[fila]:
        return False
    if num in [tablero[i][columna] for i in range(N)]:
        return False
    inicio_fila, inicio_col = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False
    return True

# Resolver Sudoku con backtracking
def resolver_sudoku(tablero):
    for fila in range(N):
        for columna in range(N):
            if tablero[fila][columna] == 0:
                for num in range(1, 10):
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][columna] = 0
                return False
    return True
