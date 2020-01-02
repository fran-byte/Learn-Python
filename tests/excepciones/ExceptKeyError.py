
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Localiza el error y crea una excepción:

# colores = {"rojo":"red","verde":"green","azul":"blue"}
# colores ["blanco"]

# Key Error: 'blanco'


colores = {"rojo":"red","verde":"green","azul":"blue"}

try:
	
	colores ["blanco"]
	
except KeyError:
	print("Key Error, la clave del diccionario no se encuentra, prueba con otra")
