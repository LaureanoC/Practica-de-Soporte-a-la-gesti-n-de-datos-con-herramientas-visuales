"""Tuple, Enumerate, Zip, Args.


Contexto: Se tiene un programa que lee diferentes listas de una tabla en una
base de datos y se quieren combinar estas listas para que luego puedan crearse
los objetos de la capa de negocio.
"""


from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    """Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción: Resolver utilizando un bucle for.
    """
    lista = []
    for i in range(3):
        lista.append((nombres[i], precios[i]))
    return tuple(lista)


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    """Re-Escribir utilizando enumerate y agregando un nuevo componente.
    Referencia: https://docs.python.org/3/library/functions.html#enumerate
    """
    lista = [] # de duplas
    for i, x in enumerate(nombres):           # i = indice   x = valor
        lista.append((x, precios[i], ids[i]))   # x = nombreActual, precios [i], ids = [i]
    return tuple(lista)

print(combinar_enumerate(nombre_articulos,precio_articulos,id_articulos))

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN

###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:
    """Re-Escribir utilizando zip.
    Referencia: https://docs.python.org/3/library/functions.html#zip
    """
    lista = []
    for nombre, precio, id in zip(nombres,precios,ids):   # el primero con el primero y así
        lista.append((nombre, precio, id))
    print(tuple(lista))
    return tuple(lista)


# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]
categoria_articulos = ["hogar", "libreria", "perfumeria"]
importado_articulos = [True, False, True]


def combinar_zip_args(*args) -> Tuple[Any]:
    """Re-Escribir utilizando zip y una cantidad arbitraria de componentes.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
    """
    lista = []
    for args in zip(*args):   
        lista.append((args))
    print(tuple(lista))
    return tuple(lista)



# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852, "hogar", True),
    ("lámpara", 16.42, 1459, "libreria", False),
    ("shampoo", 5.2, 3578, "perfumeria", True),
)

componentes = [
    nombre_articulos,
    precio_articulos,
    id_articulos,
    categoria_articulos,
    importado_articulos,
]

assert combinar_zip_args(*componentes) == respuesta
# NO MODIFICAR - FIN