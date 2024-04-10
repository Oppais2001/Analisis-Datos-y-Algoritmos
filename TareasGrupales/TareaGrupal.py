
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
            print(nodo.valor, end=" ")
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
            print(nodo.valor, end=" ")
    def recorrido_preorden_Iterativo(self):
        if self.raiz is None:
            return
        pila = [self.raiz]
        while pila:
            nodo = pila.pop()
            print(nodo.valor, end=" ")
            pila.extend(reversed(nodo.hijos))

    def recorrido_postorden_Iterativo(self):
        if self.raiz is None:
            return

        pila = [self.raiz]

        while pila:
            nodo = pila[-1]
            if nodo.hijos:
                pila.extend(reversed(nodo.hijos))
                nodo.hijos = []
            else:
                print(pila.pop().valor, end=" ")
    
    def Eliminar_Nodo(self,nodo):
        padre = nodo.padre
        nodo.padre = None
        padre.Eliminar_Nodo_Hijo(nodo)
        nodo.hijos = []
    
    def Agregar_Nodo(self, nodo_padre, nodo_hijo):
        nodo_padre.Agregar_Nodo_Hijo(nodo_hijo)
        nodo_hijo.padre = nodo_padre
                       
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
        self.padre = None

    def Definir_Nodos_Hijos(self, Lista):
        self.hijos = Lista
        for hijo in Lista:
            hijo.padre = self
    
    def Imprimir__Nodos_Hijos(self):
        for hijo in self.hijos:
            print(hijo.valor)

    def Agregar_Nodo_Hijo(self, nodo):
        print("Se ha agregado de manera exitosa el nodo: ", nodo.valor, " como hijo del nodo: ", self.valor)
        self.hijos.append(nodo)

    def Eliminar_Nodo_Hijo(self, nodo):
        for hijo in self.hijos:
            if hijo.valor == nodo.valor:
                print("Se ha eliminado de manera exitosa el nodo: ", nodo.valor)
                self.hijos.remove(nodo)

def main():
    # Creacion de los nodos
    A = Nodo('A')
    B = Nodo('B')
    C = Nodo('C')
    D = Nodo('D')
    E = Nodo('E')
    F = Nodo('F')
    G = Nodo('G')
    # Definicion de los nodos hijos
    A.Definir_Nodos_Hijos([B,C])
    B.Definir_Nodos_Hijos([E,F,G])
    # Creacion del Arbol
    arbol = Arbol(A) # Se ingresa como argumento el nodo raiz
    arbol.Eliminar_Nodo(G) # Se elimina el nodo D del arbol
    arbol.Agregar_Nodo(A,D) # Agrega como hijo del nodo A al nodo D
    print("---Forma Recursiva----")
    print('\nRecorrido preorden:')
    arbol.recorrido_preorden(arbol.raiz)# A-B-E-F-C-D-
    print('\nRecorrido postorden:')
    arbol.recorrido_postorden(arbol.raiz)# E-F-B-C-D-A-
    print('\n')
    print("---Forma Iterativa----")
    print('\nRecorrido preorden:')
    arbol.recorrido_preorden_Iterativo()

    print('\nRecorrido postorden:')
    arbol.recorrido_postorden_Iterativo()

main()