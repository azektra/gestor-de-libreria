# File: gestion_biblioteca.py
import tkinter as tk
from tkinter import messagebox

# Lista de diccionarios para almacenar los libros
# Datos de ejemplo
biblioteca = [
    {"id": 1, "titulo": "Batman", "autor": "Alfred", "prestado": False},
    {"id": 2, "titulo": "Flash", "autor": "Reverso", "prestado": False},
    {"id": 3, "titulo": "Deadpool", "autor": "Francis", "prestado": True},
    {"id": 4, "titulo": "El Señor de los Anillos", "autor": "Tolkien", "prestado": False},
    {"id": 5, "titulo": "Harry Potter", "autor": "J.K. Rowling", "prestado": False},
    {"id": 6, "titulo": "1984", "autor": "George Orwell", "prestado": True},
]

biblioteca_eliminada = []

# --- Funciones de Gestión de Libros  ---

def mostrar_libros():
    # Crea una cadena con la información de cada libro
    libros_texto = ""
    for libro in biblioteca:
        estado = "Prestado" if libro["prestado"] == True else "Disponible"
        libros_texto += f"{libro['id']}: {libro['titulo']} - {libro['autor']} ({estado})\n"

    if not libros_texto:
        libros_texto = "La biblioteca está vacía."

    messagebox.showinfo("Biblioteca", libros_texto)


def mostrar_eliminados():
    # Crea una cadena con la información de cada libro
    libros_texto = ""
    for libro in biblioteca_eliminada:
        estado = "eliminado"
        libros_texto += f"{libro['id']}: {libro['titulo']} - {libro['autor']} ({estado})\n"

    if not libros_texto:
        libros_texto = "No hay libros eliminados."

    messagebox.showinfo("Basurero", libros_texto)

def agregar_libro():
    titulo = entrada_titulo.get().strip() # Elimina espacios al inicio/final
    autor = entrada_autor.get().strip()   # Elimina espacios al inicio/final

    if titulo and autor: # Verifica que los campos no estén vacíos
        nuevo_id = 1
        if biblioteca: # Si la lista no está vacía
            nuevo_id = max([libro["id"] for libro in biblioteca]) + 1

        nuevo_libro = {"id": nuevo_id, "titulo": titulo, "autor": autor, "prestado": False}
        biblioteca.append(nuevo_libro)

        messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado correctamente con ID {nuevo_id}.")
        entrada_titulo.delete(0, tk.END) # Limpia los campos
        entrada_autor.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Por favor, ingresa título y autor.")

def prestar_libro():
    try:
        # Intenta obtener el ID y convertirlo a número
        libro_id = int(entrada_id.get().strip())

        # Busca el libro por ID
        libro_encontrado = None
        for libro in biblioteca:
            if libro["id"] == libro_id:
                libro_encontrado = libro
                break # Sale del bucle una vez encontrado

        if libro_encontrado: # Si se encontró el libro
            if not libro_encontrado["prestado"]: # Si no está prestado
                libro_encontrado["prestado"] = True
                messagebox.showinfo("Éxito", f"Has prestado '{libro_encontrado['titulo']}'")
            else:
                messagebox.showwarning("Error", "El libro ya está prestado.")
        else:
            messagebox.showwarning("Error", "Libro no encontrado.")

    except ValueError:
        # Si la conversión a entero falla
        messagebox.showwarning("Error", "Ingresa un ID numérico válido.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def devolver_libro():
    try:
        # Intenta obtener el ID y convertirlo a número
        libro_id = int(entrada_id.get().strip())

        # Busca el libro por ID
        libro_encontrado = None
        for libro in biblioteca:
            if libro["id"] == libro_id:
                libro_encontrado = libro
                break # Sale del bucle una vez encontrado

        if libro_encontrado: # Si se encontró el libro
            if libro_encontrado["prestado"]: # Si está prestado
                libro_encontrado["prestado"] = False
                messagebox.showinfo("Éxito", f"Has devuelto '{libro_encontrado['titulo']}'")
            else:
                messagebox.showwarning("Error", "El libro no estaba prestado.")
        else:
            messagebox.showwarning("Error", "Libro no encontrado.")

    except ValueError:
        # Si la conversión a entero falla
        messagebox.showwarning("Error", "Ingresa un ID numérico válido.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def eliminar_libro():
    try:
        # Intenta obtener el ID y convertirlo a número
        libro_id = int(entrada_id.get().strip())

        # Busca el libro por ID y su índice
        libro_index = -1 # Usamos -1 para indicar que no se encontró
        for i, libro in enumerate(biblioteca):
            if libro["id"] == libro_id:
                libro_index = i
                break # Sale del bucle una vez encontrado

        if libro_index != -1: # Si se encontró el libro (el índice no es -1)
            # Elimina el libro usando su índice
            libro_eliminado = biblioteca.pop(libro_index)
            biblioteca_eliminada.append(libro_eliminado)
            messagebox.showinfo("Éxito", f"Libro '{libro_eliminado['titulo']}' eliminado correctamente.")
        else:
            messagebox.showwarning("Error", "Libro no encontrado para eliminar.")

    except ValueError:
        # Si la conversión a entero falla
        messagebox.showwarning("Error", "Ingresa un ID numérico válido.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


# --- Configuración de la Interfaz Gráfica ---

# Creación de la ventana
ventana = tk.Tk()
ventana.title("Biblioteca Virtual Simplificada")
ventana.geometry("400x450") # Tamaño inicial
ventana.configure(bg="#2E2E2E")

# Configurar etiquetas y campos de entrada usando grid
tk.Label(ventana, text="Título:",fg="white",bg="#4A4A4A", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_titulo = tk.Entry(ventana,bg="#4A4A4A",fg="white", font=("Arial", 12))
entrada_titulo.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(ventana, text="Autor:",fg="white",bg="#4A4A4A", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada_autor = tk.Entry(ventana,bg="#4A4A4A",fg="white", font=("Arial", 12))
entrada_autor.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(ventana, text="ID Libro:",fg="white",bg="#4A4A4A", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_id = tk.Entry(ventana,bg="#4A4A4A",fg="white", font=("Arial", 12))
entrada_id.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Botones
tk.Button(ventana, text="Mostrar Libros", font=("Arial", 12),fg="#ffd700",bg="#4A4A4A", command=mostrar_libros).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
tk.Button(ventana, text="Agregar Libro", font=("Arial", 12),fg="#ffd700",bg="#4A4A4A", command=agregar_libro).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
tk.Button(ventana, text="Prestar Libro", font=("Arial", 12),fg="#ffd700",bg="#4A4A4A", command=prestar_libro).grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
tk.Button(ventana, text="Devolver Libro", font=("Arial", 12),fg="#ffd700",bg="#4A4A4A", command=devolver_libro).grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
tk.Button(ventana, text="Eliminar Libro", font=("Arial", 12),fg="red",bg="#4A4A4A", command=eliminar_libro).grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
tk.Button(ventana, text="libros eliminados", font=("Arial", 12),fg="red",bg="#4A4A4A", command=mostrar_eliminados).grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Configurar expansión de filas y columnas (opcional, pero mantiene la interfaz responsive)
ventana.rowconfigure(9, weight=1)
ventana.columnconfigure(1, weight=1)


# Iniciar ventana
ventana.mainloop()
