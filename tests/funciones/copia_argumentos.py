#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 
# Crear copia de la llamada para evitar modificaciones en la función



def doblar_valores(numeros):
	for i,n in enumerate(numeros):
		numeros[i]*=2
	print ("esta impresión\nes de la COPIA de la LISTA dentro de la función ",numeros,"\n")
	


ns=[10,50,100,200]
print("\nDeclaramos una Lista  ns=",ns,"\n")

print("enviamos la COPIA de la lista a la función\n")
doblar_valores(ns[:])








print("e imprimimos la lista de nuevo ns=",ns,"\n") # ahora con una lista si lo habrá doblado.

print("Y podemos comprobar que la lista no ha sido modificada  \n")


