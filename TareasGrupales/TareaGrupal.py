
class Arbol:
    '''
    Destinada a la creacion de arboles generales
    Atributos:
        raiz(Nodo): objeto de tipo nodo que servira como la raiz del arbol
    Metodos:
        recorrido_preorden: En un recorrido en preorden de un árbol, primero se visita el nodo raíz, luego se recorren recursivamente los hijos del nodo, generalmente de izquierda a derecha.
        recorrido_postorden: En un recorrido en postorden de un árbol, primero se recorren recursivamente los hijos del nodo, generalmente de izquierda a derecha, y luego se visita el nodo raíz.
    '''
    def __init__(self, nodo_raiz):
        self.raiz = nodo_raiz

    def recorrido_preorden(self, nodo):
        '''
        Visita la raíz del árbol.
        Recorre en preorden el subárbol izquierdo.
        Recorre en preorden el subárbol derecho.
        '''
        if nodo is not None:
            print(nodo.valor, end="-")
            for hijo in nodo.hijos:
                self.recorrido_preorden(hijo)

    def recorrido_postorden(self, nodo):
        '''
        Recorre en postorden el subárbol izquierdo.
        Recorre en postorden el subárbol derecho.
        Visita la raíz del árbol.
        '''
        if nodo is not None:
            for hijo in nodo.hijos:
                self.recorrido_postorden(hijo)
            print(nodo.valor, end="-")
    def recorrido_preorden_Iterativo(self, nodo):
        if nodo is None:
            return

        stack = [nodo]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.valor)
            stack.extend(reversed(node.hijos))

        return result
    def recorrido_postorden_Iterativo(self, nodo):
        if nodo is None:
            return

        stack = [nodo]
        result = []

        while stack:
            node = stack[-1]
            if node.hijos:
                stack.extend(node.hijos)
                node.hijos = []
            else:
                result.append(stack.pop().valor)

        return result[::-1]
    
    def Eliminar_nodo(self,nodo):
        if nodo is not None:
            nodo.hijos = []
    
    def Es_hijo_de(self, nodo):
        contador = 0
        if nodo is not None:
            for hijo in nodo.hijos:
                self.Es_hijo_de(hijo)

                       
class Nodo:
    '''
    Destinada a la creacion de nodos para formar estructuras de arboles generales
    Atributos:
        valor(str): valor que representa al nodo
        hijos[list[str]]: Lista de los nodos hijos por definicion los arboles generales pueden tener muchos nodos hijos
    Metodos:
        Definir_Nodos_Hijos: metodo que acepta una lista con los nodos hijos
    '''
    def __init__(self, valor):
        self.valor = valor            
        self.hijos = []
    def Definir_Nodos_Hijos(self, Lista):
        self.hijos = Lista


# Creacion de los nodos
A = Nodo('A')
B = Nodo('B')
C = Nodo('C')
D = Nodo('D')
E = Nodo('E')
F = Nodo('F')
# Definicion de los nodos hijos
A.Definir_Nodos_Hijos([B,C,D])
B.Definir_Nodos_Hijos([E,F])
#
arbol = Arbol(A)
print('\nRecorrido preorden:')
arbol.recorrido_preorden(arbol.raiz)# A-B-E-F-C-D-
print('\nRecorrido postorden:')
arbol.recorrido_postorden(arbol.raiz)# E-F-B-C-D-A-
print('\n')

print('\nRecorrido preorden:')
PilaPreorden = arbol.recorrido_preorden_Iterativo(arbol.raiz)
for node in PilaPreorden:
    print(node, end=",")

print('\nRecorrido postorden:')
PilaPostorden = arbol.recorrido_postorden_Iterativo(arbol.raiz)
for node1 in PilaPostorden:
    print(node1, end=",")

