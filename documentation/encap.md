:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 28. ENCAPSULACIÓN de Atributos y Métodos

Esta técnica consiste en bloquear el acceso a atributos y métodos internos de la clase al acceder desde el exterior.

Podemos simularlo (Ya que en Python NO EXISTE) de esta forma:

##Bloqueando ATRIBUTOS:

````python
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

e = Ejemplo()
print(e.__atributo_privado)
````
>---------------------------------------------------------------------------
>AttributeError                            Traceback (most recent call last)
<ipython-input-3-eed1a613919b> in <module>()
----> 1 print(e.__atributo_privado)

AttributeError: 'Ejemplo' object has no attribute '__atributo_privado'



##Bloqueando METODOS:

````python
class Ejemplo:
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

e = Ejemplo()
e.__metodo_privado()
````
---------------------------------------------------------------------------
>AttributeError                            Traceback (most recent call last)
<ipython-input-5-81c514698440> in <module>()
----> 1 e.__metodo_privado()

>AttributeError: 'Ejemplo' object has no attribute '__metodo_privado'

Sea como sea para acceder a esos datos se deberían crear métodos públicos que hagan de interfaz. 
En otros lenguajes les llamaríamos getters y setters y es lo que da lugar a las propiedades, 
que no son más que atributos protegidos con interfaces de acceso:

````python
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()
````
>Soy un atributo inalcanzable desde fuera.  
Soy un método inalcanzable desde fuera.