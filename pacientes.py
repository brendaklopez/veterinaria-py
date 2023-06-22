from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame
from conexion import Conexion

class Ventana(Frame):
	def __init__(self, master, *args):
		super(). __init__(master, *args)
		self.Nombre = StringVar()
		self.Especie = StringVar()
		self.Raza = StringVar()
		self.Edad = StringVar()
		self.IDPropietario = StringVar()

		self.master.columnconfigure(0,weight=1)
		self.master.rowconfigure(0, weight=1)
		self.master.rowconfigure(1,weight=5)

		self.bd=Conexion()
		self.widgets()

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
		Button(self.frame_uno, text='Actualizar', fg='black',bg='violet',width=20, bd=3).grid(column=2, row=1,pady=5)
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

		Button(self.frame_uno, text='Añadir paciente', font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=2, pady= 5, padx=5)
		Button(self.frame_uno, text='Limpiar campos', font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=3, pady= 5, padx=5)
		Button(self.frame_uno, text='Actualizar datos', font= ('Arial', 9, 'bold'), width=20,
			bd=3 ).grid(column=2, row=4, pady= 5, padx=5)

		Entry(self.frame_uno, textvariable=self.Nombre, font=('Comic Sans', 12)).grid(column=1,row=1)
		Entry(self.frame_uno, textvariable=self.Especie, font=('Comic Sans', 12)).grid(column=1,row=2)
		Entry(self.frame_uno, textvariable=self.Raza, font=('Comic Sans', 12)).grid(column=1,row=3)
		Entry(self.frame_uno, textvariable=self.Edad, font=('Comic Sans', 12)).grid(column=1,row=4)
		Entry(self.frame_uno, textvariable=self.IDPropietario, font=('Comic Sans', 12)).grid(column=1,row=5)

		self.tabla = ttk.Treeview(self.frame_dos)
		self.tabla.grid(column=0, row=0, sticky='nsew')
		ladox= ttk.Scrollbar(self.frame_dos, orient= 'horizontal', command= self.tabla.xview)
		ladox.grid(column=0, row=1, sticky='ew')
		ladoy= ttk.Scrollbar(self.frame_dos, orient= 'vertical', command= self.tabla.yview)
		ladoy.grid(column=1, row=0, sticky='ns')
		self.tabla.configure(xscrollcommand = ladox.set,yscrollcommand= ladoy.set )

		self.tabla['columns']= ('Especie','Raza','Edad', 'Dueño')
		self.tabla.column('#0',minwidth=100, width=120,anchor='center')
		self.tabla.column('Especie',minwidth=100, width=120,anchor='center')
		self.tabla.column('Raza',minwidth=100, width=120,anchor='center')
		self.tabla.column('Edad',minwidth=100, width=120,anchor='center')
		self.tabla.column('Dueño',minwidth=100, width=120,anchor='center')

		self.tabla.heading('#0',text='Nombre',anchor='center')
		self.tabla.heading('Especie',text='Especie',anchor='center')
		self.tabla.heading('Raza',text='Raza',anchor='center')
		self.tabla.heading('Edad',text='Edad',anchor='center')
		self.tabla.heading('Dueño',text='Dueño',anchor='center')


# if __name__ == '__main__':
# 	ventana = Tk()
# 	ventana.title('')
# 	ventana.minsize(height = 400, width =600)
# 	ventana.geometry('800x500')
# 	app = Ventana(ventana)
# 	app.mainloop()
