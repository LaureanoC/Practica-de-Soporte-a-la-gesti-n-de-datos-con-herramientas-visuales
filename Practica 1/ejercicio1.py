def maximo_basico(a: float, b: float) -> float:
    if(a>b):
        return a
    if(b>a):
        return b
    
print('Ejercicio a')
assert maximo_basico(10,5) == 10
assert maximo_basico(9,18) == 18
# assert maximo_basico(0,1) == 0

#############################

print('Ejercicio b')

def maximo_libreria(a: float, b: float) -> float:
    return max(a,b)


assert maximo_libreria(10,5) == 10
assert maximo_libreria(9,18) == 18

############################

def maximo_ternario(a: float, b: float) -> float:
 return a if a>b else b

print('Ejerciio c')

assert maximo_ternario(10,5) == 10
assert maximo_ternario(9,18) == 18

