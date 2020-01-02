
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Localiza el error y crea una excepción:

# resultado = "20" + 15


# TypeError: Cant't convert 'int' objetct to str implicitly



try:
	
	resultado = "20" + 15
	
except TypeError:
	print("Type Error, no puedes sumar una cadena de texto (str) a un numero (int)")
