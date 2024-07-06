import tkinter as tk
from tkinter import ttk, messagebox

# Lista para almacenar los domiciliarios registrados
domiciliarios = []

class Domiciliario:
    def __init__(self, nombre, cedula, placas, telefono, direccion, experiencia):
        self.nombre = nombre
        self.cedula = cedula
        self.placas = placas
        self.telefono = telefono
        self.direccion = direccion
        self.experiencia = experiencia
        self.calificacion = None
    
    def solicitar_servicio(self):
        # Simulación de solicitud de servicio
        return f"{self.nombre} ha sido solicitado para un servicio."

# Función para registrar un domiciliario
def registrar_domiciliario():
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    placas = entry_placas.get()
    telefono = entry_telefono.get()
    direccion = entry_direccion.get()
    experiencia = entry_experiencia.get()
    
    # Validar que no haya campos vacíos
    if not nombre or not cedula or not placas or not telefono or not direccion or not experiencia:
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return
    
    # Crear instancia de Domiciliario y añadir a la lista
    domiciliario = Domiciliario(nombre, cedula, placas, telefono, direccion, experiencia)
    domiciliarios.append(domiciliario)
    
    messagebox.showinfo("Registro exitoso", f"El domiciliario {nombre} ha sido registrado.")

# Función para mostrar domiciliarios por calificación
def mostrar_domiciliarios_por_calificacion():
    # Crear una nueva ventana para mostrar los domiciliarios por calificación
    ventana_calificaciones = tk.Toplevel(root)
    ventana_calificaciones.title("Domiciliarios por calificación")
    
    # Mostrar domiciliarios ordenados por calificación
    domiciliarios_ordenados = sorted(domiciliarios, key=lambda x: x.calificacion if x.calificacion is not None else 0, reverse=True)
    
    for i, domiciliario in enumerate(domiciliarios_ordenados):
        label_info = tk.Label(ventana_calificaciones, text=f"{i+1}. {domiciliario.nombre} - Calificación: {domiciliario.calificacion}")
        label_info.pack(padx=10, pady=5, anchor="w")

# Crear la ventana principal
root = tk.Tk()
root.title("Registro y búsqueda de domiciliarios")

# Crear un Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10)

# Pestaña para registrar domiciliario
frame_registro = ttk.Frame(notebook)
notebook.add(frame_registro, text='Registrar Domiciliario')

# Etiquetas y campos de entrada en la pestaña de registro
label_nombre = tk.Label(frame_registro, text="Nombre completo:")
label_cedula = tk.Label(frame_registro, text="Cedula:")
label_placas = tk.Label(frame_registro, text="Placas de vehículo:")
label_telefono = tk.Label(frame_registro, text="Teléfono:")
label_direccion = tk.Label(frame_registro, text="Dirección:")
label_experiencia = tk.Label(frame_registro, text="Experiencia:")

label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
label_cedula.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
label_placas.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
label_telefono.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
label_direccion.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
label_experiencia.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

entry_nombre = tk.Entry(frame_registro, width=30)
entry_cedula = tk.Entry(frame_registro, width=30)
entry_placas = tk.Entry(frame_registro, width=30)
entry_telefono = tk.Entry(frame_registro, width=30)
entry_direccion = tk.Entry(frame_registro, width=30)
entry_experiencia = tk.Entry(frame_registro, width=30)

entry_nombre.grid(row=0, column=1, padx=10, pady=5)
entry_cedula.grid(row=1, column=1, padx=10, pady=5)
entry_placas.grid(row=2, column=1, padx=10, pady=5)
entry_telefono.grid(row=3, column=1, padx=10, pady=5)
entry_direccion.grid(row=4, column=1, padx=10, pady=5)
entry_experiencia.grid(row=5, column=1, padx=10, pady=5)

# Botón para registrar domiciliario
btn_registrar = tk.Button(frame_registro, text="Registrar domiciliario", command=registrar_domiciliario)
btn_registrar.grid(row=6, column=0, columnspan=2, pady=10)

# Pestaña para buscar domiciliarios por calificación
frame_calificacion = ttk.Frame(notebook)
notebook.add(frame_calificacion, text='Buscar por Calificación')

# Botón para mostrar domiciliarios por calificación
btn_mostrar_calificacion = tk.Button(frame_calificacion, text="Mostrar por Calificación", command=mostrar_domiciliarios_por_calificacion)
btn_mostrar_calificacion.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
