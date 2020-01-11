#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Método Constructor de Clase

class Pelicula:
	def __init__(self, titulo, duracion, lanzamiento): # Acción o Método
		self.titulo=titulo
		self.duracion=duracion
		self.lanzamiento=lanzamiento
		print("\nSe ha creado la película\n",self.titulo)
		
p=Pelicula("El Padrino", 175, 1972)



