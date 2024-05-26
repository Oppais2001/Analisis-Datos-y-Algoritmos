class Node:
    def __init__(self, val):
        self.valor = val
        self.medio = None
        self.izquierda = None
        self.derecha = None

class Arbol_Trinario_Iterativo:
    def __init__(self):
        self.raiz = None

    def insertar(self, val):
        raiz = self.raiz
        if raiz is None:
            self.raiz = Node(val)
            return
        currentNode = raiz
        newNode = Node(val)

        while (currentNode):
            if (val < currentNode.valor):
                if currentNode.izquierda is None:
                    currentNode.izquierda = newNode
                    break
                else: 
                    currentNode = currentNode.izquierda
      
            elif (val > currentNode.valor):
                if currentNode.derecha is None:
                    currentNode.derecha = newNode
                    break
                else:
                    currentNode = currentNode.derecha
      
            else:
                if currentNode.medio is None:
                    currentNode.medio = newNode
                    break
                else:
                    currentNode = currentNode.medio
    
    def _eliminar_valor(self, valor):
        if self.root is None:
            return
        currentNode = self.root
        newNode = Node(None)
        while (currentNode):
            if (valor < currentNode.value):
                if currentNode.left is None:
                    currentNode.left = newNode
                    break
                else: 
                    currentNode = currentNode.left
      
            elif (valor > currentNode.value):
                if currentNode.right is None: 
                    currentNode.right = newNode
                    break
                else: 
                    currentNode = currentNode.right
      
            else:
                if currentNode.center is None:
                    currentNode.center = newNode
                    break
                else: 
                    currentNode = currentNode.center

