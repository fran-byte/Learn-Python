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
# Calcula también la distancia entre esos puntos.

import math # Importamos la función Matemáticas

class Punto:
    def __init__(self,x=0,y=0): # Si no se reciben una coordenada, dejamos su valor a cero.
        self.x=x
        self.y=y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def vector(self,v): # este método recibe 2 puntos, el propio objeto (self) y el punto en "v"
                        # El resultado de vector AB = (x2-x1, y2-y1)

        if v.x > self.x:    # Condicionamos para que la resta siempre sea al mayor
                            # En este caso cogemos v.x que es el punto que le hemos pasado con anterioridad como(p1) en p.vector(p1)
                            # y self.x es el propio elemento de la instancia (p) en p.vector(p1) y hacemos lo propio para las "y"
            vectorx = v.x - self.x
        else:
            vectorx = self.x - v.x
        if v.y > self.y:
            vectory = v.y - self.y
        else:
            vectory = self.y - v.y
        print("El vector entre {} y {} es ({}, {})".format(self, v, vectorx,vectory))

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print('Estas coordenadas {} están en el Cuadrante 1'.format(self))# Formateamos con "self" que es el propio objeto
        elif self.x < 0 and self.y > 0:                                       # es decir el Punto
            print('Estas coordenadas {} están en el Cuadrante 2'.format(self))
        elif self.x < 0 and self.y < 0:
            print('Estas coordenadas {} están en el Cuadrante 3'.format(self))
        elif self.x > 0 and self.y < 0:
            print('Estas coordenadas {} están en el Cuadrante 3'.format(self))
        elif self.x == 0 and self.y != 0:
            print('{} Estás sobre el Eje de las Y'.format(self))
        elif self.x != 0 and self.y == 0:
            print('{} Estás sobre el Eje de las X'.format(self))
        else:
            print('{} Estás en el Origen'.format(self))

    def distancia(self,v):
        if v.x > self.x:    # Condicionamos para que la resta siempre sea al mayor
                            # En este caso cogemos v.x que es el punto que le hemos pasado con anterioridad como(p1) en p.vector(p1)
                            # y self.x es el propio elemento de la instancia (p) en p.vector(p1) y hacemos lo propio para las "y"
            dx = v.x - self.x
        else:
            dx = self.x - v.x
        if v.y > self.y:
            dy = v.y - self.y
        else:
            dy = self.y - v.y
        d = math.sqrt((dx**2)+(dy**2))
        print("La distancia entre {} y {} es ({})".format(self, v, d))


p = Punto(int(input("Punto P(X): ")),int(input("Punto P(Y): "))) # creamos el primer Pto

p.cuadrante() # Llevamos nuestro Objeto (Pto creado p) al metodo cuadrante

p1 = Punto(int(input("Punto P1(X): ")),int(input("Punto P1(Y): "))) # creamos el segundo Pto.

p1.cuadrante() # Llevamos nuestro Objeto (Pto creado p1) al metodo cuadrante

p.vector(p1) # Llevamos a nuestro método(vector) del pto p el p1
p.distancia(p1)  # Llevamos a nuestro método(distancia) del pto p el p1