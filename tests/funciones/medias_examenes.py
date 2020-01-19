
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 /     
# Ejercicio:
# Un alumno desea saber cual será su calificación final.
# Dicha calificación se compone de los siguientes porcentajes:
# 30% del promedio de sus calificaciones parciales.
# 55% de calificaciones de los examenes finales.
# 15% de la calificación de los trabajos realizados.



print("\nRESULTADO CALIFICACIONES FINALES\n")


def Entrada(): # funcion entrada de datos
	
	datos=[] # datos será una lista
	
	while True: # bucle infinito
		dato=input(">>> Introduzca calificación/nes, TECLEE 'fin' para Finalizar: ")
		
		if dato=="fin": # condicional de salida del bucle
			
			return datos # devuelve datos y sale de la función
			
		elif float(dato) >= 0: # si dato, previamente convertido a flotante es mayor o igual a 0
			print("\n")
			
			datos.append(float(dato)) # lo vamos adjuntando a la lista datos
			
		else: # resulta que es un número negativo
			print("Solo números positivos, por favor !!")
		
print("\nIntroduzca las calificaciones parciales\n")

parciales=Entrada() # dejamos el resultado de la función en parciales (será una lista númerica)
p=sum(parciales) # sumamos los elementos de la lista y lo dejamos en p

print("\n")

media=(p)/len(parciales) #sacamos la media de los parciales 
print("Media: ",media, "con un 30% de la nota")
print("\nIntroduzca las calificaciones de examenes finales\n")

ExamenFinal=Entrada() # dejamos el resultado de la función en ExamenFinal (será una lista númerica)
pe=sum(ExamenFinal) # sumamos los elementos de la lista y lo dejamos en pe

print("\n")

mediaEx=(pe)/len(ExamenFinal) #sacamos la media de los examenes finales 
print("Media: ",mediaEx, "con un 55% de la nota")
print("\nIntroduzca las calificaciones de los trabajos\n")

Trabajo=Entrada() # dejamos el resultado de la función en Trabajo (será una lista númerica)
pt=sum(Trabajo) #sumamos los elementos de la lista y lo dejamos en pt

print("\n")

mediaTr=(pt)/len(Trabajo) #sacamos la media de los trabajos
print("Media: ",mediaTr, "con un 15% de la nota")
print("\n***************************************")

print("La Nota final del Curso es de:", (media*0.3+mediaEx*0.55+mediaTr*0.15)) # sumamos los porcentajes
print("\n***************************************")
