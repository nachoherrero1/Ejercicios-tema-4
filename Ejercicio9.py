class Nodo:
  def __init__(self, simbolo=None, frecuencia=0, izq=None, der=None):
    self.simbolo = simbolo
    self.frecuencia = frecuencia
    self.izq = izq
    self.der = der

def crear_arbol_huffman(simbolos, frecuencias):
  """
  Crea un árbol de Huffman a partir de una lista de símbolos y sus frecuencias.

  Argumentos:
    simbolos: Lista de símbolos.
    frecuencias: Lista de frecuencias correspondientes a cada símbolo.

  Retorno:
    El nodo raíz del árbol de Huffman.
  """
  if len(simbolos) == 1:
    return Nodo(simbolos[0], frecuencias[0])

  simbolos_frecuencias = list(zip(simbolos, frecuencias))
  simbolos_frecuencias.sort(key=lambda x: x[1])

  simbolo_izq, frecuencia_izq = simbolos_frecuencias.pop(0)
  simbolo_der, frecuencia_der = simbolos_frecuencias.pop(0)

  nodo_izq = crear_arbol_huffman([simbolo_izq], [frecuencia_izq])
  nodo_der = crear_arbol_huffman([simbolo_der], [frecuencia_der])

  nodo_padre = Nodo(None, frecuencia_izq + frecuencia_der)
  nodo_padre.izq = nodo_izq
  nodo_padre.der = nodo_der

  return nodo_padre

def codificar_mensaje(mensaje, tabla_codigos):
  """
  Codifica un mensaje utilizando la tabla de códigos de Huffman.

  Argumentos:
    mensaje: El mensaje a codificar.
    tabla_codigos: Diccionario que contiene la codificación binaria para cada símbolo.

  Retorno:
    La cadena binaria que representa el mensaje codificado.
  """
  codigo_binario = ""
  for simbolo in mensaje:
    codigo_binario += tabla_codigos[simbolo]

  return codigo_binario

def decodificar_mensaje(codigo_binario, arbol):
  """
  Decodifica un mensaje codificado con Huffman.

  Argumentos:
    codigo_binario: La cadena binaria que representa el mensaje codificado.
    arbol: El árbol de Huffman utilizado para la codificación.

  Retorno:
    El mensaje original decodificado.
  """
  mensaje_decodificado = ""
  nodo_actual = arbol

  for bit in codigo_binario:
    if bit == "0":
      nodo_actual = nodo_actual.izq
    else:
      nodo_actual = nodo_actual.der

    if nodo_actual.simbolo is not None:
      mensaje_decodificado += nodo_actual.simbolo
      nodo_actual = arbol  # Reiniciar la búsqueda en el árbol

  return mensaje_decodificado

def crear_tabla_codigos(nodo, codigo="", tabla_codigos={}):
  """
  Crea una tabla de códigos de Huffman recursivamente.

  Argumentos:
    nodo: El nodo actual del árbol.
    codigo: El código binario acumulado hasta el momento.
    tabla_codigos: Diccionario que contendrá la tabla de códigos.

  Retorno:
    La tabla de códigos de Huffman.
  """
  if nodo.simbolo is not None:
    tabla_codigos[nodo.simbolo] = codigo
    return tabla_codigos

  tabla_codigos = crear_tabla_codigos(nodo.izq, codigo + "0", tabla_codigos.copy())
  tabla_codigos = crear_tabla_codigos(nodo.der, codigo + "1", tabla_codigos)
  return tabla_codigos

# Símbolos y frecuencias
simbolos = ["A", "F", "1", "3", "0", "M", "T"]
frecuencias = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]

# Crear árbol de Huffman
arbol_huffman = crear_arbol_huffman(simbolos, frecuencias)

# Crear tabla de códigos
tabla_codigos = crear_tabla_codigos(arbol_huffman)
# Ejemplo de uso (continuación)

mensaje_original = "A1F30M"
print(f"Mensaje original: {mensaje_original}")

# Codificar mensaje
codigo_binario = codificar_mensaje(mensaje_original, tabla_codigos)
print(f"Código binario: {codigo_binario}")

# Decodificar mensaje
mensaje_decodificado = decodificar_mensaje(codigo_binario, arbol_huffman)
print(f"Mensaje decodificado: {mensaje_decodificado}")

# Comprobar si el mensaje original y el decodificado son iguales
if mensaje_original == mensaje_decodificado:
  print("¡El mensaje se ha codificado y decodificado correctamente!")
else:
  print("¡Ha ocurrido un error en la codificación o decodificación del mensaje!")
