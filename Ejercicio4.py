class Nodo:
  """
  Clase para representar un nodo en un árbol binario.

  Atributos:
    dato: El dato del nodo.
    izquierda: Enlace al nodo hijo izquierdo.
    derecha: Enlace al nodo hijo derecho.
  """

  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None

def obtener_hijo_derecho(nodo):
  """
  Devuelve el hijo derecho de un nodo.

  Argumentos:
    nodo: El nodo del que se desea obtener el hijo derecho.

  Retorno:
    El nodo hijo derecho, o None si el nodo no tiene hijo derecho.
  """
  if nodo is None:
    return None
  return nodo.derecha

def obtener_hijo_izquierdo(nodo):
  """
  Devuelve el hijo izquierdo de un nodo.

  Argumentos:
    nodo: El nodo del que se desea obtener el hijo izquierdo.

  Retorno:
    El nodo hijo izquierdo, o None si el nodo no tiene hijo izquierdo.
  """
  if nodo is None:
    return None
  return nodo.izquierda

# Ejemplo de uso
nodo = Nodo(10)
nodo.izquierda = Nodo(5)
nodo.derecha = Nodo(15)

hijo_derecho = obtener_hijo_derecho(nodo)
print(f"Hijo derecho de {nodo.dato}: {hijo_derecho.dato}")

hijo_izquierdo = obtener_hijo_izquierdo(nodo)
print(f"Hijo izquierdo de {nodo.dato}: {hijo_izquierdo.dato}")
