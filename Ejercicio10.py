class Nodo:
  def __init__(self, valor, izquierdo=None, derecho=None):
    self.valor = valor
    self.izquierdo = izquierdo
    self.derecho = derecho

def contar_nodos_en_nivel(nodo, nivel):
  """
  Cuenta el número de nodos que hay en un nivel del árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
    nivel: El nivel actual en el que se encuentra.

  Retorno:
    La cantidad de nodos en el nivel especificado.
  """
  if nodo is None:
    return 0

  if nivel == 0:
    return 1

  return contar_nodos_en_nivel(nodo.izquierdo, nivel - 1) + contar_nodos_en_nivel(nodo.derecho, nivel - 1)

def esta_completo_nivel(nodo, nivel):
  """
  Determina si un nivel del árbol está completo.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
    nivel: El nivel actual en el que se encuentra.

  Retorno:
    True si el nivel está completo, False en caso contrario.
  """
  if nodo is None:
    return False

  if nivel == 0:
    return True

  izquierdo_completo = esta_completo_nivel(nodo.izquierdo, nivel - 1)
  derecho_completo = esta_completo_nivel(nodo.derecho, nivel - 1)

  return izquierdo_completo and derecho_completo

def calcular_nodos_faltantes(nodo, nivel):
  """
  Calcula la cantidad de nodos que faltan para completar un nivel del árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
    nivel: El nivel actual en el que se encuentra.

  Retorno:
    La cantidad de nodos que faltan para completar el nivel especificado.
  """
  if nodo is None:
    return 2 ** nivel

  nodos_en_nivel = contar_nodos_en_nivel(nodo, nivel)
  nodos_completos = 2 ** nivel

  return nodos_completos - nodos_en_nivel

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.derecho = Nodo(6)

nivel = 2  # Nivel que se desea evaluar

cantidad_nodos_nivel = contar_nodos_en_nivel(raiz, nivel)
print(f"Cantidad de nodos en el nivel {nivel}: {cantidad_nodos_nivel}")

if esta_completo_nivel(raiz, nivel):
  print(f"El nivel {nivel} está completo.")
else:
  nodos_faltantes = calcular_nodos_faltantes(raiz, nivel)
  print(f"El nivel {nivel} no está completo. Faltan {nodos_faltantes} nodos.")
