"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene la clase Asesoria, encargada de gestionar
los servicios de asesoría especializada que ofrece Software FJ.
"""

# Importamos la clase abstracta Servicio.
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import (
    ErrorServicio,
    ServicioNoDisponible
)

# Importamos el gestor de registros.
from utilidades.gestor_logs import GestorLogs


# Clase Asesoria que hereda de Servicio.
class Asesoria(Servicio):

    # Constructor de la clase.
    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        especialidad,
        nombre_asesor,
        disponible=True
    ):

        # Inicializamos los atributos heredados.
        super().__init__(identificador, nombre, tarifa_base)

        # Guardamos la información de la asesoría.
        self._especialidad = especialidad
        self._nombre_asesor = nombre_asesor
        self._disponible = disponible

        # Validamos los datos de la asesoría.
        self.validar_datos()

        # Registramos la creación exitosa.
        GestorLogs.registrar_evento(
            f"Asesoría registrada correctamente: {self.identificador}"
        )

    # ---------------------------------
    # PROPIEDADES Y ENCAPSULAMIENTO
    # ---------------------------------

    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):

        anterior = self._especialidad
        self._especialidad = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._especialidad = anterior
            raise

    @property
    def nombre_asesor(self):
        return self._nombre_asesor

    @nombre_asesor.setter
    def nombre_asesor(self, valor):

        anterior = self._nombre_asesor
        self._nombre_asesor = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._nombre_asesor = anterior
            raise

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):

        anterior = self._disponible
        self._disponible = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._disponible = anterior
            raise

    # ---------------------------------
    # VALIDACIÓN DE PARÁMETROS
    # ---------------------------------

    def validar_parametros(self):

        try:

            if (
                not isinstance(self._especialidad, str)
                or not self._especialidad.strip()
            ):
                raise ErrorServicio(
                    "Debe especificar la especialidad de la asesoría."
                )

            if (
                not isinstance(self._nombre_asesor, str)
                or not self._nombre_asesor.strip()
            ):
                raise ErrorServicio(
                    "Debe especificar el nombre del asesor."
                )

            if not isinstance(self._disponible, bool):
                raise ErrorServicio(
                    "La disponibilidad debe ser verdadera o falsa."
                )

        except ErrorServicio as error:

            GestorLogs.registrar_error(
                f"Error al validar los parámetros de la asesoría "
                f"{self.identificador}",
                error
            )

            raise

        return True

    # ---------------------------------
    # VALIDACIÓN DE DATOS GENERALES
    # ---------------------------------

    def validar_datos(self):

        self.validar_parametros()

        return True

    # ---------------------------------
    # CÁLCULO DEL COSTO DE LA ASESORÍA
    # ---------------------------------

    def calcular_costo(self, duracion, descuento=0):

        try:

            # Comprobamos que la asesoría esté disponible.
            if not self.disponible:
                raise ServicioNoDisponible(
                    "La asesoría seleccionada no está disponible."
                )

            # Validamos duración y descuento.
            # La clase padre registra sus propios errores.
            self.validar_costo(duracion, descuento)

            # Calculamos el valor inicial.
            costo = self.tarifa_base * duracion

            # Aplicamos el descuento.
            costo_final = round(
                costo - (costo * descuento / 100),
                2
            )

            # Registramos el cálculo exitoso.
            GestorLogs.registrar_evento(
                f"Costo de asesoría calculado. "
                f"Identificador: {self.identificador}. "
                f"Duración: {duracion} horas. "
                f"Descuento: {descuento}%. "
                f"Total: ${costo_final:,.2f}"
            )

            return costo_final

        except ServicioNoDisponible as error:

            GestorLogs.registrar_error(
                f"No fue posible calcular el costo de la asesoría "
                f"{self.identificador}",
                error
            )

            raise

        except ErrorServicio:
            # La clase padre ya registra los errores de duración
            # y descuento, por eso no los registramos nuevamente.
            raise

    # ---------------------------------
    # DESCRIPCIÓN DEL SERVICIO
    # ---------------------------------

    def describir_servicio(self):

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Servicio: {self.nombre}\n"
            f"Especialidad: {self.especialidad}\n"
            f"Asesor: {self.nombre_asesor}\n"
            f"Tarifa por hora: ${self.tarifa_base:,.2f}\n"
            f"Estado: {estado}"
        )

    # ---------------------------------
    # MOSTRAR INFORMACIÓN DEL SERVICIO
    # ---------------------------------

    def mostrar_informacion(self):

        return (
            f"Identificador: {self.identificador}\n"
            f"{self.describir_servicio()}"
        )