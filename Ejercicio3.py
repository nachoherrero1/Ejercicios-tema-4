import re

class Nodo:
  """
  Clase para representar un nodo en un árbol n-ario.

  Atributos:
    dato: El texto del nodo.
    hijos: Una lista con los nodos hijos.
    pagina: La página donde se encuentra el tema (si se conoce).
  """

  def __init__(self, dato, pagina=None):
    self.dato = dato
    self.hijos = []
    self.pagina = pagina

def cargar_indice_desde_archivo(ruta_archivo):
  """
  Carga el índice del asignatura Ingeniería de Software de Ian Summerville desde un archivo de texto y lo transforma en un árbol n-ario.

  Argumentos:
    ruta_archivo: La ruta del archivo de texto.

  Retorno:
    El nodo raíz del árbol n-ario.
  """
  with open(ruta_archivo, 'r') as archivo:
    lineas = archivo.readlines()

  raiz = Nodo('')
  nivel_actual = 0
  padre_actual = raiz

  for linea in lineas:
    linea = linea.strip()
    if not linea:
      continue

    sangria = linea.count('\t')
    if sangria > nivel_actual:
      padre_actual = padre_actual.hijos[-1]

    nivel_actual = sangria

    # Extraer el texto del nodo y la página (si está presente)
    texto, pagina = re.match(r'^(.*?)(?:\s+\[p\. (\d+)\])?$', linea).groups()
    nodo = Nodo(texto, pagina if pagina else None)
    padre_actual.hijos.append(nodo)

  return raiz

def transformar_a_arbol_binario(nodo_nario):
  """
  Transforma un árbol n-ario en un árbol binario no balanceado mediante la transformada de Knuth.

  Argumentos:
    nodo_nario: El nodo raíz del árbol n-ario.

  Retorno:
    El nodo raíz del árbol binario no balanceado.
  """
  if len(nodo_nario.hijos) == 0:
    return nodo_nario

  if len(nodo_nario.hijos) == 1:
    return nodo_nario.hijos[0]

  izquierdo = transformar_a_arbol_binario(nodo_nario.hijos[0])
  derecho = transformar_a_arbol_binario(nodo_nario.hijos[-1])

  nuevo_nodo = Nodo(nodo_nario.dato)
  nuevo_nodo.izquierda = izquierdo
  nuevo_nodo.derecha = derecho

  return nuevo_nodo

def listar_indice_en_orden_original(nodo):
  """
  Lista el índice en su orden original (preorden).

  Argumentos:
    nodo: El nodo raíz del árbol.
  """
  if nodo is None:
    return

  print(nodo.dato)
  for hijo in nodo.hijos:
    listar_indice_en_orden_original(hijo)

def mostrar_parte_indice_diseno_software_tiempo_real(nodo):
  """
  Muestra la parte del índice correspondiente al subtitulo “Diseño de software de tiempo real”.

  Argumentos:
    nodo: El nodo raíz del árbol.
  """
  if nodo is None:
    return

  if nodo.dato.startswith('Diseño de software de tiempo real'):
    print(nodo.dato)
    for hijo in nodo.hijos:
      mostrar_parte_indice_diseno_software_tiempo_real(hijo)
  else:
    for hijo in nodo.hijos:
      mostrar_parte_indice_diseno_software_tiempo_real(hijo)

def contar_capitulos(nodo):
  """
  Cuenta la cantidad de capítulos en el índice.

  Argumentos:
    nodo: El nodo raíz del árbol.
  """
  if nodo is None:
    return 0

  capitulos = 0
  if nodo.dato.startswith('Capítulo'):
    capitulos += 1

  for hijo in nodo.hijos:
    capitulos += contar_capitulos(hijo)

  return capitulos

def buscar_temas_con_palabras(nodo, palabras):
  """
  Busca todos los temas que contengan las palabras especificadas.

  Argumentos:
    nodo: El nodo raíz del árbol.
    palabras: Una lista de palabras a buscar.
  """
  if nodo is None:
    return

  contiene_palabras = False
  for palabra in palabras:
    if palabra.lower() in nodo.dato.lower():
      contiene_palabras = True
      break

  if contiene_palabras:
    print(f"- {nodo.dato} (página {nodo.pagina})")

  for hijo in nodo.hijos:
    buscar_temas_con_palabras(hijo, palabras)

# Ejemplo de uso
ruta_archivo_indice = 'indice_ingenieria_software.txt'

arbol_nario = cargar_indice_desde_archivo(ruta_archivo_indice)
arbol_binario = transformar_a_arbol_binario(arbol_nario)

print("Índice en orden original:")
listar_indice_en_orden_original(arbol_binario)

print("\nParte del índice correspondiente al subtitulo 'Diseño de software de tiempo real':")
mostrar_parte_indice_diseno_software_tiempo_real(arbol_binario)

print("\nCantidad de capítulos:", contar_capitulos(arbol_binario))

print("\nTemas que contienen las palabras 'modelo' y 'métrica':")
buscar_temas_con_palabras(arbol_binario, ["modelo", "métrica"])

