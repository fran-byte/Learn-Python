#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 /
# Crear una función que calcule la temperatura media de un número X de días a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y
# mínima de cada día. El programa pedirá el número de días que se van a introducir.

Tmaxima=[] # Creamos una lista donde almacenaremos las temperaturas máximas
Tminima=[] # Creamos una lista donde almacenaremos las temperaturas mínimas

def Tmedia(Tmaxima,Tminima): # La función donde haremos los calculos de la media de temperatura
    SumaTmax = 0 # Definiremos la variable donde iremos incrementando y sumando uno a uno toda la lista de Tmaxima
    SumaTmin = 0 # Definiremos la variable donde iremos incrementando y sumando uno a uno toda la lista de Tminima
    for i,a in zip(Tmaxima,Tminima): # Iterando en paralelo y Sumando las listas a la vez y cada una por separado con zip
        SumaTmax += i # Vamos sumando y dejandolo en SumaTmax
        SumaTmin += a # Vamos sumando y dejandolo en SumaTmax

    return ((SumaTmax/dias+SumaTmin/dias)/2) # Procedemos a hacer la media y la retornamos


while True: # Creamos este bucle infinito para contener el try y except
    try:
        dias = int(input("Introduce el nº de días: "))
        if dias <=0: # Lo condicionamos solo a números enteros positivos
            print("Por favor números positivos")
        else:
            break # Si es correcto, rompemos el bucle y continuamos
    except:
        print("Introduce números enteros positivos")

for i in range(dias): # vamos introduciento las temperaturas máxima y mínima, tantas veces como días introducidos
    print("Día: ",i+1)
    Tma = float(input("T. máxima: "))
    Tmaxima.append(Tma)
    Tmi = float(input("T. mínima: "))
    Tminima.append(Tmi)


print("La media de temperatura de estos ",dias," días es de : ",Tmedia(Tmaxima,Tminima))," ºC"