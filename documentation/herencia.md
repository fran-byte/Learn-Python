:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 29. HERENCIA

Capacidad que de una clase de heredar los atributos y métodos de otra, y poder reutilizar el código.

## Superclases
Vamos a crear una clase base (la superclase) con los atriutos comunes y luego crear las demás clases heredando de ella (las subclases) extendiendo sus campos específicos.
````python
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"
````

## Subclases
Para heredar los atributos y métodos de una clase en otra sólo tenemos que pasarla entre paréntesis durante la definición:

````python
class Adorno(Producto):
    pass

adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
print(adorno)
````

>REFERENCIA      2034  
NOMBRE          Vaso adornado  
PVP             15  
DESCRIPCIÓN     Vaso de porcelana  

Como se puede apreciar es posible utilizar el comportamiento de una superclase sin definir nada en la subclase.

Respecto a las demás subclases como se añaden algunos atributos, podríamos definirlas de esta forma:

````python
class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t\t {self.productor}\n" \
               f"DISTRIBUIDOR\t\t {self.distribuidor}\n"


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"
````

Ahora para utilizarlas simplemente tendríamos que establecer los atributos después de crear los objetos:


````python
alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ML")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
print(alimento)

libro = Libro(2036, "Cocina Mediterránea",9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(libro)
````

## Trabajando en conjunto

Gracias a la flexibilidad de Python podemos manejar objetos de distintas clases masivamente de una forma muy simple.

Vamos a empezar creando una lista con nuestros tres productos de subclases distintas:

````python
productos = [adorno, alimento]
productos.append(libro)

print(productos)
````
> [<__main__.Adorno at 0x14c58660940>,
<__main__.Alimento at 0x14c586608d0>,
<__main__.Libro at 0x14c58660978>]


Ahora si queremos recorrer todos los productos de la lista podemos usar un bucle for:
````python
for producto in productos:
    print(producto, "\n")
````
También podemos acceder a los atributos, siempre que sean compartidos entre todos los objetos:

````python
for producto in productos:
    print(producto.referencia, producto.nombre)
````

>2034 Vaso adornado  
2035 Botella de Aceite de Oliva Extra  
2036 Cocina Mediterránea  

Si un objeto no tiene el atributo al que queremos acceder nos dará error:

````python
    print(producto.autor)
````

>---------------------------------------------------------------------------
>AttributeError                            Traceback (most recent call last)  
<ipython-input-8-36e9baf5c1cc> in <module>()  
    1 for producto in productos:  
----> 2     print(producto.autor)  
>
>AttributeError: 'Adorno' object has no attribute 'autor'

Por suerte podemos hacer una comprobación con la función isinstance() para determinar si una instancia es de una determinado clase y así mostrar unos atributos u otros:

````python
for producto in productos:
    if( isinstance(producto, Adorno) ):
        print(producto.referencia, producto.nombre)
    elif( isinstance(producto, Alimento) ):
        print(producto.referencia, producto.nombre, producto.productor)
    elif( isinstance(producto, Libro) ):
        print(producto.referencia, producto.nombre, p.isbn)   
````
>2034 Vaso adornado  
2035 Botella de Aceite de Oliva La Aceitera  
2036 Cocina Mediterránea 0-123456-78-9  

## Polimorfismo
El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases pueden responder a una misma acción.

La polimorfia es implícita en Python, ya que todas las clases son subclases de una superclase común llamada Object.

Por ejemplo la siguiente función aplica una rebaja al precio de un producto:

````python
def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)
````
Gracias al polimorfismo no tenemos que comprobar si un objeto tiene o no el atributo pvp, simplemente intentamos acceder y si existe premio:

````python
print(alimento, "\n")
rebajar_producto(alimento, 10)
print(alimento)
````
>REFERENCIA      2035  
NOMBRE          Botella de Aceite de Oliva  
PVP             5  
DESCRIPCIÓN     250 ML  
PRODUCTOR       La Aceitera  
DISTRIBUIDOR    Distribuciones SA  
>
>REFERENCIA      2035  
NOMBRE          Botella de Aceite de Oliva  
PVP             4.5  
DESCRIPCIÓN     250 ML  
PRODUCTOR       La Aceitera  
DISTRIBUIDOR    Distribuciones SA  

Por cierto, como podéis ver en el ejemplo, cuando modificamos un atributo de un objeto dentro de una función éste cambia en la instancia. Esto es por aquello que os comenté del paso por valor y referencia.