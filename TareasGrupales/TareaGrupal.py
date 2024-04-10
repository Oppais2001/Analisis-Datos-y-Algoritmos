
class Arbol:
    '''
    Destinada a la creacion de arboles generales
    Atributos:
        raiz(Nodo): objeto de tipo nodo que servira como la raiz del arbol
    Metodos:
        Agregar_Nodo: metodo que requiere de un nodo padre y un nodo hijo, para agregar un nuevo nodo.
        Eliminar_Nodo: metodo hecho para eliminar todas las conexiones de un padre a un nodo a eliminar, y a su ves eliminar todas las conexiones que tiene con sus hijos.
        recorrido_preorden_Recursivo: En un recorrido en preorden de un árbol, primero se visita el nodo raíz, luego se recorren recursivamente los hijos del nodo, de izquierda a derecha.
        recorrido_postorden_Recursivo: En un recorrido en postorden de un árbol, primero se recorren recursivamente los hijos del nodo, generalmente de izquierda a derecha, y luego se visita el nodo raíz.
        recorrido_preorden_Iterativo: En un recorrido en postorden de un árbol, mediante el uso de pila y la activacion de un bucle, el bucle estara activo mientras la pila este no vacia, el primer valor de la pila es la raiz del arbol, luego pasan a ser sus hijos(eliminando el nodo padre de la pila), hasta llegar a un nodo que no tenga hijos.
        recorrido_postorden_Iterativo: En un recorrido en postorden de un árbol, mediante el uso de pila y la activacion de un bucle, el bucle estara activo mientras la pila este no vacia, el primer valor de la pila es la raiz del arbol, luego pasan a ser sus hijos(eliminando los nodos hijos del nodo padre), hasta hacer que ningun nodo tenga hijos.
    '''
    def __init__(self, nodo_raiz):
        self.raiz = nodo_raiz

    def recorrido_preorden_Recursivo(self, nodo):
        '''
        Visita la raíz del árbol.
        Recorre en preorden el subárbol izquierdo.
        Recorre en preorden el subárbol derecho.
        '''
        if nodo is not None:
            print(nodo.valor, end=" ")# Imprime el valor del nodo
            for hijo in nodo.hijos: # si tiene hijos
                self.recorrido_preorden_Recursivo(hijo)# ingresa los hijos a la funcion de manera recursiva

    def recorrido_postorden_Recursivo(self, nodo):
        '''
        Recorre en postorden el subárbol izquierdo.
        Recorre en postorden el subárbol derecho.
        Visita la raíz del árbol.
        '''
        if nodo is not None:
            for hijo in nodo.hijos:
                self.recorrido_postorden_Recursivo(hijo)
            print(nodo.valor, end=" ") # Imprime el valor del nodo que ya ha imprimido todos sus hijos, o que no tiene hijos
    def recorrido_preorden_Iterativo(self):
        if self.raiz is None: # si la raiz esta vacia no se recorre
            return
        
        pila = [self.raiz] # Se crea una pila con el elemento raiz

        while pila: # el bucle funciona hasta que la lista este vacia 
            nodo = pila.pop() # Se toma el ultimo valor y a su ves se elimina
            print(nodo.valor, end=" ") # Se imprime el valor antes mencionado
            pila.extend(reversed(nodo.hijos)) # Agregamos los hijos a la pila, al usar el metodo reversed volteamos la lista de manera que el primer hijo sea el ultimo elemento de la lista y por lo tanto el sgte elemento a recorrer

    def recorrido_postorden_Iterativo(self):
        if self.raiz is None:
            return
        
        pila = [self.raiz]

        while pila:
            nodo = pila[-1]# Se toma el ultimo valor
            if nodo.hijos:# Si tiene hijos
                pila.extend(reversed(nodo.hijos))# Se agregan sus hijos a la pila
                nodo.hijos = []# Se borran sus hijos
            else: # Si no tiene hijos
                print(pila.pop().valor, end=" ") # Se elimina e imprime el valor
    
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
        hijos(list[Nodo]): Lista de los nodos hijos por definicion los arboles generales pueden tener muchos nodos hijos
        padre(Nodo): valor que representa al padre del nodo
    Metodos:
        Definir_Nodos_Hijos: metodo que acepta una lista con los nodos hijos
        Imprimir_Nodos_Hijos: metodo que imprime todos los nodos hijos del nodo actual
        Agregar_Nodo_Hijo: metodo que agrega un nodo como hijo del nodo actual
        Eliminar_Nodo_Hijo: metodo que elimina un nodo hijo del nodo actual
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
    print('Recorrido en preorden:')
    arbol.recorrido_preorden_Recursivo(arbol.raiz)
    print('\nRecorrido en postorden:')
    arbol.recorrido_postorden_Recursivo(arbol.raiz)
    print("\n---Forma Iterativa----")
    print('Recorrido en preorden:')
    arbol.recorrido_preorden_Iterativo()

    print('\nRecorrido en postorden:')
    arbol.recorrido_postorden_Iterativo()

main()