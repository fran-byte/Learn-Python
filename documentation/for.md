:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 9. for 
## Recorriendo LISTAS

En Pyton for se utiliza muy a menudo para recorrer el contenido de las listas, tuplas, diccionarios, etc...

````python
ns = [1,2,3,4,5,6,7,8,9]
for numero in ns:   # Vamos a ir pasandole cada indice de (ns) a (numero) y no finalizará hasta recorrerlo entero
                    # y se irá incrementando automáticamente el indice de (ns)
    print(numero) 
````