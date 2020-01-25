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

## Simulando (for) como si fuera otros lenguajes

````python
for i in range(10): # 0 a 9
  print(i)
````

>0  
>1  
>2  
>3  
>4  
>5  
>6  
>7  
>8  
>9

range (x,y,z)

x = será el inicio desde donde empezará a iterar el (for) (si no se coloca, por defecto será 0)

y = el valor que representa ese rango (-1)

z = será el incremento, si se deja vacío, por defecto será 1