#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 /
#
# Ejercicio:
# Crea una clase llamada Punto con sus dos coordenadas X e Y.
# Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
# Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
# Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto,
# teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y,
# si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
# Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.

import math # Importamos la función Matemáticas

class Punto: # Creamos la clase Punto

    def __init__(self, x=0, y=0): # La definimos así misma y sus 2 variables x e y
        self.x = x
        self.y = y

    def __str__(self): # Método string
        return "({}, {})".format(self.x, self.y) # Al imprimir por pantalla el formato sera (X,Y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} se sitúa sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} se sitúa sobre el eje Y".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )

    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format(
            self, p, d))


class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

        # Hago los cálculos, pero no llamo los atributos igual
        # que los métodos porque sino podríamos sobreescribirlos
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ) )

    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ) )

    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ) )


A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()


