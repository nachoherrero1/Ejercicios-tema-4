class Nodo:
  """
  Clase para representar un nodo en un árbol binario.

  Atributos:
    dato: El dato del nodo (operador o número).
    izquierda: Enlace al nodo hijo izquierdo.
    derecha: Enlace al nodo hijo derecho.
  """

  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None

def crear_arbol_exponencial(base, exponente):
  """
  Crea un árbol binario exponencial recursivamente.

  Argumentos:
    base: La base de la potencia.
    exponente: El exponente de la potencia.

  Retorno:
    El nodo raíz del árbol binario exponencial.
  """
  if exponente == 0:
    return Nodo(base)

  izquierdo = crear_arbol_exponencial(base, exponente - 1)
  derecho = crear_arbol_exponencial(base, exponente - 2)
  return Nodo("*", izquierdo, derecho)

def preorden(nodo):
  """
  Recorre el árbol en preorden.

  Argumentos:
    nodo: El nodo raíz del árbol.

  Retorno:
    Una lista con los datos del árbol en preorden.
  """
  if nodo is None:
    return []
  return [nodo.dato] + preorden(nodo.izquierda) + preorden(nodo.derecha)

def inorden(nodo):
  """
  Recorre el árbol en inorden.

  Argumentos:
    nodo: El nodo raíz del árbol.

  Retorno:
    Una lista con los datos del árbol en inorden.
  """
  if nodo is None:
    return []
  return inorden(nodo.izquierda) + [nodo.dato] + inorden(nodo.derecha)

def postorden(nodo):
  """
  Recorre el árbol en postorden.

  Argumentos:
    nodo: El nodo raíz del árbol.

  Retorno:
    Una lista con los datos del árbol en postorden.
  """
  if nodo is None:
    return []
  return postorden(nodo.izquierda) + postorden(nodo.derecha) + [nodo.dato]

def evaluar_expresion(nodo):
  """
  Evalúa la expresión matemática representada por el árbol binario.

  Argumentos:
    nodo: El nodo raíz del árbol.

  Retorno:
    El resultado de la evaluación de la expresión.
  """
  if nodo.dato.isdigit():
    return int(nodo.dato)

  operador = nodo.dato
  izquierdo = evaluar_expresion(nodo.izquierda)
  derecho = evaluar_expresion(nodo.derecha)

  if operador == "+":
    return izquierdo + derecho
  elif operador == "-":
    return izquierdo - derecho
  elif operador == "*":
    return izquierdo * derecho
  elif operador == "/":
    return izquierdo / derecho
  else:
    raise ValueError(f"Operador inválido: {operador}")

# Ejemplo de uso
base = 2
exponente = 5

arbol_exponencial = crear_arbol_exponencial(base, exponente)

print("Recorrido preorden:", preorden(arbol_exponencial))
print("Recorrido inorden:", inorden(arbol_exponencial))
print("Recorrido postorden:", postorden(arbol_exponencial))

resultado = evaluar_expresion(arbol_exponencial)
print(f"Resultado de la expresión: {resultado}")

# Determinación del barrido correcto
barridos = [preorden, inorden, postorden]
for barrido in barridos:
  recorrido = barrido(arbol_exponencial)
  if recorrido == [base, "*", base, "*", base, "*", base, "*"]:
    barrido_correcto = barrido.__name__
    break

print(f"Barrido que muestra la expresión en el orden correcto: {barrido_correcto}")
