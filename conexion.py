import sqlite3

class Conexion():
	def init_(self):
		self.conexion = sqlite3.connect('veterinaria.sqlite')

	def insertar_pacientes(self, Nombre, Especie, Raza,Edad, IDPropietario ):
		cursor = self.conexion.cursor()
		bd = '''INSERT INTO Mascotas (IDMascota, Nombre, Especie, Raza, Edad, IDPropietario)
		VALUES ('{}', '{}', '{}', '{}', '{}', '{}')'''.formart(nombre, especie,raza,edad,IDPropietario)
		cursor.execute(bd)
		self.conexion.commit()
		cursor.close()

	def mostrar_pacientes(self):
		cursor = self.conexion.cursor()
		bd= "SELECT * FROM Mascotas"
		cursor.execute(bd)
		pacientes = cursor.fetchall()
		return pacientes




