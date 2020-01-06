#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Pasamos argumentos por valor a la función

def doblar_valor(numero):
	numero*=2
	# return numero*2  # Para nos funcione debemos retornar el resultado, no la variable

n=10
print("\ndeclaramos n=10\n")

doblar_valor(n) # OJO con pasar una valor de la variable directamente, no le afectará nada lo que hagos en def
				# seguirá teniendo el mismo valor, no ocurre lo mismo para las listas
print("enviamos esa variable a la función para doblarla....\n")
print("e imprimimos el valor de n:   ",n,"\n") # n será 10 y no se habrá doblado
print("y como vemos no se habrá doblado, \n")

print("\n\nAhora vamos a pasarle una lista y veremos que con la lista si funciona, \n")




def doblar_valores(numeros):
	for i,n in enumerate(numeros):
		numeros[i]*=2


ns=[10,50,100,200]
print("\ndeclaramos ns=[10,50,100,200]\n")
doblar_valores(ns)

print("enviamos esa lista la función para doblarla....\n")
print("e imprimimos el valor de la lista=",ns,"\n") # ahora con una lista si lo habrá doblado.
print("y como vemos SI se habrá doblado, \n")


