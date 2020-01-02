
#			(_ _ _  _  __ |_   |_ _
#			| | (_|| )    |_)\/|_(-
#			                 / 
# Realizar una descomposición númerica para el número introducido
# Colocando el margen adecuado y rellenando con ceros a izquierdas
# y conseguir que las unidades esten debajo de las unidades, decenas debajo de decenas...



import sys # importando variables de sistema

exponent = 0

argLong= len(sys.argv)

print("\n")


if argLong == 2: # condicionando a 2 argumentos (1º Nombre de archivo[0] y 2º Argumento[1])

 

     number = int(sys.argv[1]) # guardando y convirtiendo argumento[1] string a número entero
     
     lonNum = len(sys.argv[1])

    

    

     if number > 0: # condicionando el argumento a número positivo

         for i in  reversed(sys.argv[1]): # introducimos el argumento[1]que es una string en i (de forma inversa)
            

             print("{:0{}}".format(10**exponent*int(i), lonNum))

             # multiplicando cada string(previamente convertido a número entero) a potencias de 10
 
             exponent+=1 # incrementando exponente
         
         print("\n")


     else:

         print("""Error de argumento, has introducido un número negativo
         por favor introduce como argumento un número entero positivo
         Ejemplo > python [NombreArchivo.py] [argumento1]""")

 
else:

     print("""Error de argumento has intoducido más de 1 argumento (sin contar el nombre de archivo),
     por favor introduce como argumento un número entero positivo
     Ejemplo > python [NombreArchivo.py] [argumento1]""")
