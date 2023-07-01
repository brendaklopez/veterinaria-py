import sqlite3

class Conexion():
	def __init__(self):
		self.conexion = sqlite3.connect('veterinaria.sqlite')
		self.cursor = self.conexion.cursor()

	def insertar_pacientes(self, Nombre, Especie, Raza,Edad, IDPropietario):
		bd = '''INSERT INTO Mascotas(Nombre, Especie, Raza, Edad, IDPropietario)
		VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(Nombre, Especie,Raza,Edad, IDPropietario)
		self.cursor.execute(bd)
		self.conexion.commit()

	def actualizar_pacientes(self, id_paciente, Nombre, Especie, Raza, Edad):
		bd = '''UPDATE Mascotas SET Nombre = '{}', Especie = '{}', Raza = '{}',  Edad = '{}' WHERE IDMascota = '{}' '''.format(Nombre,Especie, Raza,  Edad, id_paciente)
		self.cursor.execute(bd)
		dato= self.cursor.rowcount
		self.conexion.commit()
		return dato

	def eliminar_pacientes(self, id_paciente):
		bd= '''DELETE FROM Mascotas WHERE IDMascota = {}'''.format(id_paciente)
		self.cursor.execute(bd)
		self.conexion.commit()

	def actualizar_propietario(self, DNI, Nombre, Apellido, telefono, email, Id_prop):
		bd= '''UPDATE Propietarios SET DNI= '{}', Nombre= '{}', Apellido = '{}',  Telefono = '{}', Email = '{}' WHERE DNI = '{}' '''.format(DNI, Nombre, Apellido, telefono, email, Id_prop)
		self.cursor.execute(bd)
		dato= self.cursor.rowcount
		self.conexion.commit()
		return dato

	def mostrar_pacientes(self):
		# bd= "SELECT * FROM Mascotas"
		bd= "SELECT m.IDMascota, m.Nombre, m.Especie, m.Raza, m.Edad, p.Nombre || ' ' || p.Apellido AS Propietario FROM Mascotas m JOIN Propietarios p ON m.IDPropietario = p.DNI"
		self.cursor.execute(bd)
		pacientes = self.cursor.fetchall()
		return pacientes

	def mostrar_propietarios(self):
		bd= "SELECT * FROM Propietarios"
		self.cursor.execute(bd)
		dueños = self.cursor.fetchall()
		return dueños
		
	def insertar_propietarios(self, DNI, Nombre, Apellido, Telefono, Email):
		bd = '''INSERT INTO Propietarios(DNI, Nombre, Apellido, Telefono, Email)VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(DNI, Nombre, Apellido, Telefono, Email)
		self.cursor.execute(bd)
		self.conexion.commit()

	def eliminar_propietarios(self, id_propietario):
		bd=  '''DELETE FROM Propietarios WHERE DNI = {}'''.format(id_propietario)
		self.cursor.execute(bd)
		self.conexion.commit()

	def mostrar_servicios(self):
		bd= "SELECT * FROM Servicios"
		self.cursor.execute(bd)
		servicios = self.cursor.fetchall()
		return servicios
	
	def insertar_servicios(self, descripcion, precio):
		bd = '''INSERT INTO Servicios(Descripcion, Precio) VALUES ('{}', '{}')'''.format(descripcion, precio)
		self.cursor.execute(bd)
		self.conexion.commit()

	def actualizar_servicios(self,idservicio, descripcion, precio):
		bd = '''UPDATE Servicios SET Descripcion = '{}', Precio = '{}'  WHERE IDservicio = '{}' '''.format(descripcion, precio,idservicio)
		self.cursor.execute(bd)
		dato= self.cursor.rowcount
		self.conexion.commit()
		return dato
	
	def eliminar_servicio(self, id):
		bd=  '''DELETE FROM Servicios WHERE IDservicio = {}'''.format(id)
		self.cursor.execute(bd)
		self.conexion.commit()

	def mostrar_citas(self):
		bd= "SELECT c.IDcita, d.Fecha, d.Hora, m.nombre, s.descripcion, c.IDTurnoDisponible FROM Citas c JOIN Turnosdisponibles d ON c.IDTurnoDisponible= d.IDdiponibles JOIN mascotas m ON c.IDMascota = m.IDMascota JOIN servicios s ON c.IDservicio = s.IDservicio"
		self.cursor.execute(bd)
		servicios = self.cursor.fetchall()
		return servicios

	def insertar_cita(self, IDdisponible, IDMascota, IDServicio):
		bd = '''INSERT INTO Citas(IDMascota, IDServicio, IDTurnoDisponible)
		VALUES ('{}', '{}',  '{}')'''.format(IDMascota, IDServicio,  IDdisponible)
		self.cursor.execute(bd)
		self.conexion.commit()

	def mostrar_disponibles(self):
		bd= "SELECT * FROM Turnosdisponibles WHERE Disponibilidad = TRUE"
		self.cursor.execute(bd)
		dispo = self.cursor.fetchall()
		return dispo

	def modificar_disponibles(self, IDhora, valor):
		bd = '''UPDATE Turnosdisponibles SET Disponibilidad = '{}' WHERE IDdiponibles = '{}' '''.format(valor, IDhora)
		self.cursor.execute(bd)
		dato= self.cursor.rowcount
		self.conexion.commit()
		return dato

	def eliminar_cita(self, ID):
		bd =  '''DELETE FROM Citas WHERE IDCita = {}'''.format(ID)
		self.cursor.execute(bd)
		self.conexion.commit()





