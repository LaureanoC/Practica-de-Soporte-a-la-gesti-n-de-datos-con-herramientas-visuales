"""FOR, Sum, Reduce."""


def sumatoria_basico(n: int) -> int:
    """Devuelve la suma de los números de 1 a N.
    Restricción: Utilizar un bucle for.
    """
    resultado = 0
    for i in range(n):
        resultado = resultado + (i+1)
        print(resultado)
    return resultado # Completar


# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_sum(n: int) -> int:
    """Re-Escribir utilizando la función sum y sin usar bucles.
    Referencia: https://docs.python.org/3/library/functions.html#sum
    """
    #The range() function returns a sequence of numbers between the give range.
    # range(start, stop(antes), +suma de a tanto)
    lista = list(range(1,n+1))
    print(lista)
    resultado = sum(lista)
    print(resultado)
    return resultado


# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce


def sumatoria_reduce(n: int) -> int:
    """CHALLENGE OPCIONAL: Re-escribir utilizando reduce.
    Referencia: https://docs.python.org/3/library/functools.html#functools.reduce
    """
    listado = list(range(1,n+1))
    print(listado)
    return reduce(lambda x,y: x + y, listado)
    # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def sumatoria_gauss(n: int) -> int:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando suma de Gauss.
    Referencia: https://es.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    """
    print (n*(n+1)//2)
    return (n*(n+1)//2)

    


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_gauss(1) == 1
    assert sumatoria_gauss(100) == 5050
# NO MODIFICAR - FIN