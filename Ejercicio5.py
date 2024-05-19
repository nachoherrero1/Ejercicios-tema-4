class Nodo:
  """
  Clase para representar un nodo en un árbol binario.

  Atributos:
    nombre: El nombre del superhéroe o villano.
    es_heroe: Un valor booleano que indica si es un héroe (True) o un villano (False).
    izquierda: Enlace al nodo hijo izquierdo.
    derecha: Enlace al nodo hijo derecho.
  """

  def __init__(self, nombre, es_heroe):
    self.nombre = nombre
    self.es_heroe = es_heroe
    self.izquierda = None
    self.derecha = None

def insertar(nodo, nombre, es_heroe):
  """
  Inserta un nuevo nodo en el árbol binario.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
    nombre: El nombre del superhéroe o villano a insertar.
    es_heroe: Un valor booleano que indica si es un héroe (True) o un villano (False).
  """
  if nombre < nodo.nombre:
    if nodo.izquierda is None:
      nodo.izquierda = Nodo(nombre, es_heroe)
    else:
      insertar(nodo.izquierda, nombre, es_heroe)
  else:
    if nodo.derecha is None:
      nodo.derecha = Nodo(nombre, es_heroe)
    else:
      insertar(nodo.derecha, nombre, es_heroe)

def listar_villanos_alfabeticamente(nodo):
  """
  Lista los villanos ordenados alfabéticamente.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
  """
  if nodo is None:
    return

  if not nodo.es_heroe:
    print(nodo.nombre)

  listar_villanos_alfabeticamente(nodo.izquierda)
  listar_villanos_alfabeticamente(nodo.derecha)

def mostrar_superheroes_con_c(nodo):
  """
  Muestra todos los superhéroes que empiezan con C.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
  """
  if nodo is None:
    return

  if nodo.nombre.startswith('C') and nodo.es_heroe:
    print(nodo.nombre)

  mostrar_superheroes_con_c(nodo.izquierda)
  mostrar_superheroes_con_c(nodo.derecha)

def contar_superheroes(nodo):
  """
  Cuenta la cantidad de superhéroes en el árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
  """
  if nodo is None:
    return 0

  conteo = 0
  if nodo.es_heroe:
    conteo += 1

  conteo += contar_superheroes(nodo.izquierda)
  conteo += contar_superheroes(nodo.derecha)

  return conteo
def buscar_nodo_por_proximidad(nodo, nombre_objetivo, distancia_maxima):
  """
  Busca un nodo en el árbol por proximidad al nombre objetivo.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
    nombre_objetivo: El nombre del superhéroe o villano a buscar.
    distancia_maxima: La distancia máxima permitida para considerar un nodo como proximidad.

  Retorno:
    El nodo encontrado con la menor distancia al nombre objetivo, o None si no se encuentra dentro de la distancia máxima.
  """
  if nodo is None:
    return None

  distancia_actual = abs(len(nombre_objetivo) - len(nodo.nombre))
  nodo_cercano = None

  if distancia_actual <= distancia_maxima:
    nodo_cercano = nodo

  nodo_izquierdo_cercano = buscar_nodo_por_proximidad(nodo.izquierda, nombre_objetivo, distancia_maxima)
  if nodo_izquierdo_cercano is not None and \
      abs(len(nombre_objetivo) - len(nodo_izquierdo_cercano.nombre)) < distancia_actual:
    nodo_cercano = nodo_izquierdo_cercano

  nodo_derecho_cercano = buscar_nodo_por_proximidad(nodo.derecha, nombre_objetivo, distancia_maxima)
  if nodo_derecho_cercano is not None and \
      abs(len(nombre_objetivo) - len(nodo_derecho_cercano.nombre)) < distancia_actual:
    nodo_cercano = nodo_derecho_cercano

  return nodo_cercano

def corregir_nombre_doctor_strange(nodo):
  """
  Busca y corrige el nombre de Doctor Strange en el árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
  """
  if nodo is None:
    return

  if nodo.nombre == "Doctor Strange (mal cargado)":
    nodo.nombre = "Doctor Strange"
    print(f"Nombre de Doctor Strange corregido a: {nodo.nombre}")
  else:
    corregir_nombre_doctor_strange(nodo.izquierda)
    corregir_nombre_doctor_strange(nodo.derecha)

