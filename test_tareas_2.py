import unittest
from app import crear_tarea, editar_tarea, eliminar_tarea, visualizar_tareas, tareas

class TestTareas(unittest.TestCase):
    def test_crear_tarea_valida(self):
        tareas.clear()  # limpiar antes de probar
        tarea = crear_tarea("Estudiar XP", "Repasar conceptos", "2025-05-05")
        self.assertEqual(tarea["titulo"], "Estudiar XP")
        self.assertFalse(tarea["completada"])

    def test_crear_tarea_sin_titulo(self):
        tareas.clear()  # limpiar antes de probar
        with self.assertRaises(ValueError):
            crear_tarea("   ", "Sin título", "2025-05-06")

    def test_editar_tarea(self):
        tareas.clear()  # limpiar antes de probar
        tarea = crear_tarea("Tarea vieja", "Descripción vieja", "2025-05-01")

        nuevos_valores = {
            "titulo": "Tarea nueva",
            "descripcion": "Nueva descripción",
            "fecha_limite": "2025-06-01"
        }

        editar_tarea(tarea, nuevos_valores)
        self.assertEqual(tarea["titulo"], "Tarea nueva")
        self.assertEqual(tarea["descripcion"], "Nueva descripción")
        self.assertEqual(tarea["fecha_limite"], "2025-06-01")

    def test_eliminar_tarea(self):
        tareas.clear()  # limpiar antes de probar
        tarea1 = crear_tarea("Tarea 1", "Descripción 1", "2025-05-01")
        eliminar_tarea(tarea1)
        self.assertEqual(len(tareas), 0)

if __name__ == '__main__':
    unittest.main()
