import random

class NodoAVL:
  """
  Clase para representar un nodo en un árbol binario AVL.

  Atributos:
    dato: El valor almacenado en el nodo.
    izquierda: Enlace al nodo hijo izquierdo.
    derecha: Enlace al nodo hijo derecho.
    altura: La altura del subárbol que tiene este nodo como raíz.
    balance: El factor de balance del nodo.
  """

  def __init__(self, dato):
    self.dato = dato
    self.izquierda = None
    self.derecha = None
    self.altura = 1
    self.balance = 0

class AVL:
  """
  Clase para representar un árbol binario AVL.

  Atributos:
    raiz: El nodo raíz del árbol.
  """

  def __init__(self):
    self.raiz = None

  def insertar(self, dato):
    """
    Inserta un nuevo dato en el árbol AVL.

    Argumentos:
      dato: El dato a insertar.

    Retorno:
      None
    """
    self.raiz = self._insertar(self.raiz, dato)

  def _insertar(self, nodo, dato):
    """
    Función recursiva para insertar un dato en el árbol AVL.

    Argumentos:
      nodo: El nodo actual del recorrido.
      dato: El dato a insertar.

    Retorno:
      El nodo actualizado después de la inserción.
    """
    if nodo is None:
      return NodoAVL(dato)

    if dato < nodo.dato:
      nodo.izquierda = self._insertar(nodo.izquierda, dato)
    else:
      nodo.derecha = self._insertar(nodo.izquierda, dato)

    nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))
    nodo.balance = self._get_balance(nodo)

    return self._balancear(nodo)

  def _get_altura(self, nodo):
    """
    Obtiene la altura de un nodo.

    Argumentos:
      nodo: El nodo del que se quiere obtener la altura.

    Retorno:
      La altura del nodo, 0 si es None.
    """
    if nodo is None:
      return 0
    return nodo.altura

  def _get_balance(self, nodo):
    """
    Obtiene el factor de balance de un nodo.

    Argumentos:
      nodo: El nodo del que se quiere obtener el balance.

    Retorno:
      El factor de balance del nodo.
    """
    if nodo is None:
      return 0
    return self._get_altura(nodo.izquierda) - self._get_altura(nodo.derecha)

  def _rotacion_derecha(self, nodo):
    """
    Realiza una rotación derecha en el nodo especificado.

    Argumentos:
      nodo: El nodo en el que se debe realizar la rotación.

    Retorno:
      El nodo raíz actualizado después de la rotación.
    """
    hijo_izquierdo = nodo.izquierda
    nodo.izquierda = hijo_izquierdo.derecha
    hijo_izquierdo.derecha = nodo

    nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))
    hijo_izquierdo.altura = 1 + max(self._get_altura(hijo_izquierdo.izquierda), self._get_altura(hijo_izquierdo.derecha))

    return hijo_izquierdo

  def _rotacion_izquierda(self, nodo):
    """
    Realiza una rotación izquierda en el nodo especificado.

    Argumentos:
      nodo: El nodo en el que se debe realizar la rotación.

    Retorno:
      El nodo raíz actualizado después de la rotación.
    """
    hijo_derecho = nodo.derecha
    nodo.derecha = hijo_derecho.izquierda
    hijo_derecho.izquierda = nodo

    nodo.altura = 1 + max(self._get_altura(nodo.izquierda), self._get_altura(nodo.derecha))
    hijo_derecho.altura = 1 + max(self._get_altura(hijo_derecho.izquierda), self._get_altura(hijo_derecho.derecha))

    return hijo_derecho

    def _balancear(self, nodo):

        balance = self._get_balance(nodo)

        # Caso de desbalance a la izquierda con hijo izquierdo más alto
        if balance > 1 and self._get_balance(nodo.izquierda) >= 0:
            return self._rotacion_derecha(nodo)

        # Caso de desbalance a la izquierda con hijo derecho más alto
        if balance > 1 and self._get_balance(nodo.izquierda) < 0:
            nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
            return self._rotacion_derecha(nodo)

    # Caso de desbalance a la derecha con hijo derecho más alto
    if balance < -1 and self._get_balance(nodo.derecha) <= 0:
      return self._rotacion_izquierda(nodo)

    # Caso de desbalance a la derecha con hijo izquierdo más alto
    if balance < -1 and self._get_balance(nodo.derecha) > 0:
      nodo.derecha = self._rotacion_derecha(nodo.derecha)
      return self._rotacion_izquierda(nodo)

    return nodo

  def preorden(self):
    """
    Recorre el árbol en preorden.

    Retorno:
      Una lista con los datos del árbol en preorden.
    """
    valores = []
    self._preorden(self.raiz, valores)
    return valores

  def _preorden(self, nodo, valores):
    """
    Función recursiva para recorrer el árbol en preorden.

    Argumentos:
      nodo: El nodo actual del recorrido.
      valores: La lista para almacenar los datos del recorrido.

    Retorno:
      None
    """
    if nodo is None:
      return

    valores.append(nodo.dato)
    self._preorden(nodo.izquierda, valores)
    self._preorden(nodo.derecha, valores)

  def inorden(self):
    """
    Recorre el árbol en inorden.

    Retorno:
      Una lista con los datos del árbol en inorden.
    """
    valores = []
    self._inorden(self.raiz, valores)
    return valores

  def _inorden(self, nodo, valores):
    """
    Función recursiva para recorrer el árbol en inorden.

    Argumentos:
      nodo: El nodo actual del recorrido.
      valores: La lista para almacenar los datos del recorrido.

    Retorno:
      None
    """
    if nodo is None:
      return

    self._inorden(nodo.izquierda, valores)
    valores.append(nodo.dato)
    self._inorden(nodo.derecha, valores)

  def postorden(self):
    """
    Recorre el árbol en postorden.

    Retorno:
      Una lista con los datos del árbol en postorden.
    """
    valores = []
    self._postorden(self.raiz, valores)
    return valores

  def _postorden(self, nodo, valores):
    """
    Función recursiva para recorrer el árbol en postorden.

    Argumentos:
      nodo: El nodo actual del recorrido.
      valores: La lista para almacenar los datos del recorrido.

    Retorno:
      None
    """
    if nodo is None:
      return

    self._postorden(nodo.izquierda, valores)
    self._postorden(nodo.derecha, valores)
    valores.append(nodo.dato)

  def por_nivel(self):
    """
    Recorre el árbol por nivel utilizando una cola.

    Retorno:
      Una lista con los datos del árbol por nivel.
    """
    valores = []
    cola = []

    if self.raiz is not None:
      cola.append(self.raiz)

    while cola:
      nodo_actual = cola.pop(0)
      valores.append(nodo_actual.dato)

      if nodo_actual.izquierda is not None:
        cola.append(nodo_actual.izquierda)
      if nodo_actual.derecha is not None:
        cola.append(nodo_actual.derecha)

  def buscar(self, dato):
    """
    Busca un dato en el árbol AVL.

    Argumentos:
      dato: El dato a buscar.

    Retorno:
      True si el dato está en el árbol, False en caso contrario.
    """
    return self._buscar(self.raiz, dato)

  def _buscar(self, nodo, dato):
    """
    Función recursiva para buscar un dato en el árbol AVL.

    Argumentos:
      nodo: El nodo actual del recorrido.
      dato: El dato a buscar.

    Retorno:
      True si el dato está en el árbol, False en caso contrario.
    """
    if nodo is None:
      return False

    if dato == nodo.dato:
      return True

    if dato < nodo.dato:
      return self._buscar(nodo.izquierda, dato)
    else:
      return self._buscar(nodo.derecha, dato)

  def eliminar(self, dato):
    """
    Elimina un dato del árbol AVL.

    Argumentos:
      dato: El dato a eliminar.

    Retorno:
      None
    """
    self.raiz = self._eliminar(self.raiz, dato)

  def _eliminar(self, nodo, dato):
    """
    Función recursiva para eliminar un dato del árbol AVL.

    Argumentos:
      nodo: El nodo actual del recorrido.
      dato: El dato a eliminar.

    Retorno:
      El nodo actualizado después de la eliminación, si es necesario.
    """
    if nodo is None:
      return None

    if dato < nodo.dato:
      nodo.izquierda = self._eliminar(nodo.izquierda, dato)
    elif dato > nodo.dato:
      nodo.derecha = self._eliminar(nodo.derecha, dato)
    else:
      # Se encontró el nodo a eliminar
      nodo_minimo_derecha = self._minimo_derecha(nodo.derecha)

      if nodo_minimo_derecha is None:
        # El nodo a eliminar no tiene hijo derecho
        nodo_izquierdo = nodo.izquierda
        nodo = None
      else:
        # El nodo a eliminar tiene hijo derecho
        nodo.dato = nodo_minimo_derecha.dato
        nodo.derecha = self._eliminar(nodo.derecha, nodo_minimo_derecha.dato)

      nodo = self._balancear(nodo)

    return nodo

  def _minimo_derecha(self, nodo):
    """
    Obtiene el nodo con el valor mínimo del subárbol derecho.

    Argumentos:
      nodo: El nodo raíz del subárbol derecho.

    Retorno:
      El nodo con el valor mínimo del subárbol derecho, o None si está vacío.
    """
    if nodo is None:
      return None

    while nodo.izquierda is not None:
      nodo = nodo.izquierda

    return nodo

  def altura_subarbol_izquierdo(self):
    """
    Obtiene la altura del subárbol izquierdo del árbol.

    Retorno:
      La altura del subárbol izquierdo, 0 si el árbol está vacío.
    """
    if self.raiz is None:
      return 0
    return self._get_altura(self.raiz.izquierda)

  def altura_subarbol_derecho(self):
    """
    Obtiene la altura del subárbol derecho del árbol.

    Retorno:
      La altura del subárbol derecho, 0 si el árbol está vacío.
    """
    if self.raiz is None:
      return 0
    return self._get_altura(self.raiz.derecha)

  def contar_ocurrencias(self, dato):
    """
    Cuenta la cantidad de ocurrencias de un dato en el árbol.

    Argumentos:
      dato: El dato a contar.

    Retorno:
      La cantidad de ocurrencias del dato en el árbol.
    """
    return self._contar_ocurrencias(self.raiz, dato)

  def _contar_ocurrencias(self, nodo, dato):
    """
    Función recursiva para contar las ocurrencias de un dato en el árbol.

    Argumentos:
      nodo: El nodo actual del recorrido.
      dato: El dato a contar.

    Retorno:
      La cantidad de ocurrencias del dato en el subárbol enraizado en nodo.
    """
    if nodo is None:
      
      return 0

    ocurrencias = 0
    if dato == nodo.dato:
      ocurrencias += 1

    ocurrencias_izquierda = self._contar_ocurrencias(nodo.izquierda, dato)
    ocurrencias_derecha = self._contar_ocurrencias(nodo.derecha, dato)

    return ocurrencias + ocurrencias_izquierda + ocurrencias_derecha

  def contar_pares_impares(self):
    """
    Cuenta la cantidad de números pares e impares en el árbol.

    Retorno:
      Un diccionario con las claves 'pares' e 'impares' y sus valores correspondientes a la cantidad de números pares e impares, respectivamente.
    """
    pares, impares = self._contar_pares_impares(self.raiz)
    return {'pares': pares, 'impares': impares}

  def _contar_pares_impares(self, nodo):
    """
    Función recursiva para contar la cantidad de números pares e impares en el árbol.

    Argumentos:
      nodo: El nodo actual del recorrido.

    Retorno:
      Una tupla con la cantidad de números pares e impares en el subárbol enraizado en nodo.
    """
    if nodo is None:
      return 0, 0

    pares_izquierda, impares_izquierda = self._contar_pares_impares(nodo.izquierda)
    pares_derecha, impares_derecha = self._contar_pares_impares(nodo.derecha)

    pares = pares_izquierda + pares_derecha
    impares = impares_izquierda + impares_derecha

    if nodo.dato % 2 == 0:
      pares += 1
    else:
      impares += 1

    return pares, impares

