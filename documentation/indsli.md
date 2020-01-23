:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)


# 4. INDICES y SLICING

En la siguiente cadena de texto, podemos identificar cada caracter mediante un índice.
````python


palabra = "Python"
````

>"P" índice 0  ... o ...  - 6
>
>"y" índice 1 ...  o ...  - 5
>
>"t" índice 2 ...  o ...  - 4
>
>"h" índice 3 ...  o ...  - 3
>
>"o" índice 4 ...  o  ... - 2
>
>"n" índice 5 ...  o ...  - 1

Si queremos referirnos a cualquier índice lo haremos de la siguiente manera entre corchetes []:
````python
print (palabra[3])
> 'h'
````