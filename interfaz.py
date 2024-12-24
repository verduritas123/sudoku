import tkinter as tk
from tkinter import messagebox
from generador_sudoku import generar_tablero_completo, eliminar_numeros
from solucionador_sudoku import resolver_sudoku

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Sudoku")

        # Variables
        self.celdas = [[None for _ in range(9)] for _ in range(9)]
        
        # Mostrar diálogo de selección de dificultad
        self.seleccionar_dificultad()

        # Botones
        resolver_btn = tk.Button(root, text="Resolver", command=self.resolver)
        resolver_btn.grid(row=9, column=0, columnspan=9//2, sticky="nsew")
        
        verificar_btn = tk.Button(root, text="Verificar", command=self.verificar)
        verificar_btn.grid(row=9, column=9//2, columnspan=9//2, sticky="nsew")

        nuevo_juego_btn = tk.Button(root, text="Nuevo Juego", command=self.nuevo_juego)
        nuevo_juego_btn.grid(row=10, column=0, columnspan=9, sticky="nsew")

    def seleccionar_dificultad(self):
        # Ventana emergente para seleccionar dificultad
        def set_dificultad(valor):
            self.dificultad = valor
            dificultad_ventana.destroy()
            self.nuevo_juego()

        dificultad_ventana = tk.Toplevel(self.root)
        dificultad_ventana.title("Seleccionar Dificultad")
        dificultad_ventana.geometry("300x200")
        tk.Label(dificultad_ventana, text="Selecciona la dificultad:", font=("Arial", 14)).pack(pady=20)
        
        tk.Button(dificultad_ventana, text="Fácil", command=lambda: set_dificultad(30), width=15).pack(pady=5)
        tk.Button(dificultad_ventana, text="Medio", command=lambda: set_dificultad(50), width=15).pack(pady=5)
        tk.Button(dificultad_ventana, text="Difícil", command=lambda: set_dificultad(60), width=15).pack(pady=5)

    def nuevo_juego(self):
        self.tablero_completo = generar_tablero_completo()
        self.tablero_inicial = eliminar_numeros(self.tablero_completo, celdas_a_eliminar=self.dificultad)
        self.tablero = [fila[:] for fila in self.tablero_inicial]
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(9):
            for col in range(9):
                if self.tablero_inicial[fila][col] != 0:
                    # Celdas bloqueadas con números grandes
                    celda = tk.Label(
                        self.root, text=str(self.tablero_inicial[fila][col]), 
                        font=("Arial", 20), bg="lightgray", width=2, height=1, anchor="center"
                    )
                else:
                    # Celdas editables
                    celda = tk.Text(
                        self.root, font=("Arial", 10), height=3, width=6, wrap="word"
                    )
                    celda.bind("<FocusOut>", lambda event, r=fila, c=col: self.ajustar_celda(event, r, c))
                celda.grid(row=fila, column=col, sticky="nsew", padx=1, pady=1)
                self.celdas[fila][col] = celda

        for i in range(9):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)

    def ajustar_celda(self, event, fila, col):
        celda = event.widget
        contenido = celda.get("1.0", tk.END).strip()
        if contenido.isdigit() and len(contenido) == 1:  # Un solo número
            celda.delete("1.0", tk.END)
            celda.insert("1.0", contenido)
            celda.config(font=("Arial", 20), height=1, width=2)  # Cambiar a estilo grande
        else:  # Devolver al estilo pequeño si hay múltiples candidatos
            celda.config(font=("Arial", 10), height=3, width=6)

    def resolver(self):
        if resolver_sudoku(self.tablero):
            for fila in range(9):
                for col in range(9):
                    if isinstance(self.celdas[fila][col], tk.Text):
                        self.celdas[fila][col].delete("1.0", tk.END)
                        self.celdas[fila][col].insert("1.0", str(self.tablero[fila][col]))
            messagebox.showinfo("Éxito", "¡El Sudoku ha sido resuelto!")
        else:
            messagebox.showerror("Error", "No se puede resolver este Sudoku.")

    def verificar(self):
        tablero_usuario = []
        for fila in range(9):
            fila_valores = []
            for col in range(9):
                celda = self.celdas[fila][col]
                if isinstance(celda, tk.Text):
                    contenido = celda.get("1.0", tk.END).strip()
                    if contenido.isdigit():
                        fila_valores.append(int(contenido))
                    else:
                        fila_valores.append(0)
                else:
                    fila_valores.append(int(celda.cget("text")))

            tablero_usuario.append(fila_valores)

        if self.validar_tablero_usuario(tablero_usuario):
            messagebox.showinfo("Éxito", "¡Has resuelto el Sudoku correctamente!")
        else:
            messagebox.showerror("Error", "El tablero tiene errores.")

    def validar_tablero_usuario(self, tablero):
        for fila in range(9):
            if len(set(tablero[fila])) != 9 or 0 in tablero[fila]:
                return False
        for col in range(9):
            if len(set(tablero[f][col] for f in range(9))) != 9:
                return False
        for inicio_fila in range(0, 9, 3):
            for inicio_col in range(0, 9, 3):
                numeros = []
                for i in range(inicio_fila, inicio_fila + 3):
                    for j in range(inicio_col, inicio_col + 3):
                        numeros.append(tablero[i][j])
                if len(set(numeros)) != 9:
                    return False
        return True
