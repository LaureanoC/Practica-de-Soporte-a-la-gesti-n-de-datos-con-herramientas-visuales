"""Dataclasses"""


class Persona:
    """Clase con los siguientes miembros:

    Atributos de instancia:
    - nombre: str
    - edad: int
    - sexo (H hombre, M mujer): str
    - peso: float
    - altura: float

    Métodos:
    - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
    """

    def __init__(self, n, e, s, p, a):
        self.nombre = n
        self.edad = e
        self.sexo = s
        self.peso = p
        self.altura = a
    
    def es_mayor_edad(self):
        return self.edad >= 18



# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Persona:
    """Re-Escribir utilizando DataClasses"""    
    
#Con dataclase se definen comportamientos predefinidos como el __init__() __repr__()  __str__()

    nombre: str
    edad: int
    sexo: str
    peso: float
    altura: float

    def es_mayor_edad(self):
        return self.edad >= 18
    


# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN
