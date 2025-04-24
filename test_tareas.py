import unittest

def crear_tarea(titulo, descripcion, fecha_limite):
    if not titulo.strip():
        raise ValueError("El título es obligatorio")

    return {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "completada": False
    }

class TestTareas(unittest.TestCase):
    def test_crear_tarea_valida(self):
        tarea = crear_tarea("Hacer XP", "Aplicar TDD", "2025-04-30")
        self.assertEqual(tarea["titulo"], "Hacer XP")
        self.assertEqual(tarea["descripcion"], "Aplicar TDD")
        self.assertEqual(tarea["fecha_limite"], "2025-04-30")
        self.assertFalse(tarea["completada"])

    def test_crear_tarea_sin_titulo(self):
        with self.assertRaises(ValueError):
            crear_tarea("   ", "Falta título", "2025-04-30")

    def test_visualizar_tareas(self):
        tareas = []
        tareas.append(crear_tarea("Tarea 1", "Descripción 1", "2025-04-30"))
        tareas.append(crear_tarea("Tarea 2", "Descripción 2", "2025-05-01"))
        self.assertEqual(len(tareas), 2)
        self.assertEqual(tareas[0]["titulo"], "Tarea 1")
        self.assertEqual(tareas[1]["titulo"], "Tarea 2")
    
    def test_editar_tarea(self):
        tarea = crear_tarea("Tarea original", "Descripción original", "2025-04-30")

        # Simulación de edición de la tarea
        tarea["titulo"] = "Tarea editada"
        tarea["descripcion"] = "Nueva descripción"
        tarea["fecha_limite"] = "2025-05-10"

        self.assertEqual(tarea["titulo"], "Tarea editada")
        self.assertEqual(tarea["descripcion"], "Nueva descripción")
        self.assertEqual(tarea["fecha_limite"], "2025-05-10")
    
    def test_eliminar_tarea(self):
        tareas = []
        tarea1 = crear_tarea("Tarea 1", "Descripción 1", "2025-04-30")
        tarea2 = crear_tarea("Tarea 2", "Descripción 2", "2025-05-01")

        tareas.append(tarea1)
        tareas.append(tarea2)

        tareas.remove(tarea1)  # Simulación de eliminación

        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["titulo"], "Tarea 2")




if __name__ == '__main__':
    unittest.main()


