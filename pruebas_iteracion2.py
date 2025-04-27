import unittest
import tkinter as tk

class TestGUI(unittest.TestCase):
    def test_ventana_principal_creada(self):
        ventana = tk.Tk()
        self.assertIsInstance(ventana, tk.Tk)
        ventana.destroy()
    def test_botones_existentes(self):
        ventana = tk.Tk()

        boton_agregar = tk.Button(ventana, text="Agregar tarea")
        boton_visualizar = tk.Button(ventana, text="Visualizar tareas")
        boton_editar = tk.Button(ventana, text="Editar tarea")
        boton_eliminar = tk.Button(ventana, text="Eliminar tarea")

        self.assertEqual(boton_agregar["text"], "Agregar tarea")
        self.assertEqual(boton_visualizar["text"], "Visualizar tareas")
        self.assertEqual(boton_editar["text"], "Editar tarea")
        self.assertEqual(boton_eliminar["text"], "Eliminar tarea")
        ventana.destroy()
    
    def test_botones_tienen_comando(self):
        ventana = tk.Tk()

        def dummy_function():
            pass

        boton_agregar = tk.Button(ventana, text="Agregar tarea", command=dummy_function)
        boton_visualizar = tk.Button(ventana, text="Visualizar tareas", command=dummy_function)
        boton_editar = tk.Button(ventana, text="Editar tarea", command=dummy_function)
        boton_eliminar = tk.Button(ventana, text="Eliminar tarea", command=dummy_function)

        self.assertIsNotNone(boton_agregar["command"])
        self.assertIsNotNone(boton_visualizar["command"])
        self.assertIsNotNone(boton_editar["command"])
        self.assertIsNotNone(boton_eliminar["command"])

        ventana.destroy()


if __name__ == '__main__':
    unittest.main()
