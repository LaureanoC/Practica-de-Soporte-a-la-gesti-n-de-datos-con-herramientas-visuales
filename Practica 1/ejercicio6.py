"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    letras = []
    numeros = []

    for item in lista:
        if(type(item) == str):
            letras.append(item) 
        if(type(item) == int):
            numeros.append(item)
            
    print(letras + numeros)
    return letras + numeros
            
# alternativa profe numeros =

# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN

###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    numeros = [num for num in lista if(type(num) == int)] ## Agrego num. Para cada num en la lista si el tipo es entero
    letras = [letra for letra in lista if(type(letra) == str)] ## Agrego num. Para cada num en la lista si el tipo es string
    print(letras + numeros)
    return letras + numeros 


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """

    ## sorted(iterable, /, *, key=None, reverse=False)
    print( sorted(lista, key= lambda item: (type(item) == str), reverse=True))
    print( sorted(lista, key= lambda item: (type(item) == int)))

    return sorted(lista, key= lambda item: (type(item) == int))


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """

    ## filter(function, iterable)

    print(list(filter((lambda item: (type(item) == int)), lista)))  ## Filtro solo los numeros enteros
    print(list(filter((lambda item: (type(item) == str)), lista)))  ## Filtro los str
    print(list(filter((lambda item: (type(item) == str)), lista)) + list(filter((lambda item: (type(item) == int)), lista))) ## Concateno la lista filtrada por str con la de int

    return list(filter((lambda item: (type(item) == str)), lista)) + list(filter((lambda item: (type(item) == int)), lista)) ## Retorno


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################






