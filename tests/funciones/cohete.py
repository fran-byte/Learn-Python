
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 

# Un Cohete sale de tierra en una determinada fecha dd/mm/aa hh:mm camino de algún lugar.
# Si el tiempo de trayecto es de dd/mm/aa hh:mm
# Calcula un algoritmo que determine el día y hora de llegada.

from datetime import datetime,timedelta # Importamos el módulo datetime para trabajar con él



def FechaLanzamiento(): # Utilizamos esta función para introducir la fecha lanzamiento
	
	while True:
		try:
			Dia = int(input("Día 00: "))
			Mes = int(input("Mes 00: "))
			Anno = int(input("Año 0000: "))
			
			if Dia > 31 or Mes >12:
				print("ERROR, introduzca de nuevo la fecha de lanzamiento\n ")
				
			else:
				return Dia,Mes,Anno # Devolvemos en estas 3 variables la fecha de lanzamiento
				
		except ValueError: # si validamos con ENTER directamente en los inputs nos dará un Value Error
			print("ERROR, introduzca de nuevo la fecha de lanzamiento\n ")




def Tiempo(): # Esta funcion será utilizada tanto para la hora de despegue como para la duración del tiempo de viaje.
	
	while True:
		
		try:
			Hhours = int(input("Horas 00: "))
			Mminutes = int(input("Minutos 00: "))
			return Hhours,Mminutes
			
		except ValueError: # si validamos con ENTER directamente en los inputs nos dará un Value Error
			print("ERROR, empiece de nuevo\n ")




print("\nIndica la fecha y hora de lanzamiento\n")	
	
Fdia,Fmes,Fanno = FechaLanzamiento()	


Fhours,Fminutes = Tiempo()

print("\nIndica la duración del viaje\n")

while True:
	
		try:
			Ddia = int(input("Días 00: "))
			Dmes = int(input("Meses 00: "))
			Danno = int(input("Años 00: "))
			break 
			
		except ValueError:
			print("ERROR, Repita de nuevo por favor\n ")

Dhours,Dminutes=Tiempo()

FechaLanzamiento= datetime(Fanno, Fmes, Fdia, Fhours, Fminutes) # introducimos la fecha de lanzamiento en el formato datetime 
DuracionViaje= datetime(Danno, Dmes, Ddia, Dhours, Dminutes) # introducimos la fecha la duración en el formato datetime 

Duracion=timedelta(days=(Ddia+Dmes*30+Danno*365), hours=Dhours, minutes=Dminutes) # No se tiene en cuenta los años bisiestos, y se ha calculado la suma de dias con un estandar erroneo mes=30 días
Llegando=FechaLanzamiento+Duracion # Realizamos el cálculo para saber la fecha de llegada

print("\nFecha de lanzamiento: ", FechaLanzamiento,"\nDuración del viaje: ", DuracionViaje,"\n")

print("Fecha prevista de llegada será : ",Llegando,"\n")