# Generación de datos aleatorios
datos = []
for i in range(1000):
  datos.append(random.randint(-1000, 1000))

# Creación del árbol AVL
arbol = AVL()
for dato in datos:
  arbol.insertar(dato)

# Realización de las actividades
print("Recorrido preorden:", arbol.preorden())
print("Recorrido inorden:", arbol.inorden())
print("Recorrido postorden:", arbol.postorden())
print("Recorrido por nivel:", arbol.por_nivel())

dato_a_buscar = random.choice(datos)
print(f"Dato {dato_a_buscar} encontrado en el árbol:", arbol.buscar(dato_a_buscar))

for i in range(3):
  dato_a_eliminar = random.choice(datos)
  arbol.eliminar(dato_a_eliminar)
  print(f"Dato {dato_a_eliminar} eliminado del árbol")

altura_izquierda = arbol.altura_subarbol_izquierdo()
altura_derecha = arbol.altura_subarbol_derecho()
print(f"Altura subárbol izquierdo: {altura_izquierda}")
print(f"Altura subárbol derecho: {altura_derecha}")

dato_a_contar = random.choice(datos)
ocurrencias = arbol.contar_ocurrencias(dato_a_contar)
print(f"Ocurrencias de {dato_a_contar}: {ocurrencias}")

pares_impares = arbol.contar_pares_impares()
print(f"Números pares: {pares_impares['pares']}")
print(f"Números impares: {pares_impares['impares']}")

