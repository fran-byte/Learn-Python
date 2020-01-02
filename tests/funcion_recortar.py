
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Realiza una función llamada recortar() que reciba tres parámetros,
# el 1º el nº a recortar, el 2º el límite inferior, y el 3º limite superior, y tendrá que devolver:
# -El límite inferior si el número es menor que este
# -El límite superior si el número es mayor que este
# -El número sin cambios si no se supera ningún límite

def recortar(Num,RecInferior,RecSuperior):
	
	if Num < RecInferior:
		return RecInferior
	elif Num > RecSuperior:
		return RecSuperior
	
	return Num

N = int(input("Número: "))
Inferior = int(input("Corte Inf: "))
Superior = int(input("Corte Sup: "))

print(recortar(N,Inferior,Superior))
