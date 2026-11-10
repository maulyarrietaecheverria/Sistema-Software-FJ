"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene la clase abstracta Entidad, que representa
la estructura general de los elementos principales del sistema.
"""

# Importamos las herramientas necesarias para trabajar con clases abstractas.
from abc import ABC, abstractmethod


# Clase abstracta que representa una entidad general del sistema.
class Entidad(ABC):

    # Constructor de la clase.
    def __init__(self, identificador):
        # Validamos que el identificador no esté vacío.
        if not identificador:
            raise ValueError("El identificador no puede estar vacío.")

        # Atributo privado para proteger la información.
        self.__identificador = identificador

    # Propiedad para consultar el identificador.
    @property
    def identificador(self):
        return self.__identificador

    # Método abstracto que obliga a las clases hijas
    # a implementar su propia descripción.
    @abstractmethod
    def mostrar_informacion(self):
        pass

    # Método abstracto que obliga a las clases hijas
    # a implementar sus propias validaciones.
    @abstractmethod
    def validar_datos(self):
        pass