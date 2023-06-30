import tkinter as tk
from tkinter import ttk
from pacientes import Ventana
from propietarios import Propietarios

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación")
        self.geometry("800x500")

        self.frame_actual = None

        self.crear_frame1()

    def crear_frame1(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual = Frame1(self)
        self.frame_actual.grid(row=0, column=0, sticky='nsew')

    def crear_frame2(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual =  Ventana(self)
        self.frame_actual.grid(row=0, column=0, sticky='nsew')

    def crear_frame3(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual =  Propietarios(self)
        self.frame_actual.grid(row=0, column=0, sticky='nsew')


class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Bienvenido al sistema de veterinaria", fg= 'black', bg='white',
            font=('Arial', 20,'bold')).grid(column=1,row=0)

        button = tk.Button(self, text="Pacientes", command=master.crear_frame2, font= ('Arial', 9, 'bold'), width=30,
            bd=10 ).grid(column=2, row=2)

        button = tk.Button(self, text="Propietarios", command=master.crear_frame3, font= ('Arial', 9, 'bold'), width=30,
            bd=10 ).grid(column=2, row=3)


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
