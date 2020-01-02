
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Localiza el error y crea una excepción:

# lista [2,6,9,43,3]
# lista [10]

# Index Error: List index out of range


lista = [2,6,9,43,3]	

try:
	
	lista [10]
	
except IndexError:
	print("No puedes acceder a ese indice, está fuera de rango")
