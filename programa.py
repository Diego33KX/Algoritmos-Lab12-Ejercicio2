from funciones import leer_datos_archivo, crear_archivo,find,insertNode
from timeit import default_timer as timer

class BSTNode:
    '''
    Node BST definition
    '''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

nombre_archivo = "lista_numeros"
##############################
#CREACIÓN DE ARCHIVO
##############################
crear_archivo(nombre_archivo)

##############################
#LEER ARCHIVO CREADO
##############################
lista_de_numeros = leer_datos_archivo(nombre_archivo)

##############################
#CANTIDAD DE ELEMENTOS
##############################
print(len(lista_de_numeros))

##############################
#CREAR EL ARBOL ------>
##############################
lista_datos_nodo = []

for x in lista_de_numeros:
    lista_datos_nodo.append(BSTNode(x))

for i in lista_datos_nodo:
    if i == lista_datos_nodo[0]:
        root = lista_datos_nodo[0]
    else:
         insertNode(root, i)
import tree as t
t.printLevelOrder(root)
print()
print("NODOS PRINCIPALES")
print("root.data =",root.data)
print("root.left.data =",root.left.data)
print("root.right.data =",root.right.data)
###############################
#BUSCAR ELEMENTOS EN EL ÁRBOL
###############################


###############################
#MEDIR EL TIEMPO DE 3 BÚSQUEDAS
###############################
print()
print("BUSQUEDA")
start=timer()
if __name__ == '__main__':
    datos = find(root,100)
    if datos == None:
        print('No se encontró dicho número')
    else:
        print("El número ",datos, " si se encontró en la lista")

if __name__ == '__main__':
    datos = find(root,25)
    if datos == None:
        print('No se encontró dicho número')
    else:
        print("El número ",datos, " si se encontró en la lista")

if __name__ == '__main__':
    datos = find(root,40)
    if datos == None:
        print('No se encontró dicho número')
    else:
        print("El número ",datos, " si se encontró en la lista")

end=timer()
delay=end-start
print()
print("> Tiempo de búsqueda {}".format(delay))




