#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 
# Realizar una tabla o matriz introduciendo filas y columnas

import sys # damos acceso o importamos variables del systema (interprete)


if len(sys.argv) == 3: 	# condicionamos a solo 3 argumentos 
						#(1 nombre de archivo, 2 argv[1], 3 argv[2]
						
	NumeroFilas = int(sys.argv[1]) # recogemos el argumento 1 en la variable
	NumeroColumnas = int(sys.argv[2]) # recogemos el argumento 2 en la variable
	
	if NumeroFilas and NumeroColumnas > 0 and NumeroFilas and NumeroColumnas < 21: 
		# condicionamos nuemeros entre (1-20)
		
		for i in range(NumeroFilas):
			print(" ")
			for x in range(NumeroColumnas):
				print("O ",end='')
		print("\n")
	
	else:
		print("""
		Error, los argumentos introducidos no son válidos
		Introduzca 2 números enteros entre 1 y 20
		""")





else:
	print("""
	Error, los argumentos introducidos no son válidos
	Introduzca 2 números enteros entre 1 y 20
	""")
