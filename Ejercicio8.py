class Nodo:
  def __init__(self, valor, izquierdo=None, derecho=None):
    self.valor = valor
    self.izquierdo = izquierdo
    self.derecho = derecho

def obtener_minimo(nodo):
  """
  Obtiene el nodo con el valor mínimo del árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.

  Retorno:
    El nodo con el valor mínimo del árbol.
  """
  if nodo is None:
    return None

  minimo = nodo
  minimo_izquierdo = obtener_minimo(nodo.izquierdo)
  minimo_derecho = obtener_minimo(nodo.derecho)

  if minimo_izquierdo is not None and minimo_izquierdo.valor < minimo.valor:
    minimo = minimo_izquierdo
  if minimo_derecho is not None and minimo_derecho.valor < minimo.valor:
    minimo = minimo_derecho

  return minimo

def obtener_maximo(nodo):
  """
  Obtiene el nodo con el valor máximo del árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.

  Retorno:
    El nodo con el valor máximo del árbol.
  """
  if nodo is None:
    return None

  maximo = nodo
  maximo_izquierdo = obtener_maximo(nodo.izquierdo)
  maximo_derecho = obtener_maximo(nodo.derecho)

  if maximo_izquierdo is not None and maximo_izquierdo.valor > maximo.valor:
    maximo = maximo_izquierdo
  if maximo_derecho is not None and maximo_derecho.valor > maximo.valor:
    maximo = maximo_derecho

  return maximo

# Ejemplo de uso
raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)
raiz.izquierdo.izquierdo = Nodo(2)
raiz.izquierdo.derecho = Nodo(7)
raiz.derecho.izquierdo = Nodo(12)
raiz.derecho.derecho = Nodo(20)

nodo_minimo = obtener_minimo(raiz)
print(f"Valor mínimo del árbol: {nodo_minimo.valor}")

nodo_maximo = obtener_maximo(raiz)
print(f"Valor máximo del árbol: {nodo_maximo.valor}")
