"""Clousures, Generadores, Generadores Delegados

Esta guia muestra uno de los patrones avanzados de programación para evitar
el uso de variables globales. El método descripto se llama closure y consiste
en vincular una función con datos que persistan luego de la ejecución, sin
recurrir a variables globales. Esto se hace mediante la declaración de una
función dentro de otra y permite comportamiento que sería imposible lograr de
otra manera.
"""


from typing import Iterator, Callable


def generar_pares_clousure(initial: int = 0) -> Callable[[], int]:
    """Toma un número inicial y devuelve una función que cada vez que es
    invocada devuelve el número par siguiente al devuelto la última vez que
    fue invocada.

    Restricciones:
        - Usar closures
        - Usar el modificador nonlocal
    """
    def pares_clousure():
        nonlocal initial
        initial += 2     #Modifico el parametro para que luego sea 2, y luego 4
        return initial - 2 # retorno el valor previo a la modificación
    return pares_clousure


# NO MODIFICAR - INICIO
generador_pares = generar_pares_clousure(0)
assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4
# NO MODIFICAR - FIN

###############################################################################


"""Este tipo de comportamiento es conocido com semi-corutina, las semi-corutinas
en Python son llamadas funciones generadoras y se caracterizan por utilizar el
yield en lugar del return.
"""


def generar_pares_generator(initial: int = 0) -> Iterator[int]:
    """Re-Escribir utilizando Generadores
    Referencia: https://docs.python.org/3/howto/functional.html?highlight=generator#generators
    """
    while True:
        yield initial
        initial+=2
    

# NO MODIFICAR - INICIO
generador_pares = generar_pares_generator()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
# NO MODIFICAR - FIN