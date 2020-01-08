
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 
# METODO - CONSTRUCTOR DE CLASE
# Construimos la clase Galleta

class Galleta(): # Creando la clase Galleta
	
	chocolate=False # Atributo compartido por todas las instancias
	
	def __init__(self): # inicializando los atributos de la clase Galleta
		print("\nSe acaba de crear una galleta\n")
		
	def chocolatear(self):
		self.chocolate=True
		
	def tiene_chocolate(self):
		if(self.chocolate):
			print("\nSoy una galleta CHOCOLATEADA\n")
		else:
			print("\nSoy una galleta SIN Chocolate\n")
	
	
g=Galleta()

g.tiene_chocolate() # llamamos a la función (dentro de Galleta) y preguntamos si tiene chocolate

g.chocolatear()	# llamando a chocolatear ahora le asignamos el atributo de clase chocolate=True

g.tiene_chocolate() # Volvemos a preguntar si tiene chocolate
