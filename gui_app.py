import tkinter as tk
from tkinter import messagebox, simpledialog
from app import crear_tarea, visualizar_tareas, editar_tarea, eliminar_tarea

# Lista global para almacenar tareas
tareas = []

def agregar_tarea():
    titulo = simpledialog.askstring("Crear tarea", "Título:")
    descripcion = simpledialog.askstring("Crear tarea", "Descripción:")
    fecha_limite = simpledialog.askstring("Crear tarea", "Fecha límite (YYYY-MM-DD):")

    try:
        tarea = crear_tarea(titulo, descripcion, fecha_limite)
        tareas.append(tarea)
        messagebox.showinfo("Éxito", "Tarea creada exitosamente")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def mostrar_tareas():
    if not tareas:
        messagebox.showinfo("Tareas", "No hay tareas aún.")
        return
    
    resultado = ""
    for idx, tarea in enumerate(tareas):
        resultado += f"{idx+1}. {tarea['titulo']} - {tarea['descripcion']} - {tarea['fecha_limite']}\n"
    
    messagebox.showinfo("Todas las tareas", resultado)

def editar_una_tarea():
    if not tareas:
        messagebox.showinfo("Editar", "No hay tareas para editar.")
        return

    try:
        indice = simpledialog.askinteger("Editar tarea", "Número de tarea a editar (1, 2, 3...):") - 1
        if indice < 0 or indice >= len(tareas):
            raise IndexError
        
        nuevo_titulo = simpledialog.askstring("Editar tarea", "Nuevo título:")
        nueva_descripcion = simpledialog.askstring("Editar tarea", "Nueva descripción:")
        nueva_fecha = simpledialog.askstring("Editar tarea", "Nueva fecha límite (YYYY-MM-DD):")

        editar_tarea(tareas[indice], {"titulo": nuevo_titulo, "descripcion": nueva_descripcion, "fecha_limite": nueva_fecha})
        messagebox.showinfo("Éxito", "Tarea editada exitosamente.")
    except (IndexError, TypeError):
        messagebox.showerror("Error", "Número inválido de tarea.")

def eliminar_una_tarea():
    if not tareas:
        messagebox.showinfo("Eliminar", "No hay tareas para eliminar.")
        return

    try:
        indice = simpledialog.askinteger("Eliminar tarea", "Número de tarea a eliminar (1, 2, 3...):") - 1
        if indice < 0 or indice >= len(tareas):
            raise IndexError
        
        eliminar_tarea(tareas[indice])  # Corregido: solo pasa una tarea
        messagebox.showinfo("Éxito", "Tarea eliminada exitosamente.")
    except (IndexError, TypeError):
        messagebox.showerror("Error", "Número inválido de tarea.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Administrador de Tareas XP")
ventana.geometry("300x300")

# Botones
boton_crear = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
boton_crear.pack(pady=10)

boton_mostrar = tk.Button(ventana, text="Visualizar tareas", command=mostrar_tareas)
boton_mostrar.pack(pady=10)

boton_editar = tk.Button(ventana, text="Editar tarea", command=editar_una_tarea)
boton_editar.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_una_tarea)
boton_eliminar.pack(pady=10)

ventana.mainloop()