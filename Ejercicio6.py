class Nodo:
  def __init__(self, dato, izquierda=None, derecha=None):
    self.dato = dato
    self.izquierda = izquierda
    self.derecha = derecha

def insertar_arbol(arbol, dato, campo):
  if arbol is None:
    return Nodo(dato)

  if campo == "nombre":
    if dato.nombre < arbol.dato.nombre:
      arbol.izquierda = insertar_arbol(arbol.izquierda, dato, campo)
    else:
      arbol.derecha = insertar_arbol(arbol.derecha, dato, campo)
  elif campo == "ranking":
    if dato.ranking < arbol.dato.ranking:
      arbol.izquierda = insertar_arbol(arbol.izquierda, dato, campo)
    else:
      arbol.derecha = insertar_arbol(arbol.derecha, dato, campo)
  elif campo == "especie":
    if dato.especie < arbol.dato.especie:
      arbol.izquierda = insertar_arbol(arbol.izquierda, dato, campo)
    else:
      arbol.derecha = insertar_arbol(arbol.derecha, dato, campo)
  else:
    raise ValueError(f"Campo no válido: {campo}")

  return arbol

def barrido_inorden(arbol):
  if arbol is None:
    return

  barrido_inorden(arbol.izquierda)
  print(arbol.dato)
  barrido_inorden(arbol.derecha)

def barrido_por_nivel(arbol):
  if arbol is None:
    return

  cola = []
  cola.append(arbol)

  while cola:
    nodo_actual = cola.pop(0)
    print(nodo_actual.dato)

    if nodo_actual.izquierda is not None:
      cola.append(nodo_actual.izquierda)
    if nodo_actual.derecha is not None:
      cola.append(nodo_actual.derecha)

def mostrar_informacion_jedi(jedi):
  print(f"\nInformación de {jedi.nombre}:")
  print(f"Especie: {jedi.especie}")
  print(f"Año de nacimiento: {jedi.anio_nacimiento}")
  print(f"Color de sable de luz: {jedi.color_sable_luz}")
  print(f"Ranking: {jedi.ranking}")
  print(f"Maestros: {jedi.maestros}")

def mostrar_jedis_por_ranking(arbol, ranking):
  if arbol is None:
    return

  if arbol.dato.ranking == ranking:
    mostrar_informacion_jedi(arbol.dato)

  mostrar_jedis_por_ranking(arbol.izquierda, ranking)
  mostrar_jedis_por_ranking(arbol.derecha, ranking)

def listar_jedis_color_sable_verde(arbol):
  if arbol is None:
    return

  if arbol.dato.color_sable_luz == "verde":
    print(arbol.dato.nombre)

  listar_jedis_color_sable_verde(arbol.izquierda)
  listar_jedis_color_sable_verde(arbol.derecha)

def listar_jedis_con_maestros(arbol):
  if arbol is None:
    return

  for maestro in arbol.dato.maestros:
    if maestro in jedi:
      print(arbol.dato.nombre)

  listar_jedis_con_maestros(arbol.izquierda)
  listar_jedis_con_maestros(arbol.derecha)

def mostrar_jedis_especies(arbol, especies):
  if arbol is None:
    return

  if arbol.dato.especie in especies:
    print(arbol.dato.nombre)

  mostrar_jedis_especies(arbol.izquierda, especies)
  mostrar_jedis_especies(arbol.derecha, especies)

def listar_jedis_letra_a(arbol):
  if arbol is None:
    return

  if arbol.dato.nombre.startswith("A"):
    print(arbol.dato.nombre)

  listar_jedis_letra_a(arbol.izquierda)
  listar_jedis_letra_a(arbol.derecha)

def listar_jedis_con_guion(arbol):
  if arbol is None:
    return

  if "-" in arbol.dato.nombre:
    print(arbol.dato.nombre)

  listar_jedis_con_guion(arbol.izquierda)
  listar_jedis_con_guion(arbol.derecha)

# Suponiendo que "jedis" es una lista de objetos Jedi leídos del archivo

# Crear árboles de acceso
arbol_nombre = None
arbol_ranking = None
arbol_especie = None
jedi = []  # Define the variable "jedi" as an empty list

for jedi in jedi:
    arbol_nombre = insertar_arbol(arbol_nombre, jedi, "nombre")
    arbol_ranking = insertar_arbol(arbol_ranking, jedi, "ranking")
    arbol_especie = insertar_arbol(arbol_especie, jedi, "especie")

# Barridos inorden
print("\nBarrido inorden por nombre:")
barrido_inorden(arbol_nombre)

print("\nBarrido inorden por ranking:")
barrido_inorden(arbol_ranking)

# Barridos por nivel
print("\nBarrido por nivel por ranking:")
barrido_por_nivel(arbol_ranking)

print("\nBarrido por nivel por especie:")
barrido_por_nivel(arbol_especie)

# Mostrar información de Jedi específicos
mostrar_informacion_jedi(jedi["Yoda"])
mostrar_informacion_jedi(jedi["Luke Skywalker"])

# Mostrar Jedi por ranking
print("\nJedis con ranking 'Jedi Master':")
mostrar_jedis_por_ranking(arbol_ranking, "Jedi Master")

# Listar Jedi por color de sable de luz
print("\nJedis con sable de luz verde:")
listar_jedis_color_sable_verde(arbol_nombre)  # Se utiliza el árbol por nombre para este caso

# Listar Jedi con maestros en el archivo
print("\nJedis con maestros en el archivo:")
listar_jedis_con_maestros(arbol_nombre)  # Se utiliza el árbol por nombre para este caso

# Mostrar Jedi de especies específicas
print("\nJedis de especie 'Togruta' o 'Cerean':")
mostrar_jedis_especies(arbol_especie, ["Togruta", "Cerean"])

# Listar Jedi con letra A o guion
print("\nJedis que comienzan con la letra A:")
listar_jedis_letra_a(arbol_nombre)

print("\nJedis que contienen un '-' en su nombre:")
listar_jedis_con_guion(arbol_nombre)

