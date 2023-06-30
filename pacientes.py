from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame
from conexion import Conexion
from principal import Aplicacion, Frame1

class Ventana(Frame):
	def __init__(self, master, *args):
		super(). __init__(master, *args)
		self.Nombre = StringVar()
		self.Especie = StringVar()
		self.Raza = StringVar()
		self.Edad = StringVar()
		self.Dueño = StringVar()
		self.selected_option = StringVar()
		self.propietarios={}

		self.master.columnconfigure(0,weight=1)
		self.master.rowconfigure(0, weight=1)
		self.master.rowconfigure(1,weight=5)

		self.bd=Conexion()
		self.widgets()
		self.actualizar_tabla()
		self.main=Aplicacion()

	def limpiar_campos(self):
		self.Nombre.set('')
		self.Edad.set('')
		self.Especie.set('')
		self.Raza.set('')
		self.Dueño.set('')

	def actualizar_tabla(self):
		self.limpiar_campos()
		datos = self.bd.mostrar_pacientes()
		self.tabla.delete(*self.tabla.get_children())
		for i in range(len(datos)):
			self.tabla.insert('', i, text=datos[i][0], values=datos[i][1:6])

	def agregar_datos(self):
				Nombre = self.Nombre.get()
				Edad = self.Edad.get()
				Especie= self.Especie.get()
				Raza = self.Raza.get()
				Dueño = [propietario['IDPropietario'] for propietario in self.propietarios if propietario['Nombre'] == self.selected_option.get()][0]
				datos = (Nombre, Especie, Raza, Edad, Dueño)
				if Nombre and Especie and Raza and Edad and Dueño !='':
					self.bd.insertar_pacientes(Nombre,Especie,Raza,Edad,Dueño)
					self.limpiar_campos()
					self.actualizar_tabla()
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
					self.Dueño.set(d[5])

	def eliminar_fila(self):
		self.limpiar_campos()
		item = self.tabla.selection()[0]
		self.data = self.tabla.item(item)
		id_paciente = self.data['text']
		self.tabla.delete(item)
		self.bd.eliminar_pacientes(id_paciente)



	def actualizar_pacientes(self):
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
		self.propietarios = [{'IDPropietario': row[0], 'Nombre': row[1]} for row in db_rows]
		return self.propietarios
		# nombres=list(self.bd.mostrar_propietarios())
		# return nombres

	def volver_inicio(self):
		self.main.crear_frame1()

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

		Button(self.frame_uno, text='Añadir paciente Nuevo', command= self.agregar_datos, font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=1, pady= 5, padx=5)
		Button(self.frame_uno, text='Limpiar campos', command =self.limpiar_campos ,font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=2, pady= 5, padx=5)
		Button(self.frame_uno, text='Eliminar', command =self.eliminar_fila ,font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=3, pady= 5, padx=5)
		Button(self.frame_uno, text='Modificar', command =self.actualizar_pacientes,font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=4, pady= 5, padx=5)
		Button(self.frame_uno, text='Volver a Inicio', command= seld.volver_inicio,font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=5, pady= 5, padx=5)


		Entry(self.frame_uno, textvariable=self.Nombre, font=('Comic Sans', 12)).grid(column=1,row=1)
		Entry(self.frame_uno, textvariable=self.Especie, font=('Comic Sans', 12)).grid(column=1,row=2)
		Entry(self.frame_uno, textvariable=self.Raza, font=('Comic Sans', 12)).grid(column=1,row=3)
		Entry(self.frame_uno, textvariable=self.Edad, font=('Comic Sans', 12)).grid(column=1,row=4)

		combobox = ttk.Combobox(self.frame_uno, textvariable=self.selected_option)
		combobox.grid(column=1, row=5)
		propietarios = self.combo_input()

		combobox['values'] = [propietario['Nombre'] for propietario in propietarios]
		# Entry(self.frame_uno, textvariable=self.Dueño, font=('Comic Sans', 12)).grid(column=1,row=5)


		self.tabla = ttk.Treeview(self.frame_dos)
		self.tabla.grid(column=0, row=0, sticky='nsew')
		ladox= ttk.Scrollbar(self.frame_dos, orient= 'horizontal', command= self.tabla.xview)
		ladox.grid(column=0, row=1, sticky='ew')
		ladoy= ttk.Scrollbar(self.frame_dos, orient= 'vertical', command= self.tabla.yview)
		ladoy.grid(column=1, row=0, sticky='ns')
		self.tabla.configure(xscrollcommand = ladox.set,yscrollcommand= ladoy.set )

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
		# self.tabla.bind("<Double-1>", self.eliminar_fila)


if __name__ == '__main__':
	

	ventana = Tk()
	ventana.title('')
	ventana.minsize(height = 400, width =600)
	ventana.geometry('800x500')
	app = Ventana(ventana)
	app.mainloop()