def listar_superheroes_descendente(nodo):
  """
  Lista los superhéroes ordenados de manera descendente.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
  """
  if nodo is None:
    return

  listar_superheroes_descendente(nodo.derecha)
  if nodo.es_heroe:
    print(nodo.nombre)
  listar_superheroes_descendente(nodo.izquierda)

def crear_bosque_heroes_villanos(nodo):
  """
  Crea dos árboles (bosque) a partir del árbol original, uno para héroes y otro para villanos.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol original.

  Retorno:
    Una tupla que contiene dos árboles: el árbol de héroes y el árbol de villanos.
  """
  arbol_heroes = None
  arbol_villanos = None

  if nodo is None:
    return arbol_heroes, arbol_villanos

  if nodo.es_heroe:
    arbol_heroes = Nodo(nodo.nombre, nodo.es_heroe)
    arbol_heroes.izquierda, arbol_heroes.derecha = crear_bosque_heroes_villanos(nodo.izquierda)
    arbol_heroes.derecha = crear_bosque_heroes_villanos(nodo.derecha)
  else:
    arbol_villanos = Nodo(nodo.nombre, nodo.es_heroe)
    arbol_villanos.izquierda, arbol_villanos.derecha = crear_bosque_heroes_villanos(nodo.izquierda)
    arbol_villanos.derecha = crear_bosque_heroes_villanos(nodo.derecha)

  return arbol_heroes, arbol_villanos

def contar_nodos_arbol(nodo):
  """
  Cuenta la cantidad de nodos en un árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.

  Retorno:
    La cantidad de nodos en el árbol.
  """
  if nodo is None:
    return 0

  return 1 + contar_nodos_arbol(nodo.izquierda) + contar_nodos_arbol(nodo.derecha)
def barrido_ordenado_alfabetico(nodo):
  """
  Realiza un barrido ordenado alfabéticamente de un árbol.

  Argumentos:
    nodo: El nodo actual del recorrido en el árbol.
  """
  if nodo is None:
    return

  barrido_ordenado_alfabetico(nodo.izquierda)
  print(nodo.nombre)
  barrido_ordenado_alfabetico(nodo.derecha)

# Ejemplo de uso
heroes_villanos = [
  ("Iron Man", True),
  ("Capitán América", True),
  ("Thor", True),
  ("Hulk", True),
  ("Viuda Negra", True),
  ("Ojo de Halcón", True),
  ("Loki", False),
  ("Thanos", False),
  ("Hela", False),
  ("Mystique", False),
  ("Magneto", False),
  ("Doctor Strange (mal cargado)", True),
]

raiz = None
for nombre, es_heroe in heroes_villanos:
  insertar(raiz, nombre, es_heroe)

print("\nVillanos ordenados alfabéticamente:")
listar_villanos_alfabeticamente(raiz)

print("\nSuperhéroes que empiezan con C:")
mostrar_superheroes_con_c(raiz)

print("\nCantidad de superhéroes:", contar_superheroes(raiz))

print("\nCorrección del nombre de Doctor Strange:")
corregir_nombre_doctor_strange(raiz)

print("\nSuperhéroes ordenados de manera descendente:")
listar_superheroes_descendente(raiz)

print("\nBosque de héroes y villanos:")
arbol_heroes, arbol_villanos = crear_bosque_heroes_villanos(raiz)

print("\nCantidad de nodos en el árbol de héroes:", contar_nodos_arbol(arbol_heroes))
print("Barrido ordenado alfabéticamente del árbol de héroes:")
barrido_ordenado_alfabetico(arbol_heroes)

print("\nCantidad de nodos en el árbol de villanos:", contar_nodos_arbol(arbol_villanos))
print("Barrido ordenado alfabéticamente del árbol de villanos:")
barrido_ordenado_alfabetico(arbol_villanos)
