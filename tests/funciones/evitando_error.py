#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 
# Evitando errores al pasar los argumentos a la función

def resta(a=None, b=None): # Colocamos la condicional de None para evitar el error
	if a==None or b==None: 
		print("\nERROR, Envía 2 números a la función")
		return
		
	else:
		return a-b

print("\nEl primer envío lo hemos hecho Vacío sin argumentos\n y la función nos devuelve:\n",resta(),"\n")
print("En el segundo envío si introducimos los argumentos\n y la función nos devuelve la resta:\n",resta(4,5),"\n")



