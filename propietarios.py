from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame
from conexion import Conexion

class Propietarios(Frame):
	def __init__(self, master, *args):
		super(). __init__(master, *args)
		self.Nombre = StringVar()
		self.Apellido = StringVar()
		self.Telefono = StringVar()
		self.Email = StringVar()

		self.master.columnconfigure(0,weight=1)
		self.master.rowconfigure(0, weight=1)
		self.master.rowconfigure(1,weight=5)

		self.bd=Conexion()
		self.widgets()
		self.actualizar_tabla()

	def limpiar_campos(self):
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
		Nombre = self.Nombre.get()
		Apellido = self.Apellido.get()
		Email= self.Email.get()
		Telefono= self.Telefono.get()
		datos = (Nombre, Apellido, Telefono, Email)
		if Nombre and Apellido and Email and Telefono !='':
			self.bd.insertar_propietarios(Nombre, Apellido,Telefono, Email)
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

	def actualizar_pacientes(self):
		pass
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


	def widgets(self):
		self.frame_uno = Frame(self.master, bg='white',height=200,width=800)
		self.frame_uno.grid(column=0,row=0,sticky='nsew')

		self.frame_dos=Frame(self.master, bg='white', height=300, width=800)
		self.frame_dos.grid(column=0,row=1,sticky='nsew')

		self.frame_uno.columnconfigure([0,1,2],weight=1)
		self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)

		self.frame_dos.columnconfigure(0,weight=1)
		self.frame_dos.rowconfigure(0,weight=1)

		Label(self.frame_uno, text = 'Opciones', fg= 'black', bg='white',
			font=('Arial', 13,'bold')).grid(column=2,row=0)
		Label(self.frame_uno, text = 'Agregar y actualizar propietarios', fg= 'black', bg='white',
			font=('Arial', 13,'bold')).grid(columnspan=2, column=0,row=0,pady=5)
		Label(self.frame_uno,text= 'Nombre', fg='black', bg='white',
			font=('Arial', 13, 'bold')).grid(column=0,row=1, pady=5)
		Label(self.frame_uno,text='Apellido', fg='black', bg='white',
			font=('Arial', 13, 'bold')).grid(column=0,row=2, pady=5)
		Label(self.frame_uno,text='Telefono', fg='black', bg='white',
			font=('Arial', 13, 'bold')).grid(column=0,row=3, pady=5)			
		Label(self.frame_uno,text='Email', fg='black', bg='white',
			font=('Arial', 13, 'bold')).grid(column=0,row=4, pady=5)

		Button(self.frame_uno, text='Añadir dueño Nuevo', command= self.agregar_datos, font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=1, pady= 5, padx=5)
		Button(self.frame_uno, text='Limpiar campos', command =self.limpiar_campos,font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=2, pady= 5, padx=5)
		Button(self.frame_uno, text='Eliminar', command = self.eliminar_fila,font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=3, pady= 5, padx=5)
		Button(self.frame_uno, text='Modificar', font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=4, pady= 5, padx=5)


		Entry(self.frame_uno, textvariable=self.Nombre, font=('Comic Sans', 12)).grid(column=1,row=1)
		Entry(self.frame_uno, textvariable=self.Apellido, font=('Comic Sans', 12)).grid(column=1,row=2)
		Entry(self.frame_uno, textvariable=self.Telefono, font=('Comic Sans', 12)).grid(column=1,row=3)
		Entry(self.frame_uno, textvariable=self.Email, font=('Comic Sans', 12)).grid(column=1,row=4)

		self.tabla = ttk.Treeview(self.frame_dos)
		self.tabla.grid(column=0, row=0, sticky='nsew')
		ladox= ttk.Scrollbar(self.frame_dos, orient= 'horizontal', command= self.tabla.xview)
		ladox.grid(column=0, row=1, sticky='ew')
		ladoy= ttk.Scrollbar(self.frame_dos, orient= 'vertical', command= self.tabla.yview)
		ladoy.grid(column=1, row=0, sticky='ns')
		self.tabla.configure(xscrollcommand = ladox.set,yscrollcommand= ladoy.set )

		self.tabla['columns']= ('Nombre', 'Apellido','Telefono','Email')
		self.tabla.column('#0',minwidth=100, width=120,anchor='center')
		self.tabla.column('Nombre',minwidth=100, width=120,anchor='center')
		self.tabla.column('Apellido',minwidth=100, width=120,anchor='center')
		self.tabla.column('Telefono',minwidth=100, width=120,anchor='center')
		self.tabla.column('Email',minwidth=100, width=120,anchor='center')

		self.tabla.heading('#0',text='Id',anchor='center')
		self.tabla.heading('Nombre',text='Nombre',anchor='center')
		self.tabla.heading('Apellido',text='Apellido',anchor='center')
		self.tabla.heading('Telefono',text='Telefono',anchor='center')
		self.tabla.heading('Email',text='Email',anchor='center')
		

		self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
		# self.tabla.bind("<Double-1>", self.eliminar_fila)


if __name__ == '__main__':
	

	ventana = Tk()
	ventana.title('')
	ventana.minsize(height = 400, width =600)
	ventana.geometry('800x500')
	app = Propietarios(ventana)
	app.mainloop()
