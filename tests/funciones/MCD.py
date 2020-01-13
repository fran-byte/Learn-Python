#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 /
# Crear una función que calcule el MCD de dos número por el método de Euclides.
# El método de Euclides es el siguiente:
#
# Se divide el número mayor entre el menor.
#
# Si la división es exacta, el divisor es el MCD.
#
# Si la división no es exacta, dividimos el divisor entre el resto obtenido y
# se continúa de esta forma hasta obtener una división exacta,
# siendo el último divisor el MCD.
#
# Crea un programa principal que lea dos números enteros y muestre el MCD.

def mcd(a,b):

    if a>b:
        dividendo = a
        divisor = b
    else:
        dividendo = b
        divisor = a

    if dividendo%divisor == 0:
        print("División exacta, retornamos en la primera condicción:")
        return divisor

    else:
        contador=0
        resto = dividendo % divisor
        while True:
            print("La División NO fue EXACTA, tenemos que seguir dividiendo"
                  " divisor entre resto: ",contador+1," Vez / veces")
            if dividendo % divisor != 0:
                dividendo = divisor
                divisor = resto
                contador+=1

            else:
                return divisor
print("\nMCD de 2 número: ")
while True:
    try:

        a = int(input("Primer Número: "))
        b = int(input("Segundo Número: "))
        if a > 0 and b > 0:
            break
    except:
        print("Números enteros y positivos por favor.")

print("El M.C.D. de ",a," y ",b," es: ",mcd(a,b))