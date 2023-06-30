from tkinter import Tk, Button, Entry, Label, ttk, StringVar, Scrollbar, Frame
from conexion import Conexion

class Aplicacion(Frame):
    def __init__(self, master, *args):
        super(). __init__(master, *args)
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1,weight=5)

    def volver(self):
        self.master.destroy()
        root = Tk()
        root.geometry("800x500")
        root.title("Sistema de veterinaria")
        app = Menu(master=root)
        app.mainloop()
        
    def config_widgets(self):
        self.frame_uno = Frame(self.master, bg='white',height=200,width=800)
        self.frame_uno.grid(column=0,row=0,sticky='nsew')
        self.frame_dos=Frame(self.master, bg='white', height=300, width=800)
        self.frame_dos.grid(column=0,row=1,sticky='nsew')
        self.frame_uno.columnconfigure([0,1,2],weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame_dos.columnconfigure(0,weight=1)
        self.frame_dos.rowconfigure(0,weight=1)
        
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox= ttk.Scrollbar(self.frame_dos, orient= 'horizontal', command= self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy= ttk.Scrollbar(self.frame_dos, orient= 'vertical', command= self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand = ladox.set,yscrollcommand= ladoy.set )
        
        Button(self.frame_uno, text='Añadir Nuevo', command= self.agregar_datos, font= ('Arial', 9, 'bold'), width=20,
               bd=3 ).grid(column=2, row=1, pady= 5, padx=5)
        Button(self.frame_uno, text='Limpiar campos', command =self.limpiar_campos,font= ('Arial', 9, 'bold'), width=20,
               bd=3 ).grid(column=2, row=2, pady= 5, padx=5)
        Button(self.frame_uno, text='Eliminar', command = self.eliminar_fila,font= ('Arial', 9, 'bold'), width=20,
               bd=3 ).grid(column=2, row=3, pady= 5, padx=5)
        Button(self.frame_uno, text='Modificar', command= self.modificar, font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=4, pady= 5, padx=5)
        Button(self.frame_uno, text='Atras', command= self.volver, font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=5, pady= 5, padx=5)

class Turnos(Aplicacion):
    def __init__(self, master, *args):
        super(). __init__(master, *args)
        self.fecha = StringVar()
        self.hora = StringVar()
        self.selection_servicios= StringVar()
        self.selection_mascota = StringVar()
        self.mascotas= {}
        self.Servicios= {}
        self.bd=Conexion()
        self.widgets()
        self.actualizar_tabla()

    def limpiar_campos(self):
        self.hora.set('')
        self.fecha.set('')

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.bd.mostrar_citas()
        self.tabla.delete(*self.tabla.get_children())
        for i in range(len(datos)):
            self.tabla.insert('', i, text=datos[i][0], values=datos[i][1:5])
    
    def agregar_datos(self):
        self.cargar_macotas()
        self.cargar_servicios()
        fecha = self.fecha.get()
        hora = self.hora.get()
        mascota = [m['Id'] for m in self.mascotas if m['Nombre'] == self.selected_option.get()][0]
        servicio = [s['Id'] for s in self.Servicios if m['Descripcion'] == self.selected_option.get()][0]
        self.bd.insertar_cita(fecha, hora, mascota,servicio)
        self.limpiar_campos()
        self.actualizar_tabla()

    def eliminar_fila(self):
        pass

    def modificar(self):
        pass

    def obtener_fila(self):
        pass

    def cargar_macotas(self):
        db_rows = self.bd.mostrar_pacientes()
        self.mascotas = [{'Id': row[0], 'Nombre': row[1]} for row in db_rows]
        return self.mascotas

    def cargar_servicios(self):
        db_rows = self.bd.mostrar_servicios()
        self.Servicios = [{'Id': row[0], 'Descripcion': row[1]} for row in db_rows]
        return self.Servicios

    def widgets(self):
        super().config_widgets()
        Label(self.frame_uno, text = 'Opciones', fg= 'black', bg='white',
            font=('Arial', 13,'bold')).grid(column=2,row=0)
        Label(self.frame_uno, text = 'TURNOS', fg= 'black', bg='white',
            font=('Arial', 13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
        Label(self.frame_uno,text= 'Fecha', fg='black', bg='white',
            font=('Arial', 13, 'bold')).grid(column=0,row=1, pady=5)
        Label(self.frame_uno,text= 'Hora', fg='black', bg='white',
            font=('Arial', 13, 'bold')).grid(column=0,row=2, pady=5)
        Label(self.frame_uno,text= 'Mascota', fg='black', bg='white',
            font=('Arial', 13, 'bold')).grid(column=0,row=3, pady=5)
        Label(self.frame_uno,text= 'Servicio', fg='black', bg='white',
            font=('Arial', 13, 'bold')).grid(column=0,row=4, pady=5)

        Entry(self.frame_uno, textvariable=self.fecha, font=('Comic Sans', 12)).grid(column=1,row=1)
        Entry(self.frame_uno, textvariable=self.hora, font=('Comic Sans', 12)).grid(column=1,row=2)

        combo_mascotas = ttk.Combobox(self.frame_uno, textvariable=self.selection_mascota)
        combo_mascotas.grid(column=1, row=3)
        combo_servicios = ttk.Combobox(self.frame_uno, textvariable=self.selection_servicios)
        combo_servicios.grid(column=1, row=4)
        mascotas =self.cargar_macotas()
        combo_mascotas['values'] = [masc['Nombre'] for masc in mascotas]

        servicios =self.cargar_servicios()
        combo_servicios['values'] = [s['Descripcion'] for s in servicios]


        self.tabla['columns']= ('Fecha','Hora', 'Mascota','Servicio')
        self.tabla.column('#0',minwidth=100, width=120,anchor='center')
        self.tabla.column('Fecha',minwidth=100, width=120,anchor='center')
        self.tabla.column('Hora',minwidth=100, width=120,anchor='center')
        self.tabla.column('Mascota',minwidth=100, width=120,anchor='center')
        self.tabla.column('Servicio',minwidth=100, width=120,anchor='center')

        self.tabla.heading('#0',text='Id',anchor='center')
        self.tabla.heading('Fecha',text='Fecha',anchor='center')
        self.tabla.heading('Hora',text='Hora',anchor='center')
        self.tabla.heading('Mascota',text='Mascota',anchor='center')
        self.tabla.heading('Servicio',text='Servicio',anchor='center')

    
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)


class Servicios(Aplicacion):
    def __init__(self, master, *args):
        super(). __init__(master, *args)
        self.descripcion = StringVar()
        self.precio = StringVar()
        self.selected_option = StringVar()
        self.bd=Conexion()
        self.widgets()
        self.actualizar_tabla()

    def limpiar_campos(self):
        self.descripcion.set('')
        self.precio.set('')

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.bd.mostrar_servicios()
        self.tabla.delete(*self.tabla.get_children())
        for i in range(len(datos)):
            self.tabla.insert('', i, text=datos[i][0], values=datos[i][1:3])

    def agregar_datos(self):
        descripcion = self.descripcion.get()
        precio = self.precio.get()
        if descripcion and precio !='':
            self.bd.insertar_servicios(descripcion, precio)
            self.limpiar_campos()
            self.actualizar_tabla()

    def obtener_fila(self,event):
            item = self.tabla.focus()
            self.data = self.tabla.item(item)
            id_servicio = self.data['text']
            datos = self.bd.mostrar_servicios()
            for d in datos:
                Id = d[0]
                if Id == id_servicio:
                    self.descripcion.set(d[1])
                    self.precio.set(d[2])

    def eliminar_fila(self):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        self.data = self.tabla.item(item)
        id = self.data['text']
        self.tabla.delete(item)
        self.bd.eliminar_servicio(id)

    def modificar(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        Id = self.data['text']
        descripcion = self.descripcion.get()
        precio = self.precio.get()
        if descripcion and precio != '':
            self.bd.actualizar_servicios(Id, descripcion, precio)
            self.actualizar_tabla()
            self.limpiar_campos()

    def widgets(self):
        super().config_widgets()
        Label(self.frame_uno, text = 'Opciones', fg= 'black', bg='white',
            font=('Arial', 13,'bold')).grid(column=2,row=0)
        Label(self.frame_uno, text = 'SERVICIOS', fg= 'black', bg='white',
            font=('Arial', 13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
        Label(self.frame_uno,text= 'Descripcion', fg='black', bg='white',
            font=('Arial', 13, 'bold')).grid(column=0,row=1, pady=5)
        Label(self.frame_uno,text= 'Precio', fg='black', bg='white',
            font=('Arial', 13, 'bold')).grid(column=0,row=2, pady=5)

        Entry(self.frame_uno, textvariable=self.descripcion, font=('Comic Sans', 12)).grid(column=1,row=1)
        Entry(self.frame_uno, textvariable=self.precio, font=('Comic Sans', 12)).grid(column=1,row=2)

        self.tabla['columns']= ('Servicio','Precio')
        self.tabla.column('#0',minwidth=100, width=120,anchor='center')
        self.tabla.column('Servicio',minwidth=100, width=120,anchor='center')
        self.tabla.column('Precio',minwidth=100, width=120,anchor='center')

        self.tabla.heading('#0',text='Id',anchor='center')
        self.tabla.heading('Servicio',text='Servicio',anchor='center')
        self.tabla.heading('Precio',text='Precio',anchor='center')

        

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)

class Propietarios(Aplicacion):
    def __init__(self, master, *args):
        super(). __init__(master, *args)
        self.DNI = StringVar()
        self.Nombre = StringVar()
        self.Apellido = StringVar()
        self.Telefono = StringVar()
        self.Email = StringVar()
        self.bd=Conexion()
        self.widgets()
        self.actualizar_tabla()
        
    def limpiar_campos(self):
        self.DNI.set('')
        self.Nombre.set('')
        self.Apellido.set('')
        self.Telefono.set('')
        self.Email.set('')
        
    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.bd.mostrar_propietarios()
        self.tabla.delete(*self.tabla.get_children())
        for i in range(len(datos)):
              self.tabla.insert('', i, text=datos[i][0], values=datos[i][1:5])
              
    def agregar_datos(self): 
        dni = self.DNI.get()
        Nombre = self.Nombre.get()
        Apellido = self.Apellido.get()
        Email= self.Email.get()
        Telefono= self.Telefono.get()
        datos = (dni, Nombre, Apellido, Telefono, Email)
        if dni and Nombre and Apellido and Email and Telefono !='':
            self.bd.insertar_propietarios(dni, Nombre, Apellido,Telefono, Email)
            self.limpiar_campos()
            self.actualizar_tabla()
            
    def obtener_fila(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        id_propietarios = self.data['text']
        datos = self.bd.mostrar_propietarios()
        for d in datos:
            Id = d[0]
            if Id == id_propietarios:
                self.DNI.set(d[0])
                self.Nombre.set(d[1])
                self.Apellido.set(d[2])
                self.Telefono.set(d[3])
                self.Email.set(d[4])
                
    def eliminar_fila(self):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        self.data = self.tabla.item(item)
        id_propietario = self.data['text']
        self.tabla.delete(item)
        self.bd.eliminar_propietarios(id_propietario)
        
    def modificar(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        DNI = self.data['text']
        Nombre = self.Nombre.get()
        Apellido = self.Apellido.get()
        telefono = self.Telefono.get()
        email = self.Email.get()
        if DNI and Nombre and Apellido and telefono and email != '':
            self.bd.actualizar_propietario(DNI, Nombre, Apellido, telefono, email)
            self.actualizar_tabla()
            self.limpiar_campos()
            
            
    def widgets(self):
        super().config_widgets()
        Label(self.frame_uno, text = 'Opciones', fg= 'black', bg='white',
              font=('Arial', 13,'bold')).grid(column=2,row=0)
        Label(self.frame_uno, text = 'Agregar y actualizar propietarios', fg= 'black', bg='white',
              font=('Arial', 13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
        Label(self.frame_uno,text= 'DNI', fg='black', bg='white',
              font=('Arial', 13, 'bold')).grid(column=0,row=1, pady=5)
        Label(self.frame_uno,text= 'Nombre', fg='black', bg='white',
              font=('Arial', 13, 'bold')).grid(column=0,row=2, pady=5)
        Label(self.frame_uno,text='Apellido', fg='black', bg='white',
              font=('Arial', 13, 'bold')).grid(column=0,row=3, pady=5)
        Label(self.frame_uno,text='Telefono', fg='black', bg='white',
			font=('Arial', 13, 'bold')).grid(column=0,row=4, pady=5)
        Label(self.frame_uno,text='Email', fg='black', bg='white',
              font=('Arial', 13, 'bold')).grid(column=0,row=5, pady=5)
        
        Entry(self.frame_uno, textvariable=self.DNI, font=('Comic Sans', 12)).grid(column=1,row=1)
        Entry(self.frame_uno, textvariable=self.Nombre, font=('Comic Sans', 12)).grid(column=1,row=2)
        Entry(self.frame_uno, textvariable=self.Apellido, font=('Comic Sans', 12)).grid(column=1,row=3)
        Entry(self.frame_uno, textvariable=self.Telefono, font=('Comic Sans', 12)).grid(column=1,row=4)
        Entry(self.frame_uno, textvariable=self.Email, font=('Comic Sans', 12)).grid(column=1,row=5)
        
        self.tabla['columns']= ('Nombre', 'Apellido','Telefono','Email')
        self.tabla.column('#0',minwidth=100, width=120,anchor='center')
        self.tabla.column('Nombre',minwidth=100, width=120,anchor='center')
        self.tabla.column('Apellido',minwidth=100, width=120,anchor='center')
        self.tabla.column('Telefono',minwidth=100, width=120,anchor='center')
        self.tabla.column('Email',minwidth=100, width=120,anchor='center')
        self.tabla.heading('#0',text='DNI',anchor='center')
        self.tabla.heading('Nombre',text='Nombre',anchor='center')
        self.tabla.heading('Apellido',text='Apellido',anchor='center')
        self.tabla.heading('Telefono',text='Telefono',anchor='center')
        self.tabla.heading('Email',text='Email',anchor='center')
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
		# self.tabla.bind("<Double-1>", self.eliminar_fila)

class Pacientes(Aplicacion):
    def __init__(self, master, *args):
        super(). __init__(master, *args)
        self.Nombre = StringVar()
        self.Especie = StringVar()
        self.Raza = StringVar()
        self.Edad = StringVar()
        self.selected_option = StringVar()
        self.bd=Conexion()
        self.widgets()
        self.actualizar_tabla()
        self.Dueño = StringVar()
        self.propietarios = {}

    def limpiar_campos(self):
		# self.Dueño.configure(state="enabled")
        self.Nombre.set('')
        self.Edad.set('')
        self.Especie.set('')
        self.Raza.set('')

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.bd.mostrar_pacientes()
        self.tabla.delete(*self.tabla.get_children())
        for i in range(len(datos)):
            self.tabla.insert('', i, text=datos[i][0], values=datos[i][1:6])
        
# self.Dueño.configure(state="disabled")
    def obtener_fila(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        id_paciente = self.data['text']
        datos = self.bd.mostrar_pacientes()
        for d in datos:
            Id = d[0]
            if Id == id_paciente:
                self.Nombre.set(d[1])
                self.Especie.set(d[2])
                self.Raza.set(d[3])
                self.Edad.set(d[4])

    def eliminar_fila(self):
                self.limpiar_campos()
                item = self.tabla.selection()[0]
                self.data = self.tabla.item(item)
                id_paciente = self.data['text']
                self.tabla.delete(item)
                self.bd.eliminar_pacientes(id_paciente)

    def modificar(self):
                item = self.tabla.focus()
                self.data = self.tabla.item(item)
                id_paciente = self.data['text']
                Nombre = self.Nombre.get()
                Especie = self.Especie.get()
                Raza = self.Raza.get()
                Edad = self.Edad.get()
                if Nombre and Especie and Raza and Edad != '':
                    self.bd.actualizar_pacientes(id_paciente, Nombre, Especie, Raza, Edad)
                    self.actualizar_tabla()
                    self.limpiar_campos()

    def combo_input(self):
                db_rows = self.bd.mostrar_propietarios()
                self.propietarios = [{'DNI': row[0], 'Nombre': row[1]} for row in db_rows]
                return self.propietarios

    def agregar_datos(self):
        self.combo_input()
        Nombre = self.Nombre.get()
        Edad =self.Edad.get()
        Especie=self.Especie.get()
        Raza = self.Raza.get()
        Dueño = [propietario['DNI'] for propietario in self.propietarios if propietario['Nombre'] == self.selected_option.get()][0]
        datos = (Nombre, Especie, Raza, Edad, Dueño)
        if Nombre and Especie and Raza and Edad and Dueño !='':
            self.bd.insertar_pacientes(Nombre,Especie,Raza,Edad,Dueño)
            self.limpiar_campos()
            self.actualizar_tabla()

    def widgets(self):
                super().config_widgets()

                Label(self.frame_uno, text = 'Opciones', fg= 'black', bg='white',
                      font=('Arial', 13,'bold')).grid(column=2,row=0)
                Label(self.frame_uno, text = 'Agregar y actualizar pacientes', fg= 'black', bg='white',
                      font=('Arial', 13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
                Label(self.frame_uno,text= 'Nombre', fg='black', bg='white',
                      font=('Arial', 13, 'bold')).grid(column=0,row=1, pady=5)
                Label(self.frame_uno,text='Especie', fg='black', bg='white',
                      font=('Arial', 13, 'bold')).grid(column=0,row=2, pady=5)
                Label(self.frame_uno,text='Raza', fg='black', bg='white',
                      font=('Arial', 13, 'bold')).grid(column=0,row=3, pady=5)
                Label(self.frame_uno,text='Edad', fg='black', bg='white',
                      font=('Arial', 13, 'bold')).grid(column=0,row=4, pady=5)
                Label(self.frame_uno,text='Dueño', fg='black', bg='white',
                      font=('Arial', 13, 'bold')).grid(column=0,row=5, pady=5)

                Entry(self.frame_uno, textvariable=self.Nombre, font=('Comic Sans', 12)).grid(column=1,row=1)
                Entry(self.frame_uno, textvariable=self.Especie, font=('Comic Sans', 12)).grid(column=1,row=2)
                Entry(self.frame_uno, textvariable=self.Raza, font=('Comic Sans', 12)).grid(column=1,row=3)
                Entry(self.frame_uno, textvariable=self.Edad, font=('Comic Sans', 12)).grid(column=1,row=4)

                combobox = ttk.Combobox(self.frame_uno, textvariable=self.selected_option)
                combobox.grid(column=1, row=5)
                prop = self.combo_input()
                combobox['values'] = [propietario['Nombre'] for propietario in prop]
                self.tabla['columns']= ('Nombre', 'Especie','Raza','Edad', 'Dueño')
                self.tabla.column('#0',minwidth=100, width=120,anchor='center')
                self.tabla.column('Nombre',minwidth=100, width=120,anchor='center')
                self.tabla.column('Especie',minwidth=100, width=120,anchor='center')
                self.tabla.column('Raza',minwidth=100, width=120,anchor='center')
                self.tabla.column('Edad',minwidth=100, width=120,anchor='center')
                self.tabla.column('Dueño',minwidth=100, width=120,anchor='center')

                self.tabla.heading('#0',text='Id',anchor='center')
                self.tabla.heading('Nombre',text='Nombre',anchor='center')
                self.tabla.heading('Especie',text='Especie',anchor='center')
                self.tabla.heading('Raza',text='Raza',anchor='center')
                self.tabla.heading('Edad',text='Edad',anchor='center')
                self.tabla.heading('Dueño',text='Dueño',anchor='center')
                self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)

class Menu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.frame1 = None
        self.frame_actual = None

        self.crear_menu()

    def volver(self):
        self.master.destroy()
        root = Tk()
        root.geometry("800x500")
        root.title("Sistema de veterinaria")
        app = Menu(master=root)
        app.mainloop()

    def crear_menu(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual = self
        self.frame_actual.grid(row=0, column=0, sticky='nsew')

        label = Label(self, text="Bienvenido al sistema de veterinaria", fg='black', bg='white',
                      font=('Arial', 20, 'bold'))
        label.grid(column=1, row=0)

        button = Button(self, text="Pacientes", command=self.crear_pacientes, font=('Arial', 9, 'bold'),
                        width=30, bd=10).grid(column=1, row=2)

        button = Button(self, text="Propietarios", command=self.crear_propietarios, font=('Arial', 9, 'bold'),
                        width=30, bd=10).grid(column=1, row=3)
        button = Button(self, text="Servicios", command=self.crear_servicios, font=('Arial', 9, 'bold'),
                        width=30, bd=10).grid(column=1, row=4)
        button = Button(self, text="Turnos", command=self.crear_turnos, font=('Arial', 9, 'bold'),
                        width=30, bd=10).grid(column=1, row=5)


    def crear_pacientes(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual = Pacientes(self.master)
        #self.frame_actual.grid(row=0, column=0, sticky='nsew')

        Button(self.frame_actual, text="Volver a Menú", command=self.volver, font=('Arial', 9, 'bold'),
               width=30, bd=10).grid(column=2, row=5)
        

    def crear_propietarios(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual= Propietarios(self.master)

        Button(self.frame_actual, text="Volver a Menú", command=self.volver, font=('Arial', 9, 'bold'),
               width=30, bd=10).grid(column=2, row=5)

    def crear_servicios(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual= Servicios(self.master)

        Button(self.frame_actual, text="Volver a Menú", command=self.volver, font=('Arial', 9, 'bold'),
               width=30, bd=10).grid(column=2, row=5)

    def crear_turnos(self):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual= Turnos(self.master)

        Button(self.frame_actual, text="Volver a Menú", command=self.volver, font=('Arial', 9, 'bold'),
               width=30, bd=10).grid(column=2, row=5)


if __name__ == '__main__':

    root = Tk()
    root.geometry("800x500")
    root.title("Sistema de veterinaria")
    app = Menu(master=root)
    app.mainloop()
