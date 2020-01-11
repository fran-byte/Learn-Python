#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Método str devolviendo una cadena de texto formateada.


class Pelicula:
	# Constructor de Clase
	def __init__(self, titulo,duracion,lanzamiento): # Acción o Método
		self.titulo = titulo
		self.duracion = duracion
		self.lanzamiento = lanzamiento
		print("\nSe ha creado la película: ",self.titulo)

	# Destructor de clase
	def __del__(self):
		print("\nSe está borrando la película: ",self.titulo)

	# Redefiniendo el método string
	def __str__(self): # Método str (string) devuelve una cadena de texto
		return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)

	# Redefiniendo el método lenght

	def __len__(self):
		return self.duracion



p = Pelicula("El Padrino",175,1972)

s = str(p) # Lanzamos la llamada al método de mostrar

print (s)

d = len(p)

print (d)


