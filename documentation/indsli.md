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

Si queremos referirnos a cualquier índice lo haremos de la siguiente manera entre corchetes [ ]:
````python
print (palabra[3])
> 'h'
print (palabra[-5])
> 'y'
````

Podemos hacer _SLICING_ (Rebanando), es decir coger _**rebanadas**_ de esa cadena de texto anterior:
````python
print (palabra[2:-1]) # Una rebanada desde el índice 2 hasta el -1 pero sin tomar este último
> 'tho'
````
````python
print (palabra[:2]) # Desde el inicio (ya que lo hemos dejado vacío)
                    # hasta la posición 2, pero sin tomar esta última es decir el índice 0 y 1
````
> 'Py'
>
Si no especificamos en tre los corchetes ningún número nos recogera desde el inicio hasta el final [:]

Por el contrario si indicamos un índice que no existe nos dará un error.