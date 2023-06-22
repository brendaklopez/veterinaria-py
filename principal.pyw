import tkinter as tk
from tkinter import ttk

class Ventana(tk.Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.Nombre = tk.StringVar()
        self.Especie = tk.StringVar()
        self.Raza = tk.StringVar()
        self.Edad = tk.StringVar()
        self.IDPropietario = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)

        self.widgets()

    def widgets(self):
        self.frame_uno = tk.Frame(self, bg='white', height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')

        self.frame_dos = tk.Frame(self, bg='white', height=300, width=800)
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)

        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        tk.Label(self.frame_uno, text='Opciones', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(column=2, row=0)
        tk.Button(self.frame_uno, text='Actualizar', fg='black', bg='violet', width=20, bd=3).grid(column=2, row=1, pady=5)
        tk.Label(self.frame_uno, text='Agregar y actualizar pacientes', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        tk.Label(self.frame_uno, text='Nombre', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(column=0, row=1, pady=5)
        tk.Label(self.frame_uno, text='Especie', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(column=0, row=2, pady=5)
        tk.Label(self.frame_uno, text='Raza', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(column=0, row=3, pady=5)
        tk.Label(self.frame_uno, text='Edad', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(column=0, row=4, pady=5)
        tk.Label(self.frame_uno, text='Dueño', fg='black', bg='white', font=('Arial', 13, 'bold')).grid(column=0, row=5, pady=5)

        tk.Button(self.frame_uno, text='Añadir paciente', font=('Arial', 9, 'bold'), width=20, bd=3).grid(column=2, row=2, pady=5, padx=5)
        tk.Button(self.frame_uno, text='Limpiar campos', font=('Arial', 9, 'bold'), width=20, bd=3).grid(column=2, row=3, pady=5, padx=5)
        tk.Button(self.frame_uno, text='Actualizar datos', font=('Arial', 9, 'bold'), width=20, bd=3).grid(column=2, row=4, pady=5, padx=5)

        tk.Entry(self.frame_uno, textvariable=self.Nombre, font=('Comic Sans', 12)).grid(column=1, row=1)
        tk.Entry(self.frame_uno, textvariable=self.Especie, font=('Comic Sans', 12)).grid(column=1, row=2)
        tk.Entry(self.frame_uno, textvariable=self.Raza, font=('Comic Sans', 12)).grid(column=1, row=3)
        tk.Entry(self.frame_uno, textvariable=self.Edad, font=('Comic Sans', 12)).grid(column=1, row=4)
        tk.Entry(self.frame_uno, textvariable=self.IDPropietario, font=('Comic Sans', 12)).grid(column=1, row=5)

        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Especie', 'Raza', 'Edad', 'Dueño')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Especie', minwidth=100, width=120, anchor='center')
        self.tabla.column('Raza', minwidth=100, width=120, anchor='center')
        self.tabla.column('Edad', minwidth=100, width=120, anchor='center')
        self.tabla.column('Dueño', minwidth=100, width=120, anchor='center')

        self.tabla.heading('#0', text='Nombre', anchor='center')
        self.tabla.heading('Especie', text='Especie', anchor='center')
        self.tabla.heading('Raza', text='Raza', anchor='center')
        self.tabla.heading('Edad', text='Edad', anchor='center')
        self.tabla.heading('Dueño', text='Dueño', anchor='center')


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
        self.frame_actual.grid(row=0, column=0)

    def crear_frame2(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual = Frame2(self)
        self.frame_actual.grid(row=0, column=0)


class Frame1(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        label = tk.Label(self, text="Estás en el Frame 1")
        label.grid(row=0, column=0)

        button = tk.Button(self, text="Ir al Frame 2", command=master.crear_frame2)
        button.grid(row=1, column=0)


class Frame2(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.ventana = Ventana(self)
        self.ventana.grid(row=0, column=0)


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
