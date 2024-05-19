class Nodo:
  def __init__(self, nombre, tipo, hijos=[]):
    self.nombre = nombre
    self.tipo = tipo  # "directorio" o "archivo"
    self.hijos = hijos
def transformar_a_binario(nodo_nario):
  if not nodo_nario:
    return None

  nodo_binario = Nodo(nodo_nario.nombre, nodo_nario.tipo)

  # Si el nodo n-ario tiene un solo hijo, se convierte en el hijo izquierdo del nodo binario.
  if len(nodo_nario.hijos) == 1:
    nodo_binario.hijos.append(transformar_a_binario(nodo_nario.hijos[0]))
  else:
    # Si el nodo n-ario tiene más de un hijo, se convierten en subárboles binarios y se unen como hijos izquierdo y derecho del nodo binario.
    hijo_izquierdo = transformar_a_binario(nodo_nario.hijos[0])
    hijo_derecho = transformar_a_binario(nodo_nario.hijos[1:])

    nodo_binario.hijos.append(hijo_izquierdo)
    nodo_binario.hijos.append(hijo_derecho)

  return nodo_binario
def barrido_inorden(nodo):
  if not nodo:
    return

  barrido_inorden(nodo.hijos[0])
  print(f"{nodo.nombre} ({nodo.tipo})")
  barrido_inorden(nodo.hijos[1])
def listar_contenido_carpeta(nodo, carpeta):
  if not nodo:
    return

  if nodo.nombre == carpeta and nodo.tipo == "directorio":
    for hijo in nodo.hijos:
      print(f"{hijo.nombre} ({hijo.tipo})")
  else:
    listar_contenido_carpeta(nodo.hijos[0], carpeta)
    listar_contenido_carpeta(nodo.hijos[1], carpeta)
def contar_archivos_carpeta(nodo, carpeta):
  if not nodo:
    return 0

  contador = 0
  if nodo.nombre == carpeta and nodo.tipo == "directorio":
    for hijo in nodo.hijos:
      if hijo.tipo == "archivo":
        contador += 1
  else:
    contador += contar_archivos_carpeta(nodo.hijos[0], carpeta)
    contador += contar_archivos_carpeta(nodo.hijos[1], carpeta)

  return contador
raiz_binario = None  # Define the variable "raiz_binario" before using it

def mostrar_todos_archivos(nodo):
    if not nodo:
        return

    if nodo.tipo == "archivo":
        print(nodo.nombre)

    mostrar_todos_archivos(nodo.hijos[0])
    mostrar_todos_archivos(nodo.hijos[1])

raiz_binario = transformar_a_binario(raiz_binario)  # Assign a value to "raiz_binario"

print("\nBarrido inorden del árbol binario no balanceado:")
barrido_inorden(raiz_binario)

print("\nContenido de la carpeta /Imágenes:")
listar_contenido_carpeta(raiz_binario, "/Imágenes")

print("\nCantidad de archivos en la carpeta /documentos:")
cantidad_archivos = contar_archivos_carpeta(raiz_binario, "/documentos")
print(f"Cantidad de archivos: {cantidad_archivos}")

