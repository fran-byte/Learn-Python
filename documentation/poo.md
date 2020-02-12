:page_with_curl: [README](../README.md) :books: [Material didáctico](/documentation/indicedocu.md) :pencil: [Ejercicios](/tests/indicetests.md)

# 25. POO


La programación orientada a objetos (POO, u OOP según sus siglas en inglés) es un paradigma de programación que viene a innovar la forma de obtener resultados.

Los objetos manipulan los datos de entrada para la obtención de datos de salida específicos, donde cada objeto ofrece una funcionalidad especial.

# CLASES
Podemos definir una clase como una Plantilla o modelo para crear a partir de ella ciertos Objetos. Esta plantilla es la que contiene la información; características y capacidades que tendrá el objeto que sea creado a partir de ella.

Así a su vez los objetos creados a partir de ella estarán agrupados en esa misma clase.

````python
Class Nombredelaclase (object): #Declaramos la clase nuestra que hereda de Object

 def  __init__ (self, parámetros): #Constructor de la clase

# apartir de aqui declaramos los atributos
````

## El método constructor de la clase en Python (__init__)

Si hablamos de métodos de una clase puede existir diferentes tipos de ellos.

Pero el mas importante es el método constructor; el cual dicho nombre hace referencia a inicializar los atributos del objeto creado a partir  de la clase que lo posea.

Por supuesto no es necesario que este método exista dentro de una clase para que la clase exista. Pero si es necesario para indicarle al interprete de Python que cuando se Instancia un objeto a dicha clase debe asignarle los argumentos que nosotros le damos al momento de la instancia. (inicialización de atributos)