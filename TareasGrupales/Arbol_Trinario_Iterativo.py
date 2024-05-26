class NodoTrinario:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.medio = None
        self.derecha = None

class ArbolTrinarioIterativo:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = NodoTrinario(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        actual = self.raiz
        while actual:
            if valor < actual.valor:
                if actual.izquierda is None:
                    actual.izquierda = nuevo_nodo
                    return
                actual = actual.izquierda
            elif valor == actual.valor:
                if actual.medio is None:
                    actual.medio = nuevo_nodo
                    return
                actual = actual.medio
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo_nodo
                    return
                actual = actual.derecha

    def _eliminar_valor(self, valor):
        actual = self.raiz
        padre = None
        es_izquierda = True

        while actual and actual.valor != valor:
            padre = actual
            if valor < actual.valor:
                actual = actual.izquierda
                es_izquierda = True
            elif valor > actual.valor:
                actual = actual.derecha
                es_izquierda = False
            else:  # valor == actual.valor
                if actual.medio is not None:
                    # Reemplazar con el hijo medio
                    if padre is None:
                        self.raiz = actual.medio
                    elif es_izquierda:
                        padre.izquierda = actual.medio
                    else:
                        padre.derecha = actual.medio
                    return True
                else:
                    # No hay hijo medio, se procede a eliminar como en un árbol binario
                    if actual.izquierda is not None and actual.derecha is not None:
                        # Caso con dos hijos: encontrar el sucesor in-order
                        sucesor = actual.derecha
                        while sucesor.izquierda is not None:
                            sucesor = sucesor.izquierda
                        valor_sucesor = sucesor.valor
                        self.eliminar(valor_sucesor)
                        actual.valor = valor_sucesor
                        return True
                    elif actual.izquierda is not None:
                        if padre is None:
                            self.raiz = actual.izquierda
                        elif es_izquierda:
                            padre.izquierda = actual.izquierda
                        else:
                            padre.derecha = actual.izquierda
                        return True
                    elif actual.derecha is not None:
                        if padre is None:
                            self.raiz = actual.derecha
                        elif es_izquierda:
                            padre.izquierda = actual.derecha
                        else:
                            padre.derecha = actual.derecha
                        return True
                    else:
                        # Caso sin hijos
                        if padre is None:
                            self.raiz = None
                        elif es_izquierda:
                            padre.izquierda = None
                        else:
                            padre.derecha = None
                        return True

        return False  # No se encontró el nodo
