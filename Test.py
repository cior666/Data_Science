import numpy as np

a=np.array([[1, 2], [3, 4]])
print(a)
lista_alumnos=[] #declaro una lista vacia
lista_alumnos.append("CRO") #agrego elemento
lista_alumnos.append("ciorci")
print (lista_alumnos)

lista_random="gato", "perro", "raton",False,1.4,3,True,["uno", "dos", "tres"]
print(lista_random[7][0])
resultado=lista_random[7]
print(resultado[1])

lista_alumnos.pop(0)
print(lista_alumnos)

#SLICING
#lista[inicio:fin:salto]

#Tupla
#coleccion de datos inmutables, es decir, no se pueden modificar una vez creadas
#se declaran con () y no se puede agregar, sacar o modificar elementos
tupla_alumnos=("CRO", "ciorci", "gato", "perro", "raton")
print(tupla_alumnos[0])

#SET: estructura mas usada en estadistica, no tiene orden, no se pueden repetir elementos
#No admite duplicados, no tiene indices, es inmutable a la modificacion, 
# pero si a la eliminacion y adicion, para eliminar es discard o remove
#para agregar es add, metodo para chequear la diferencia entre dos conjuntos es difference
#y para la interseccion es intersection
set_numeros={1,2,3,4,5,6,7,8,9}
print(set_numeros)

#Diccionario: coleccion de datos en pares clave-valor, se declaran con {}
#se pueden modificar, agregar y eliminar elementos, no tiene orden
#para acceder a un elemento se usa la clave, no el indice, la clave es el primer elemento
#Almacena pares de valores.
alumnos_dicc={"CRO": 1, "ciorci": 2, "gato": 3, "perro": 4, "raton": 5}
print(alumnos_dicc["CRO"])

