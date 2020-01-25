:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 10. for  Continuamos iterando 
## "Modificando al vuelo" cadenas (inmutables)

Realmente no se pueden Modificar, pero vamos a hacer algo parecido.

````python
cadena1 = "Python"
cadena2 = ""

for caracter in cadena1:
    cadena2+=caracter*2 # Una simple modificación multiplicar el elemento x 2
print(cadena2)
    
  
````
> PPyytthhoonn