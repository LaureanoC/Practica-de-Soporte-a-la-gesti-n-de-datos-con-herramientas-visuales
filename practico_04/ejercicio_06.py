"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE PersonaPeso(
    idPersona INTEGER,
    fecha DATE,
    peso INTEGER,
    PRIMARY KEY (idPersona, fecha)
    FOREIGN KEY (idPersona) REFERENCES Persona (idPersona)
    )''')

    conn.commit()
    conn.close()

    


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE PersonaPeso")


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
