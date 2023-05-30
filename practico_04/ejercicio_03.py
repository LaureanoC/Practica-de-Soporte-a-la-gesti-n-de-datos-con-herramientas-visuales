"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # cur.execute('insert into new_test (curent_dt) values (?)', (temp,))
    # The reason this happens is that (temp) is an integer but (temp,) is a tuple of length one containing temp.

    cursor.execute('''DELETE FROM persona WHERE idPersona = ?''', (id_persona,)) 

    if cursor.rowcount > 0:
        conn.commit()
        conn.close()
        print("Se borró el registro")
        return True
    else:
        
        conn.close()
        print("No se encontró ningun registro con el id " + str(id_persona))
        return False

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
