"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene la clase abstracta Servicio.
Sirve como estructura general para los diferentes servicios
que ofrece la empresa Software FJ.
"""

# Importamos herramientas para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos la clase Entidad.
from modelos.entidad import Entidad

# Importamos la excepción personalizada.
from excepciones.errores_personalizados import ErrorServicio

# Importamos el gestor de registros.
from utilidades.gestor_logs import GestorLogs


# Clase abstracta Servicio que hereda de Entidad.
class Servicio(Entidad, ABC):

    # Constructor de la clase.
    def __init__(self, identificador, nombre, tarifa_base):

        try:
            # Inicializamos los atributos de la clase padre.
            super().__init__(identificador)

            # Validamos el nombre del servicio.
            if not isinstance(nombre, str) or not nombre.strip():
                raise ErrorServicio(
                    "El nombre del servicio es obligatorio."
                )

            # Validamos que la tarifa sea un número positivo.
            if (
                not isinstance(tarifa_base, (int, float))
                or isinstance(tarifa_base, bool)
                or tarifa_base <= 0
            ):
                raise ErrorServicio(
                    "La tarifa base debe ser un número positivo."
                )

            # Atributos protegidos de la clase.
            self._nombre = nombre.strip()
            self._tarifa_base = float(tarifa_base)

            # Registramos la creación del servicio.
            GestorLogs.registrar_evento(
                f"Servicio creado correctamente: {self._nombre}. "
                f"Identificador: {self.identificador}"
            )

        except ErrorServicio as error:

            # Registramos el error de creación.
            GestorLogs.registrar_error(
                "No fue posible crear el servicio",
                error
            )

            raise

    # Propiedad para consultar el nombre.
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para consultar la tarifa.
    @property
    def tarifa_base(self):
        return self._tarifa_base

    # Método abstracto para calcular el costo.
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass

    # Método abstracto para describir el servicio.
    @abstractmethod
    def describir_servicio(self):
        pass

    # Método abstracto para validar los parámetros.
    @abstractmethod
    def validar_parametros(self):
        pass

    # Método para validar duración y descuento.
    def validar_costo(self, duracion, descuento=0):

        try:
            if (
                not isinstance(duracion, (int, float))
                or isinstance(duracion, bool)
                or duracion <= 0
            ):
                raise ErrorServicio(
                    "La duración debe ser un número mayor que cero."
                )

            if (
                not isinstance(descuento, (int, float))
                or isinstance(descuento, bool)
                or not 0 <= descuento <= 100
            ):
                raise ErrorServicio(
                    "El descuento debe estar entre 0 y 100."
                )

            return True

        except ErrorServicio as error:

            # Registramos los errores de duración o descuento.
            GestorLogs.registrar_error(
                f"Error al validar el costo del servicio {self.nombre}",
                error
            )

            raise