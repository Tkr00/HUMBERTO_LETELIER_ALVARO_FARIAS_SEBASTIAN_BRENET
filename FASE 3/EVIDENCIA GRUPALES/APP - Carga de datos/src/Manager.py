import tkinter as tk
import sys
from tkinter import *
from tkinter import scrolledtext
from Funciones.principales import main, fecha_actual, cerrar_conexion
from Funciones.secundarias import fecha_actual, configuracion, resourcePath, guardar_data2, configuracion2
from constantes import style
from tkinter import messagebox
import threading
from tkinter import filedialog
import json
from src.Vparametros import VentanaSecundaria







### PESTAÑA PRINCIPAL
class App(tk.Tk):


    ### INICIALIZACION DE APP  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Carga de datos")
        self.icono = tk.PhotoImage(file=resourcePath("assets/4k.gif"))
        self.iconphoto(True, self.icono)
        self.geometry("854x480")
        self.resizable(False, False)
        self.configure(background=style.BACKGROUND)
        self.init_widgets() 
        self.iniciar()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.mostrar_config()
        


    ### WIDGETS
    def init_widgets(self):
        ### FRAME ENCABEZADO
        Frame1 = tk.Frame(self)
        Frame1.configure(background=style.COMPONENT)
        Frame1.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=5,
            pady=5
        )

        ### LABEL PARA ARCHIVO
        self.label_path = tk.Label(
            Frame1,
            text="ARCHIVO:",
            bg=style.COMPONENT,
            fg=style.TEXT
        )
        self.label_path.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ### ENTRY PARA MOSTRAR LA RUTA
        self.entry_path = tk.Entry(Frame1, state="readonly", width=50)
        self.entry_path.grid(row=0, column=1, padx=10, pady=10)

        ### BOTÓN PARA SELECCIONAR ARCHIVO
        self.btn_seleccionar_archivo = tk.Button(Frame1)
        self.btn_seleccionar_archivo.config(
            text="Seleccionar",
            command=self.seleccionar_archivo,
            **style.BTN_STYLE,
            activebackground="white",
            activeforeground=style.TEXT
        )
        self.btn_seleccionar_archivo.grid(row=0, column=2, padx=10, pady=10)


        Frame1.grid_columnconfigure(3, weight=1)

        ### BOTÓN PARAMETROS
        self.btn_parametros = tk.Button(Frame1)
        self.btn_parametros.config(
            text="Parametros",
            state=tk.NORMAL,
            width=10,
            height=1,
            command=self.abrir_ventana,
            **style.BTN_STYLE,
            activebackground="white",
            activeforeground=style.TEXT
        )
        self.btn_parametros.grid(row=0, column=4, padx=10, pady=10, sticky="e")

        ### FRAME PRINCIPAL
        Frame2 = tk.Frame(self)
        Frame2.configure(background=style.COMPONENT)
        Frame2.pack(
            expand=True,
            fill=tk.BOTH,
            padx=5,
            pady=5
        )

        # CONSOLA
        self.console_output = scrolledtext.ScrolledText(
            Frame2, wrap=tk.WORD, width=40, height=10
        )
        self.console_output.pack(
            expand=True,
            fill=tk.BOTH,
            padx=5,
            pady=5
        )
        sys.stdout = ConsoleRedirector(self.console_output)

        ### FRAME FOOTER
        Frame_footer = tk.Frame(self, height=80)
        Frame_footer.configure(background=style.COMPONENT)
        Frame_footer.pack_propagate(False)
        Frame_footer.pack(
            side=tk.BOTTOM,
            fill=tk.X,
            padx=5,
            pady=5
        )

        # ORGANIZAR BOTÓN
        Frame_footer.grid_rowconfigure(0, weight=1)
        Frame_footer.grid_columnconfigure(0, weight=1)
        Frame_footer.grid_columnconfigure(1, weight=1)
        Frame_footer.grid_columnconfigure(2, weight=1)
        Frame_footer.grid_columnconfigure(3, weight=1)

        # BOTÓN INICIAR
        self.btn_iniciar = tk.Button(Frame_footer)
        self.btn_iniciar.config(
            text="INICIAR",
            state=tk.NORMAL,
            width=12,
            height=2,
            command=self.iniciar,
            **style.BTN_STYLE,
            activebackground="white",
            activeforeground=style.TEXT
        )
        self.btn_iniciar.grid(row=0, column=0, padx=20, pady=10)

        # BOTÓN DETENER
        self.btn_detener = tk.Button(Frame_footer)
        self.btn_detener.config(
            text="DETENER",
            state=tk.NORMAL,
            width=12,
            height=2,
            command=self.stop,
            **style.BTN_STYLE,
            activebackground="white",
            activeforeground=style.TEXT
        )
        self.btn_detener.grid(row=0, column=1, padx=20, pady=10)

        # BOTÓN CERRAR
        self.btn_cerrar = tk.Button(Frame_footer)
        self.btn_cerrar.config(
            text="CERRAR",
            state=tk.NORMAL,
            width=12,
            height=2,
            command=self.on_close,
            **style.BTN_STYLE,
            activebackground="white",
            activeforeground=style.TEXT
        )
        self.btn_cerrar.grid(row=0, column=2, padx=20, pady=10)






    ### FUNCIÓN PARA MOSTRAR PATH
    def mostrar_config(self):
        v_parametros = configuracion2()
        direccion = v_parametros["path"]
        self.entry_path.config(state="normal")  # Cambiar a estado editable
        self.entry_path.delete(0, tk.END)       # Borrar el contenido actual
        self.entry_path.insert(0, direccion)    # Insertar la ruta obtenida
        self.entry_path.config(state="readonly")
        




    ### FUNCIÓN PARA ABRIR SEGUNDA VENTANA
    def abrir_ventana(self):
        if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()



    ### FUNCIÓN PARA ESCRIBIR EN PANTALLA
    def write(self, text):
        self.console_output.insert(tk.END, text)
        self.console_output.see(tk.END)
        self.update_idletasks()



    ### FUNCION PARA INICIAR PROCESO, CONEXION E INGRESO DE DATOS
    def iniciar(self):
        param = configuracion2()
        self.ruta_archivo = param["path"]
        #fecha_hora = fecha_actual()
        if self.ruta_archivo != "":
            
            try:
                self.btn_iniciar.config(state=tk.DISABLED)
                self.btn_cerrar.config(state=tk.DISABLED)    
                global timer_runs        
                timer_runs = threading.Event()
                timer_runs.set()
                t = threading.Thread(target=main, args=(timer_runs, self.ruta_archivo,))
                t.start()
            except Exception as ex:
                messagebox.showerror(message="Error al ingresar datos.", title='ERROR')
                print(f"Ha ocurrido el siguiente error: {ex}")
                return         
            
        else:
            messagebox.showwarning(message="No hay ningun archivo vinculado", title='WARNING')
    


    ### FUNCIÓN PARA DETENER PROCESO
    def stop(self):
        fecha_hora = fecha_actual()
        try:
            timer_runs.clear()
            cerrar_conexion()
            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_cerrar.config(state=tk.NORMAL)
        except Exception as ex:
            #print(f"{fecha_hora}: El proceso aun no ha sido ejecutado...")
            print("El proceso aun no ha sido ejecutado...")
            return
        

     ### FUNCIÓN PARA SELECCIONAR ARCHIVO   
    def seleccionar_archivo(self):
        try:
            # Mostrar cuadro de diálogo para seleccionar archivo
            file_path = filedialog.askopenfilename(
                title="Seleccionar archivo",
                filetypes=[("DAT files", "*.dat"), ("Todos los archivos", "*.*")]
            )
            if file_path:  # Si se seleccionó un archivo
                # Guardar la ruta en config.json
                config_path = resourcePath("config_path.json")
                try:
                    with open(config_path, "r") as file:
                        config_data = json.load(file)
                except FileNotFoundError:
                    config_data = {}

                # Actualizar el JSON con la nueva ruta
                config_data["path"] = file_path
                with open(config_path, "w") as file:
                    json.dump(config_data, file, indent=4)

                # Actualizar el contenido del Entry
                self.entry_path.config(state="normal")  # Cambiar a estado editable
                self.entry_path.delete(0, tk.END)       # Borrar el contenido actual
                self.entry_path.insert(0, file_path)    # Insertar la nueva ruta
                self.entry_path.config(state="readonly")  # Volver a readonly

                # Mostrar mensaje de éxito
                messagebox.showinfo(
                    message=f"Archivo Seleccionado",
                    title="Éxito"
                )
            else:
                messagebox.showwarning(
                    message="No se seleccionó ningún archivo",
                    title="Advertencia"
                )
        except Exception as ex:
            messagebox.showerror(
                message=f"Error al seleccionar el archivo: {ex}",
                title="Error"
            )




    ### FUNCION DE CERRADA DE APP
    def on_close(self):
        try:
            timer_runs.clear()
            cerrar_conexion()
        except:
            print("")
        # CERRA APP
        self.destroy()    


### CLASE PARA REDIRIGIR MENSAJES DE CONSOLA
class ConsoleRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text + '\n')
        self.text_widget.see(tk.END)
    
    def flush(self):
        pass

