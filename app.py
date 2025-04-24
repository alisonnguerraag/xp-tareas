tareas = []  # lista para simular base de datos

def crear_tarea(titulo, descripcion, fecha_limite):
    if not titulo.strip(): # el strip es para quitar los espacios
        raise ValueError("El título es obligatorio")
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "completada": False
    }
    tareas.append(tarea)
    return tarea

def visualizar_tareas():
    return tareas

def editar_tarea(tarea, nuevos_valores):
    if "titulo" in nuevos_valores:
        tarea["titulo"] = nuevos_valores["titulo"]
    if "descripcion" in nuevos_valores:
        tarea["descripcion"] = nuevos_valores["descripcion"]
    if "fecha_limite" in nuevos_valores:
        tarea["fecha_limite"] = nuevos_valores["fecha_limite"]

def eliminar_tarea(tarea):
    if tarea in tareas:
        tareas.remove(tarea)

# intento del entregable funcional iteracion 1
if __name__ == "__main__": # esto solo se ejecuta si se corre directamente en app.py 
    print("Crear tarea:")
    t1 = crear_tarea("Concierto: Gracie Abrams", "Comprar boletos para ver a Gracie", "2025-04-28")
    print(visualizar_tareas())
    
    print("\nEditar tarea:")
    editar_tarea(t1, {
        "titulo": "Gracie Abrams (VIP)",
        "descripcion": "Comprar boletos VIP para ver a Gracie",
        "fecha_limite": "2025-04-25"
    })
    print(visualizar_tareas())
    
    print("\nEliminar tarea:")
    eliminar_tarea(t1)
    print(visualizar_tareas())
