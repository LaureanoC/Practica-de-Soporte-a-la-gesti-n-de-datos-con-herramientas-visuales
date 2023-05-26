"""Único return vs múltiples return."""

from typing import Union


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:

#Union permite que el tipo de una variable pueda adoptar en este caso un float o un string

    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".
    Restricciones:
        - Utilizar un único return.
        - No utilizar AND ni OR.
    """

    return a*b if multiplicar else ("Operación no válida" if b==0 else a/b)

     # Completar


# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN


###############################################################################


def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Re-Escribir utilizando tres returns."""
    if(multiplicar):
        return a*b
    if(not multiplicar and b != 0):
        return a/b
    if(not multiplicar and b == 0):
        return "Operación no válida"
        

# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN