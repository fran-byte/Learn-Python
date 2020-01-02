
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Localiza el error y crea una excepción:

# resultado = 10/0

# Traceback (most recent call last):
#   File "excepcion_1.py", line 15, in <module>
#    resultado = 10/0
# ZeroDivisionError: division by zero


	

try:
	resultado = 10/0
	
except ZeroDivisionError:
	print("No puedes dividir entre cero")
