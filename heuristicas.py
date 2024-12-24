from solucionador_sudoku import es_valido
N=9
# Función que devuelve las celdas vacías ordenadas por la cantidad de opciones posibles
def obtener_celda_con_menos_opciones(tablero):
    vacias = []
    for fila in range(N):
        for columna in range(N):
            if tablero[fila][columna] == 0:  # Celda vacía
                opciones_posibles = obtener_opciones_posibles(tablero, fila, columna)
                vacias.append((fila, columna, opciones_posibles))
    
    # Ordenamos las celdas por el número de opciones posibles (de menor a mayor)
    vacias.sort(key=lambda x: len(x[2]))
    return vacias

# Función que obtiene las opciones posibles para una celda (números válidos)
def obtener_opciones_posibles(tablero, fila, columna):
    opciones = []
    for num in range(1, 10):
        if es_valido(tablero, fila, columna, num):
            opciones.append(num)
    return opciones

# Modificación en el algoritmo de backtracking para aplicar la heurística
def resolver_sudoku_con_heuristicas(tablero):
    celdas_vacias = obtener_celda_con_menos_opciones(tablero)
    
    if not celdas_vacias:
        return True  # No hay más celdas vacías, Sudoku resuelto
    
    fila, columna, opciones_posibles = celdas_vacias[0]  # Tomamos la celda con menos opciones posibles
    
    for num in opciones_posibles:
        tablero[fila][columna] = num  # Colocamos el número en la celda
        
        if resolver_sudoku_con_heuristicas(tablero):
            return True
        
        tablero[fila][columna] = 0  # Retrocedemos (backtrack)
    
    return False
