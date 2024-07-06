import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido")
        self.root.geometry("400x300")  # Tamaño de la ventana de bienvenida

        self.root.iconbitmap('C:/Users/labinf1.pasto/Documents/k/Protecyo/icono/moto.ico')

        # Establecer el color de fondo azul claro
        self.root.configure(background='light blue')

        # Cargar la imagen de marca de agua (simulación)
        watermark_img = Image.open('watermark.png')  # Ajusta la ruta según tu imagen
        watermark_img = watermark_img.resize((400, 300), Image.LANCZOS)  # Redimensionar la imagen con LANCZOS
        self.watermark_photo = ImageTk.PhotoImage(watermark_img)

        # Mostrar la imagen de marca de agua en la ventana de bienvenida
        self.watermark_label = tk.Label(self.root, image=self.watermark_photo, bg='light blue')
        self.watermark_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Crear un Canvas para el fondo semi transparente
        self.canvas = tk.Canvas(self.root, width=380, height=120, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Añadir un rectángulo semi transparente al Canvas
        self.canvas.create_rectangle(0, 0, 380, 120, fill='light blue', outline='')  # Ajusta el color y la transparencia

        # Etiqueta de bienvenida y descripción
        self.canvas.create_text(190, 50, text="Bienvenido a tu App Segura de Domiciliarios",
                                font=('Arial', 16, 'bold'), fill='sea green', justify='center')

        self.canvas.create_text(190, 95, text="Esta app te permitirá registrarte como domiciliario y ofrecer tus servicios de manera formal.\n" 
                                               "También podrás calificar al domiciliario una vez hayas hecho uso de su servicio.",
                                font=('Arial', 12), fill='black', justify='center')

        # Botón para cerrar la ventana y abrir la aplicación principal
        ttk.Button(self.root, text="Iniciar App", command=self.close_and_open_main_app).place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    def close_and_open_main_app(self):
        self.root.destroy()  # Cerrar la ventana de bienvenida
        root = tk.Tk()
        app = DomiciliarioApp(root)
        root.mainloop()

class DomiciliarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tu App segura de Domiciliarios")
        self.root.geometry("400x400")  # Establecer el tamaño inicial de la ventana

        # Configuración del ícono de la ventana
        self.root.iconbitmap('C:/Users/labinf1.pasto/Documents/k/Protecyo/icono/moto.ico')

        # Configuración de estilo
        self.estilo = ttk.Style()
        self.estilo.configure('Estilo.TNotebook', background='light blue')  # Fondo de las pestañas
        self.estilo.configure('Estilo.TFrame', background='light blue')
        self.estilo.configure('Estilo.TLabelFrame', background='white')      # Fondo de los frames dentro de las pestañas

        # Crear las pestañas
        self.notebook = ttk.Notebook(root, style='Estilo.TNotebook')
        self.notebook.pack(padx=12, pady=12, fill=tk.BOTH, expand=True)

        self.registro_frame = ttk.Frame(self.notebook, style='Estilo.TFrame')
        self.calificacion_frame = ttk.Frame(self.notebook, style='Estilo.TFrame')
        self.seleccion_frame = ttk.Frame(self.notebook, style='Estilo.TFrame')

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
        ttk.Label(registro_label_frame, text="Nombre:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(registro_label_frame, textvariable=self.nombre_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(registro_label_frame, text="Cédula:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(registro_label_frame, textvariable=self.cedula_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(registro_label_frame, text="Placas de vehículo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(registro_label_frame, textvariable=self.placas_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(registro_label_frame, text="Teléfono:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(registro_label_frame, textvariable=self.telefono_var).grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(registro_label_frame, text="Dirección:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(registro_label_frame, textvariable=self.direccion_var).grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(registro_label_frame, text="Experiencia (meses):").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(registro_label_frame, textvariable=self.experiencia_var).grid(row=5, column=1, padx=5, pady=5)

        # Botón para registrar domiciliario
        tk.Button(self.registro_frame, text="Registrar Domiciliario", command=self.registrar_domiciliario, bg="blue", fg="white").pack(pady=10)

        # Lista para almacenar domiciliarios y sus calificaciones (simulación)
        self.domiciliarios = []

        # Frame para calificar domiciliarios
        calificacion_label_frame = ttk.LabelFrame(self.calificacion_frame, text="Calificar Domiciliarios")
        calificacion_label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.calificacion_listbox = tk.Listbox(calificacion_label_frame, width=40)
        self.calificacion_listbox.pack(pady=10)

        self.calificacion_scale = ttk.Scale(calificacion_label_frame, from_=1, to=5, orient=tk.HORIZONTAL, length=200)
        self.calificacion_scale.pack()
        ttk.Label(calificacion_label_frame, text="Calificación (1-5)").pack()

        tk.Button(calificacion_label_frame, text="Calificar", command=self.calificar_domiciliario, bg="green", fg="white").pack(pady=10)

        # Frame para seleccionar domiciliario y mostrar calificación
        seleccion_label_frame = ttk.LabelFrame(self.seleccion_frame, text="Seleccionar Domiciliario")
        seleccion_label_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.treeview = ttk.Treeview(seleccion_label_frame, columns=('Calificación',))
        self.treeview.heading('#0', text='Nombre')
        self.treeview.heading('Calificación', text='Calificación')
        self.treeview.pack(pady=10)

        # Cargar datos previos de un archivo CSV (simulación)
        self.cargar_datos_csv()
        self.actualizar_lista_domiciliarios()

        # Configurar la función de seleccionar un item del Treeview (simulación)
        self.treeview.bind('<ButtonRelease-1>', self.mostrar_datos_domiciliario)

    def registrar_domiciliario(self):
        # Obtener datos del registro (simulación)
        nombre = self.nombre_var.get()
        cedula = self.cedula_var.get()
        # Resto del código para el registro...

    def calificar_domiciliario(self):
        # Función para calificar un domiciliario (simulación)
        pass

    def mostrar_datos_domiciliario(self, event):
        # Función para mostrar los datos de un domiciliario seleccionado (simulación)
        pass

    def cargar_datos_csv(self):
        # Función para cargar datos previos desde un archivo CSV (simulación)
        pass

    def actualizar_lista_domiciliarios(self):
        # Función para actualizar la lista de domiciliarios en la interfaz (simulación)
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()
