#Importamos todas la clases que vamos a utilizar
from paquete_archivos.miarchivo import *
from modelado.mimodelo import *
from metodo_ordenar.combinacion import *

objLeer = MiArchivo()									#Creamos un objeto tipo MiArchivo para leer el archivo
lista_datos = objLeer.obtener_informacion()				#Declaramos una lista para alamacenar la informacion del objeto objLeer
lista_datos = [l.split(";") for l in lista_datos]		#Separamos con el split los datos de la lista con el caracter ";""

lista_datos2 = []										#Creamos dos listas vacias 
lista_edad = []

print("Listado de datos")
for d in lista_datos:									#Creamos un for para recorrer la lista con datos recibidos
    p = Persona(d[0],d[1],d[2])      					#Creamos un objeto persona para enviarle a su constructor
    lista_datos2.append(p)								#Agregamos a la lista 2 el objeto con todos los datos	
    print(p)											#Presentamos los datos acumulados en el objeto

for n in lista_datos2:									#creamos un for para recorrer la lista_datos2
	lista_edad.append(n.obtener_edad())					#Asignamos las edades a la nueva lista
print(merge_sort(lista_edad))  							#Llamamos al metodo que ordena y lo imprimos con la lista ordenada