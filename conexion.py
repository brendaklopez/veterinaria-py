import sqlite3

class Conexion():
	def __init__(self):
		self.conexion = sqlite3.connect('veterinaria.sqlite')

	def insertar_pacientes(self, Nombre, Especie, Raza,Edad, IDPropietario):
		cursor = self.conexion.cursor()
		bd = '''INSERT INTO Mascotas(Nombre, Especie, Raza, Edad, IDPropietario)
		VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(Nombre, Especie,Raza,Edad, IDPropietario)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def actualizar_pacientes(self, id_paciente, Nombre, Especie, Raza, Edad):
		cursor = self.conexion.cursor()
		bd = '''UPDATE Mascotas SET Nombre = '{}', Especie = '{}', Raza = '{}',  Edad = '{}' WHERE IDMascota = '{}' '''.format(Nombre,Especie, Raza,  Edad, id_paciente)
		cursor.execute(bd)
		dato= cursor.rowcount
		self.conexion.commit()
		cursor.close()
		return dato

	def eliminar_pacientes(self, id_paciente):
		cursor = self.conexion.cursor()
		bd=  '''DELETE FROM Mascotas WHERE IDMascota = {}'''.format(id_paciente)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def mostrar_pacientes(self):
		cursor = self.conexion.cursor()
		# bd= "SELECT * FROM Mascotas"
		bd= "SELECT m.IDMascota, m.Nombre, m.Especie, m.Raza, m.Edad, p.Nombre || ' ' || p.Apellido AS Propietario FROM Mascotas m JOIN Propietarios p ON m.IDPropietario = p.DNI"
		cursor.execute(bd)
		pacientes = cursor.fetchall()
		return pacientes

	def mostrar_propietarios(self):
		cursor = self.conexion.cursor()
		bd= "SELECT * FROM Propietarios"
		cursor.execute(bd)
		dueños = cursor.fetchall()
		return dueños
		
	def insertar_propietarios(self, DNI, Nombre, Apellido, Telefono, Email):
		cursor = self.conexion.cursor()
		bd = '''INSERT INTO Propietarios(DNI, Nombre, Apellido, Telefono, Email)
		VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(DNI, Nombre, Apellido, Telefono, Email)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def eliminar_propietarios(self, id_propietario):
		cursor = self.conexion.cursor()
		bd=  '''DELETE FROM Propietarios WHERE DNI = {}'''.format(id_propietario)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def mostrar_servicios(self):
		cursor = self.conexion.cursor()
		bd= "SELECT * FROM Servicios"
		cursor.execute(bd)
		servicios = cursor.fetchall()
		return servicios
	
	def insertar_servicios(self, descripcion, precio):
		cursor = self.conexion.cursor()
		bd = '''INSERT INTO Servicios(Descripcion, Precio) VALUES ('{}', '{}')'''.format(descripcion, precio)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def actualizar_servicios(self,idservicio, descripcion, precio):
		cursor = self.conexion.cursor()
		bd = '''UPDATE Servicios SET Descripcion = '{}', Precio = '{}'  WHERE IDservicio = '{}' '''.format(descripcion, precio,idservicio)
		cursor.execute(bd)
		dato= cursor.rowcount
		self.conexion.commit()
		cursor.close()
		return dato
	
	def eliminar_servicio(self, id):
		cursor = self.conexion.cursor()
		bd=  '''DELETE FROM Servicios WHERE IDservicio = {}'''.format(id)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def mostrar_citas(self):
		cursor = self.conexion.cursor()
		bd= "SELECT c.IDcita, c.Fecha, c.Hora, m.nombre, s.descripcion FROM Citas c JOIN mascotas m ON c.IDMascota = m.IDMascota JOIN servicios s ON c.IDservicio = s.IDservicio"
		cursor.execute(bd)
		servicios = cursor.fetchall()
		return servicios

	def insertar_cita(self, Fecha, Hora, IDMascota, IDServicio):
		cursor = self.conexion.cursor()
		bd = '''INSERT INTO Citas(Fecha, Hora, IDMascota, IDServicio)
		VALUES ('{}', '{}', '{}', '{}')'''.format( Fecha, Hora, IDMascota, IDServicio)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()


