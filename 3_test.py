import tkinter as tk
from tkinter import ttk, messagebox
import csv

class DomiciliarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tu App segura de Domiciliarios")
        
        # Crear las pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.registro_frame = ttk.Frame(self.notebook)
        self.calificacion_frame = ttk.Frame(self.notebook)
        self.seleccion_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.registro_frame, text="Registro Domiciliario")
        self.notebook.add(self.calificacion_frame, text="Calificar Domiciliarios")
        self.notebook.add(self.seleccion_frame, text="Seleccionar Domiciliario")
        
        # Variables para almacenar los datos del domiciliario
        self.nombre_var = tk.StringVar()
        self.cedula_var = tk.StringVar()
        self.placas_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.direccion_var = tk.StringVar()
        self.experiencia_var = tk.StringVar()

        # Frame para el registro de domiciliario
        registro_label_frame = ttk.LabelFrame(self.registro_frame, text="Registro de Domiciliario")
        registro_label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Campos de entrada para el registro
        tk.Label(registro_label_frame, text="Nombre completo:").grid(row=0, column=0, sticky="w")
        tk.Entry(registro_label_frame, textvariable=self.nombre_var).grid(row=0, column=1)

        tk.Label(registro_label_frame, text="Cédula:").grid(row=1, column=0, sticky="w")
        tk.Entry(registro_label_frame, textvariable=self.cedula_var).grid(row=1, column=1)

        tk.Label(registro_label_frame, text="Placas de vehículo:").grid(row=2, column=0, sticky="w")
        tk.Entry(registro_label_frame, textvariable=self.placas_var).grid(row=2, column=1)

        tk.Label(registro_label_frame, text="Teléfono:").grid(row=3, column=0, sticky="w")
        tk.Entry(registro_label_frame, textvariable=self.telefono_var).grid(row=3, column=1)

        tk.Label(registro_label_frame, text="Dirección:").grid(row=4, column=0, sticky="w")
        tk.Entry(registro_label_frame, textvariable=self.direccion_var).grid(row=4, column=1)

        tk.Label(registro_label_frame, text="Experiencia:").grid(row=5, column=0, sticky="w")
        tk.Entry(registro_label_frame, textvariable=self.experiencia_var).grid(row=5, column=1)

        # Botón para registrar domiciliario
        tk.Button(self.registro_frame, text="Registrar Domiciliario", command=self.registrar_domiciliario).pack(pady=10)

        # Lista para almacenar domiciliarios y sus calificaciones
        self.domiciliarios = []

        # Frame para calificar domiciliarios
        calificacion_label_frame = ttk.LabelFrame(self.calificacion_frame, text="Calificar Domiciliarios")
        calificacion_label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.calificacion_listbox = tk.Listbox(calificacion_label_frame, width=40)
        self.calificacion_listbox.pack(pady=10)

        self.calificacion_scale = tk.Scale(calificacion_label_frame, from_=1, to=5, orient=tk.HORIZONTAL, label="Calificación")
        self.calificacion_scale.pack()

        tk.Button(calificacion_label_frame, text="Calificar", command=self.calificar_domiciliario).pack(pady=10)

        # Frame para seleccionar domiciliario y mostrar calificación
        seleccion_label_frame = ttk.LabelFrame(self.seleccion_frame, text="Seleccionar Domiciliario")
        seleccion_label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(seleccion_label_frame, columns=('Calificación',))
        self.treeview.heading('#0', text='Nombre')
        self.treeview.heading('Calificación', text='Calificación')
        self.treeview.pack(pady=10)

        # Cargar datos previos de un archivo CSV
        self.cargar_datos_csv()
        self.actualizar_lista_domiciliarios()

        # Configurar la función de seleccionar un item del Treeview
        self.treeview.bind('<ButtonRelease-1>', self.mostrar_datos_domiciliario)

    def registrar_domiciliario(self):
        # Obtener datos del registro
        nombre = self.nombre_var.get()
        cedula = self.cedula_var.get()
        placas = self.placas_var.get()
        telefono = self.telefono_var.get()
        direccion = self.direccion_var.get()
        experiencia = self.experiencia_var.get()

        # Validar que todos los campos estén llenos
        if nombre and cedula and placas and telefono and direccion and experiencia:
            domiciliario = {
                'nombre': nombre,
                'cedula': cedula,
                'placas': placas,
                'telefono': telefono,
                'direccion': direccion,
                'experiencia': experiencia,
                'calificacion': '',
            }
            self.domiciliarios.append(domiciliario)
            self.guardar_datos_csv()
            messagebox.showinfo("Registro Exitoso", "Domiciliario registrado correctamente.")
            self.limpiar_campos_registro()
            self.actualizar_lista_domiciliarios()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def limpiar_campos_registro(self):
        self.nombre_var.set("")
        self.cedula_var.set("")
        self.placas_var.set("")
        self.telefono_var.set("")
        self.direccion_var.set("")
        self.experiencia_var.set("")

    def calificar_domiciliario(self):
        selected_index = self.calificacion_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            calificacion = self.calificacion_scale.get()
            self.domiciliarios[index]['calificacion'] = calificacion
            self.guardar_datos_csv()
            messagebox.showinfo("Calificación Registrada", "Calificación registrada correctamente.")
            self.calificacion_listbox.delete(0, tk.END)
            self.actualizar_lista_domiciliarios()

    def mostrar_datos_domiciliario(self, event):
        item = self.treeview.selection()[0]
        domiciliario_nombre = self.treeview.item(item, 'text')
        if domiciliario_nombre:
            for domiciliario in self.domiciliarios:
                if domiciliario['nombre'] == domiciliario_nombre:
                    messagebox.showinfo("Datos del Domiciliario", f"""
                    Nombre: {domiciliario['nombre']}
                    Cédula: {domiciliario['cedula']}
                    Placas de vehículo: {domiciliario['placas']}
                    Teléfono: {domiciliario['telefono']}
                    Dirección: {domiciliario['direccion']}
                    Experiencia: {domiciliario['experiencia']}
                    Calificación: {domiciliario['calificacion']}
                    """)

    def guardar_datos_csv(self):
        with open('domiciliarios.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nombre', 'cedula', 'placas', 'telefono', 'direccion', 'experiencia', 'calificacion'])
            writer.writeheader()
            for domiciliario in self.domiciliarios:
                writer.writerow(domiciliario)

    def cargar_datos_csv(self):
        try:
            with open('domiciliarios.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.domiciliarios.append(row)
                self.actualizar_lista_domiciliarios()
        except FileNotFoundError:
            print("Archivo CSV no encontrado, se creará al guardar datos.")

    def actualizar_lista_domiciliarios(self):
        self.calificacion_listbox.delete(0, tk.END)
        self.treeview.delete(*self.treeview.get_children())
        for domiciliario in self.domiciliarios:
            self.calificacion_listbox.insert(tk.END, domiciliario['nombre'])
            self.treeview.insert('', 'end', text=domiciliario['nombre'], values=(domiciliario['calificacion'],))

# Inicialización de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = DomiciliarioApp(root)
    
    # Configurar el icono de la ventana
    root.iconbitmap('c:\Users\labinf1.pasto\Documents\k\icono')


    
    root.mainloop()

   