
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento, uno a uno. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento.

lista=[]

def agregar_una_vez(lista, elementos):
	

	try:
			
		if elementos not in lista:
			lista.append(elementos)
			print("\nLista Fusionada: ",lista,"\n")
					
				
		else:
			raise ValueError
				
	except ValueError:
		print("\nValueError:    Elemento duplicado: ", elementos,"\n")
				
						
	

print("\nPrimer Envío: [10, -2, 'Hola','Adios'],'Hola")
agregar_una_vez([10, -2, "Hola","Adios"],"Hola")	

print("Segundo Envío: [10, -2, 'Hola','Adios'],'Adios")
agregar_una_vez([10, -2, "Hola","Adios"],"Adios")

print("Tercer Envío: [10, -2, 'Hola','Adios'],'Python")
agregar_una_vez([10, -2, "Hola","Adios"],"Python")


