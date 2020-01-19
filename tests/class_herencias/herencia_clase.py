#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 /
# Herencias de Clase
# En una tienda tenemos 3 tipos de Productos, Alimentos, Adornos y libros
# Todos los productos tienen en comun atributos de Referencia, Nombre, PVP y Descripción
# Los Adornos no tiene ningún atributo extra
# Los Alimentos tienen Productor y Distribuidor
# Los Libros tienen isbn y Autor
# Crea la clase y subclases correspondientes que sean herederas de la primera
# Crea otra clase llamada Teclado para llamar a cada uno de las sub clases y
# poder introducir los atributos correspondientes, para posteriormente imprimirlos

class Producto: # Creando la Super-Clase con atributos comunes a todos los productos
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self): # Método de formateo de string de Producto
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"
class Adorno(Producto): # Creando una Sub-Clase sin ningún atributo extra, tendrá solo los heredados de Producto
    pass

class Alimento(Producto): # Creando una Sub-Clase con dos atributos productor y distribuidor + los heredados
    productor = ""
    distribuidor = ""

    def __str__(self): # Método de formateo de string de Alimento
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"PRODUCTOR\t {self.productor}\n" \
               f"DISTRIBUIDOR {self.distribuidor}\n"


class Libro(Producto): # Creando una Sub-Clase con dos atributos isbn y autor + los heredados
    isbn = ""
    autor = ""

    def __str__(self): # Método de formateo de string de Libro
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.nombre}\n" \
               f"PVP\t\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n" \
               f"ISBN\t\t {self.isbn}\n" \
               f"AUTOR\t\t {self.autor}\n"

class Teclado:
    def __init__(self,opcion):
        self.opcion = opcion

        if (opcion)=="1":
            while True:
                try:
                    # Vamos introducir los atributos de Adorno
                    tecladoR,tecladoN,tecladoP,tecladoD = input("ADORNO: (Referencia, Nombre, PVP, Descripción) ").split()
                    a = Adorno(tecladoR, tecladoN, tecladoP, tecladoD)
                    return print(a)
                except:
                    print("Intentalo de nuevo recuerda dejar un espacio en blanco entre cada dato")

        elif (opcion)=="2":
            while True:

                try:
                    # Vamos introducir los atributos de Libro
                    tecladoR,tecladoN,tecladoP,tecladoD,tecladoISBN,tecladoA = input("LIBRO: (Referencia, Nombre, PVP, Descripción, ISBN, AUTOR) ").split()
                    a = Libro(tecladoR, tecladoN, tecladoP, tecladoD)
                    a.isbn = tecladoISBN
                    a.autor = tecladoA
                    return print(a)
                except:
                    print("Intentalo de nuevo recuerda dejar un espacio en blanco entre cada dato")

        elif (opcion)=="3":
            while True:

                try:
                    # Vamos introducir los atributos de Alimento
                    tecladoR,tecladoN,tecladoP,tecladoD,tecladoPro,tecladoD = input("ALIMENTO: (Referencia, Nombre, PVP, Descripción, Productor, Distribuidor) ").split()
                    a = Alimento(tecladoR, tecladoN, tecladoP, tecladoD)
                    a.productor = tecladoPro
                    a.distribuidor = tecladoD
                    return print(a)
                except:
                    print("Intentalo de nuevo recuerda dejar un espacio en blanco entre cada dato")
        elif (opcion) == "4":
            exit()

        else:
            return print("\nOpción Erronea !!\n")

while True:
    print("""Qué datos desea introducir
    1-Adornos
    2-Libros
    3-Alimetos
    4-Salir del Programa""")
    Teclado(input(">>  "))

