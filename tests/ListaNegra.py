
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento.
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento.


elementos=[]

def agregar_una_vez(lista, elementos):
	
	listaNegra=[]
		
		
	for a,i in enumerate(elementos):
				
		if elementos[a] not in lista:
			lista.append(elementos[a])
			print("Lista Fusionada: ",lista)
				
			
		else:
			listaNegra.append(elementos[a])
	print("\nLista Negra: ",listaNegra,"\n")
	print("Lista Fusionada: ",lista,"\n")

	
while (True):
	try:
		e = input("Introduzca datos   : ")
		if e == "end":
			lista=[10,"Python",-2,"rr","Hola"]
			agregar_una_vez(lista,elementos)
			
			break
		else:
			
			elementos.append(e)
			
		

	except ValueError:
		print("El elemento")
	
#agregar_una_vez([10, -2, "Hola"],3)

