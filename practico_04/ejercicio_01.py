"""Base de Datos SQL - Crear y Borrar Tablas"""
#  si no está instalado el paquete -> pip install pysqlite3 para python v3
# sino pip install sqlite3
import sqlite3 

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    #Creo una base de datos en memoria
    conn = sqlite3.connect("example.db")

    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS persona 
                            (idPersona INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nombre TEXT, 
                            fechaNacimiento DATE, 
                            dni INTEGER, 
                            altura INTEGER)''')
    
    #Guardo los cambios
    conn.commit()

    #Cierro la conexión

    conn.close()
    


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE persona")
    conn.commit()
    conn.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
