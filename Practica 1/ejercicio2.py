"""Toma 3 numeros y devuelve el max
restricion: utilizar unicamente tres ifs y comparaciones encadenadas

"""

def maximo_encadenado(a: float, b: float, c: float) -> float:
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>a and c>b):
        return c

print ('Ejercicio a')    

assert maximo_encadenado(1, 10, 5) == 10
assert maximo_encadenado(4, 9, 18) == 18
assert maximo_encadenado(24, 9, 18) == 24


##########################################################


def maximo_cuadruple(a: float, b: float, c: float, d: float) -> float:
    return max(a,b,c,d)

print ('Ejercicio b')  

assert maximo_cuadruple(1,10,5,-5) == 10
assert maximo_cuadruple(4, 9, 18, 6) == 18
assert maximo_cuadruple(24, 9, 18, 20) == 24
assert maximo_cuadruple(24, 9, 18, 30) == 30


#########################################################

def maximo_arbitrario(*args) -> float:
    return max(args)

print('Ejercicio c')

assert maximo_arbitrario(1,10,5,-5) == 10
assert maximo_arbitrario(4, 9, 18, 6) == 18
assert maximo_arbitrario(24, 9, 18, 20) == 24
assert maximo_arbitrario(24, 9, 18, 30) == 30


#######################################################

#Por lista

def maximo_recursivo_lista(lista) -> float:
    if (len(lista) == 1):
        return lista[0]
    else:
        return max(lista[0], maximo_recursivo_lista(lista[1:]))    

print('Ejercicio d por lista')
assert maximo_recursivo_lista([1,10,5,-5]) == 10
assert maximo_recursivo_lista([4, 9, 18, 6]) == 18
assert maximo_recursivo_lista([24, 9, 18, 20]) == 24
assert maximo_recursivo_lista([24, 9, 18, 30]) == 30


##################

def maximo_recursivo(*args) -> float:

    lista = args
    print(args)
    print
    if (len(args) == 1):
        return args[0]
    else:
        return max(args[0], maximo_recursivo(args))    


assert maximo_recursivo(1,10,5,-5) == 10
assert maximo_recursivo(4, 9, 18, 6) == 18
assert maximo_recursivo(24, 9, 18, 20) == 24
assert maximo_recursivo(24, 9, 18, 30) == 30



