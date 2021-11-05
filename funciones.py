import random,ast

#FUNCIÓN PARA CREAR EL ARCHIVO EXTERNO
def crear_archivo(nombre_archivo):
    archivo_numeros = open(nombre_archivo+".txt","w",encoding="utf8")
    lista = []

    for i in range(1000):
        numero = random.randint(1,50000)
        lista.append(numero)
    archivo_numeros.writelines(str((lista)))
    archivo_numeros.close()
    print(len(lista))

#FUNCIÓN PARA LEER EL ARCHIVO EXTERNO
def leer_datos_archivo(nombre_arc):
    archi1 = open(nombre_arc+".txt","r")
    lineas = ast.literal_eval(archi1.read())
    archi1.close()
    return lineas

#FUNCIÓN PARA REALIZAR UNA BUSQUEDA EN EL ÁRBOL
def find(root, data):
    currentNode = root

    if currentNode == None:
        return None
    else:
        if data == currentNode.data:
            
            return currentNode.data
        elif data < currentNode.data:
            
            return find(currentNode.left,data)
        else:
            return find(currentNode.right,data)

#INSERTAR ELEMENTOS AL ÁRBOL
def insertNode(root, node):

    if root == None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)
    return root