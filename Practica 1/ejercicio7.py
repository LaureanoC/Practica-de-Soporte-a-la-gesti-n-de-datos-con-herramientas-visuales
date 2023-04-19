"""Slicing."""


from functools import reduce
from math import ceil

def es_palindromo(palabra: str) -> bool:
    invertida = palabra[::-1]
    print(invertida)

    if(invertida == palabra):
        return True
    else:
        return False

 #palabras_reves = palabra[::-1]
 #return palabras_reves

# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


def es_palindromo_lambda(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.
    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
   
    if(palabra == ""):
        return True
    else:
        print(reduce(lambda x,y: y + x, palabra)) ## No es con slices pero funciona 
        return reduce(lambda x,y: y + x, palabra) == palabra



# NO MODIFICAR - INICIO
assert not es_palindromo_lambda("amor")
assert es_palindromo_lambda("radar")
assert es_palindromo_lambda("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.
    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """


    if(len(palabra) % 2 == 0):
        
        print(palabra)
        print(palabra[0:2])
        print(int(len(palabra)/2)) ## Sino me lo tomaba como 2.0 float
        print(palabra[0:int(len(palabra)/2)])
        return palabra[0:int(len(palabra)/2)]
    else:

        print(len(palabra)) # 5
        print(len(palabra)/2)   # 2.5
        print(ceil(len(palabra)/2))  #3
        print(palabra[0:ceil(len(palabra)/2)]) ## Hel

        return palabra[0:ceil(len(palabra)/2)]

   
# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN