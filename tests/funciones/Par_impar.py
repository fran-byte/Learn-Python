
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Utilizaremos una función de argumentos determinados.

# Crea una funcion llamada separar() que reciba una lista y devuelva dos,
# una con los número pares y otra con los impares

ListaPar=[] # Definimos las listas que imprimiremos al final del programa,
ListaImp=[] # una para los pares y otra para los impares
NumLista=[]

def separar(args): # Creamos una función determinada
				
	for c,arg in enumerate(args): #vamos dejando los valores de los argumentos obtenidos en arg
			
		if args[c] % 2 == 0: # condicionamos arg para saber si el resto de su división es cero
			ListaPar.append(args[c]) # y lo añadimos a la lista de los pares
		else:
			ListaImp.append(args[c]) # y si no lo añadimos a la lista de los impares
			
	return ListaPar,ListaImp # retornamos las dos listas
		
while (True):
	try:
		Num = input("   : ")
		if Num == "end":
			break
		else:
			Num=int(Num)
			NumLista.append(Num)
			
	except ValueError: # en caso de Error en la entrada de datos, al introducir algo diferente a "end" o números
		print("Números por favor o 'end' para finalizar entrada de datos")
	
separar(NumLista) # llamamos a la función y le ennviamos la lista guardada de números enteros

print ("\nPares: ",ListaPar,"\nImpares: ",ListaImp,"\n")
