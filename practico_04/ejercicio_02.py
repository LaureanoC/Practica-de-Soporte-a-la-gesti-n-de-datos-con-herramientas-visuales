"""Base de Datos SQL - Alta"""

import datetime
from ejercicio_01 import reset_tabla
import sqlite3


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""

    # Convertimos la fecha de nacimiento
    fecha_str = nacimiento.strftime('%Y-%m-%d')

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Persona(nombre, fechaNacimiento, dni, altura) 
                    VALUES(?,?,?,?)''', (nombre, fecha_str, dni, altura))
    
    conn.commit()
    ultimoId = cursor.lastrowid
    conn.close()
    print("Se añadió un registro con id: " + str(ultimoId))

    #Puedes poner un punto de interrupción y utilizar el debbuger para ver los registros insertados en example.db

    return ultimoId



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
