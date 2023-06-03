"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * from Persona WHERE idPersona = ?''', (id_persona,))

    fila = cursor.fetchone()

    if(fila is not None):
        print("Se encontró el registro")
        print(fila)
        print(fila == (1, 'juan carlos perez', "1988-04-16", 32165497, 181))
        cursor.close()
        conn.close()
        return fila
        
    else:
        print("No se encontró el registro")
        cursor.close()
        conn.close()
        return False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', "1988-05-15", 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
