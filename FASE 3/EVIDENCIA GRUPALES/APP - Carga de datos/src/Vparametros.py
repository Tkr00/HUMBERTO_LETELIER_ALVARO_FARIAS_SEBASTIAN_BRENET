import tkinter as tk
from tkinter import *
from Funciones.secundarias import fecha_actual, configuracion, guardar_data, resourcePath
from constantes import style
from tkinter import messagebox





### PESTAÑA PARA PARAMETROS
class VentanaSecundaria(tk.Toplevel):
    en_uso = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("PARAMETROS")
        self.geometry("360x220")
        self.icono = tk.PhotoImage(file=resourcePath("assets/4k.gif"))
        self.iconphoto(True, self.icono)
        self.configure(background=style.BACKGROUND)
        self.resizable(False, False)
        self.sec_widgets()
        self.mostrar_config()


        self.focus()
        self.__class__.en_uso = True

    def destroy(self):
        self.__class__.en_uso = False
        return super().destroy()
    
    def sec_widgets(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

        ### LABEL USUARIO
        self.label_user = tk.Label(
            self,
            text="Usuario: "
        )
        self.label_user.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.entry_user = tk.Entry(self, width=30)
        self.entry_user.grid(row=1, column=2, padx=10, pady=10)

        ### LABEL CONTRASEÑA
        self.label_password = tk.Label(
            self,
            text="Contraseña: "
        )
        self.label_password.grid(row=2, column=1, sticky="e", padx=10, pady=10)

        self.entry_password = tk.Entry(self, show="*", width=30)
        self.entry_password.grid(row=2, column=2, padx=10, pady=10)

        ### LABEL TIEMPO
        self.label_tiempo_lectura = tk.Label(
            self,
            text="Tiempo: "
        )
        self.label_tiempo_lectura.grid(row=3, column=1, sticky="e", padx=10, pady=10)

        self.entry_tiempo_lectura = tk.Entry(self, width=30)
        self.entry_tiempo_lectura.grid(row=3, column=2, padx=10, pady=10)

        ### BOTÓN GUARDAR
        self.btn_guardar = tk.Button(
            self,
            text="Guardar",
            command=self.guardar_datos,
            width=15
        )
        self.btn_guardar.grid(row=4, column=1, columnspan=2, pady=20)


    ### FUNCION PARA GUARDAR PARAMETROS
    def guardar_datos(self):
        fecha_hora = fecha_actual()
        try:
            user = self.entry_user.get()
            password = self.entry_password.get()
            tiempo = self.entry_tiempo_lectura.get()

            parametros = {"user":user,"password":password,"tiempo":tiempo}
            guardar_data(parametros)
            messagebox.showinfo(message="Datos guardados", title="Guardado Exitoso")
        except Exception as ex:
            print(f"{fecha_hora}Ha ocurrido el siguiente error: {ex}")
            messagebox.showerror(message="Ha ocurrido un error al intentar guardo los datos", title='ERROR')
            return
        self.destroy()


    ### FUNCIÓN PARA MOSTRAR CONFIGURACIÓN
    def mostrar_config(self):
        v_parametros = configuracion()
        user = v_parametros["user"]
        password = v_parametros["password"]
        tiempo = v_parametros["tiempo"]

        self.entry_user.insert(0, user)
        self.entry_password.insert(0, password)
        self.entry_tiempo_lectura.insert(0, tiempo)