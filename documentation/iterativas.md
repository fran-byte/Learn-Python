:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 8. SENTENCIAS ITERATIVAS (BUCLES)

## while

````python
c = 0
while c <= 5 : # Se ejecutará mientras c sea menor o igual a 5
    
    print("c vale: ",c)
    c+=1
print ("El bucle ha finalizado")
`````

>c vale:  0  
>
>c vale:  1
>
>c vale:  2
>
>c vale:  3
>
>c vale:  4
>
>c vale:  5
>
>El bucle ha finalizado

## while True:
#Construyendo un Bucle Infinito

````python

while True : # Se ejecutará siempre (hasta verse interrumpido)
    
    print("""OPCIONES
    1- SALUDAR
    2- SUMAR 2 Números
    3- SALIR""")
    opcion=input()
    if opcion == "1":
        print("HOLA")
    elif opcion == "2":
        n1=float(input("N.1: "))
        n2=float(input("N.2: "))
        print(n1,"+",n2,"=",n1+n2)
    elif opcion == "3":
        print("PROGRAMA FINALIZADO !!")
        break # Aquí rompemos el bucle
    else:
        print("Opción invalida, prueba de nuevo")
print("Estamos fuera del while True (Bucle Infinito)")
`````