"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio
from sqlalchemy.exc import IntegrityError

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        #Creo el motor de la base de datos
        engine = create_engine('sqlite:///example.db')

        #Creo todas las tablas definidas en Base, es decir socios
        Base.metadata.create_all(engine)
        # La función sessionmaker crea un generador de sesiones que permite interactuar con la base de datos
        Session = sessionmaker(bind=engine)
        #Esta línea crea una instancia de la clase Session
        self.session = Session()

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        socio = self.session.query(Socio).get(id_socio)

        if socio:
            return socio
        return None

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        # Sin el first lo que hace es asignar la query
        socio = self.session.query(Socio).filter_by(dni=dni_socio).first()
        print("El socio POR DNI ES")
        print(socio)
        if socio:
            return socio
        return None
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        return self.session.query(Socio).all()

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        try:
            self.session.query(Socio).delete()
            self.session.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar todos los datos: {str(e)}")
            self.session.rollback()
            return False

    def alta(self, socio: Socio) -> Socio:
      try:
          self.session.add(socio)
          self.session.commit()
          return socio
      except IntegrityError:
          self.session.rollback()
          print("El DNI del socio ya existe en la base de datos.")
          return None

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        # the column name and value to filter on en el filter by
        self.session.query(Socio).filter_by(id=id_socio).delete()
        self.session.commit()
        return True
        

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        self.session.merge(socio)
        self.session.commit()
        
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        return self.session.query(Socio).count()



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN