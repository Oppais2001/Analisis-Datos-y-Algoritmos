class ArbolTrinarioRecursivo(object): # Recursivo
  """Implementa insercion y eliminacion en un árbol trinario. 
  Un árbol tri-nary es muy parecido a un árbol binario, pero con tres nodos secundarios para 
  cada padre en lugar de dos, con el nodo izquierdo siendo valores menores que el
  padre, los valores del nodo derecho mayores que el padre y los nodos centrales 
  valores iguales a los del elemento primario.
  
  Por ejemplo, supongamos que agregué los siguientes nodos al árbol en este orden: 
    5, 4, 9, 5, 7, 2, 2.
    
  El árbol resultante se vería así:
          5 
        / | \
      4   5   9 
    /        /
   2        7 
   | 
   2
  """
  
  class Node:
    """Objeto para un único nodo primario en un árbol.
    Cada nodo tiene un nodo izquierdo, derecho y medio, donde el nodo izquierdo tiene valores 
    menor que el principal, el nodo derecho tiene valores mayores que el primario y
    El nodo central tiene valores iguales a los del nodo principal. 
    """
    def __init__(self, valor):
      self.valor = valor
      self.izquierda = None
      self.medio = None
      self.derecha = None

  def __init__(self):
    self.raiz = None
  
  def __str__(self):
    return self._print_in_order(self.raiz, nodes=[]) 
      
  def _print_in_order(self, raiz, nodes):
    if raiz is not None:  
      self._print_in_order(raiz.izquierda, nodes)
      nodes.append(raiz.valor)
      self._print_in_order(raiz.medio, nodes)
      self._print_in_order(raiz.derecha, nodes)
    return str(nodes)
  
  def insertar(self, valor):
    """Agrega una clave a un subárbol."""
    if type(valor) == list: #Detecta cuando se inserta una lista de elementos al arbol
      return [self._insertar_valor(k, self.raiz) for k in valor] # Recorre la lista insertando uno a uno los elementos de la misma
    return self._insertar_valor(valor, self.raiz) # Si no es lista se tiene que es un elemento unico, el cual se agrega

  def _insertar_valor(self, valor, raiz):
    if raiz is None:# Comprueba que si el nodo existe
      raiz = ArbolTrinarioRecursivo.Node(valor)# Usando la clase nodo propia del arbol crea un nodo usando el valor ingresado
    elif valor == raiz.valor: # en caso de no serla comprueba el nuevo valor a ingresar con la raiz, en caso de ser igual...
      raiz.medio = self._insertar_valor(valor, raiz.medio)# Si el elemento que esta al medio existe, hace nuevamente las comprobaciones, sabiendo que el del medio siempre es igual se crearia una suerte de linea hacia abajo en el arbol, si no existe pasa a crear un nuevo nodo que estaria en la posicion del medio de la raiz
    elif valor < raiz.valor:
      raiz.izquierda = self._insertar_valor(valor, raiz.izquierda)# Si el elemento que esta a izquierda existe, hace nuevamente las comprobaciones, se compara nuevamente con el nodo izquierdo si es mayor, igual o menor, hasta llegar a reemplazar un nodo vacio
    else:
      raiz.derecha = self._insertar_valor(valor, raiz.derecha)# Si el elemento que esta a derecha existe, hace nuevamente las comprobaciones, se compara nuevamente con el nodo derecho si es mayor, igual o menor, hasta llegar a reemplazar un nodo vacio
    if self.raiz is None:
      self.raiz = raiz # en el caso de no haber una raiz definida, mediante la comprobacion pre
    return raiz # retorna el nuevo nodo, o el nodo padre del valor ingresado en caso de existir
    
  def eliminar(self, valor):
    """Elimina una clave de un subárbol."""
    return self._eliminar_valor(valor, self.raiz)

  def _eliminar_valor(self, valor, raiz):
    if raiz is None: # es el caso que al recorrer no exista el valor dentro del arbol
       raise ValueError()
    if valor < raiz.valor: # Misma logica que se usa en el caso de añadir 
       raiz.izquierda = self._eliminar_valor(valor, raiz.izquierda)
    elif (valor > raiz.valor):
       raiz.derecha = self._eliminar_valor(valor, raiz.derecha)
    elif (valor == raiz.valor):
      if(raiz.medio is not None):
         raiz.medio = raiz.medio.medio
      elif (raiz.derecha is not None):# En el caso de eliminar el valor que tenga los dos hijos, sera reemplazado por el menor valor del subarbol derecho
        raiz.valor = self._find_min(raiz.derecha).valor
        raiz.derecha = self._eliminar_valor(raiz.valor, raiz.derecha) 
      elif (raiz.izquierda is not None):
        raiz = raiz.izquierda
      elif (raiz == self.raiz):# Agregue una forma de que al eliminar todo, se pueda eliminar la raiz
        self.raiz = None
      else:
        raiz = None
    return raiz
         
  def _find_min(self, raiz):
    """Encuentra el valor mínimo de un árbol (o subárbol)."""
    if raiz.izquierda is None:
      return raiz
    return self._find_min(raiz.izquierda)
     
t = ArbolTrinarioRecursivo()

print('metodo insertar: (5,4, 9, 5, 7, 2, 2)')
t.insertar([5, 4, 9, 5, 7, 2, 2])
print(t, '\n')

print('metodo eliminar valor 5')
t.eliminar(5)
print(t, '\n')

print('metodo eliminar valor 9')
t.eliminar(9)
print(t, '\n')

print('metodo insertar valor 6')
t.insertar(6)
print(t, '\n')
    