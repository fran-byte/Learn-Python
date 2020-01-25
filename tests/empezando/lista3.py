#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 /

# Ejercicio de LISTAS / for/ CONDICIONALES :
# Dadas 2 listas (lista1 y lista2) generar sus elementos comunes una tercera lista (lista3)
# Pero en la lista3 no debe de haber ningún elemento repetido.

lista1=[1,2,3,4,5,60,70,80,90]
lista2=[1,2,3,4,5,6,7,8,9]
lista3=[]

for volcado in lista1: # Vamos a ir volcado cada elemento de la lista1 en volcado
  if volcado in lista2 and volcado not in lista3: # colocamos la condiciones:
                # sí volcado(que es lista1) está en lista2 y además no está en lista3
    lista3.append(volcado)  # añadimos ese elemento como un apéndice a lista3

print("lista1: ",lista1)
print("lista2: ",lista2)
print("\nlista3: ",lista3,"\nContenidos comunes de la lista1 y lista2")