"""
Clase para gestionar los servicios de reserva de salas.
Proyecto Software FJ - UNAD.
"""

from modelos.servicio import Servicio
from excepciones.errores_personalizados import (
    ErrorServicio,
    ServicioNoDisponible
)
from utilidades.gestor_logs import GestorLogs


class ReservaSalas(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        tipo_sala,
        capacidad,
        disponible=True
    ):
        # Inicializamos los atributos heredados de Servicio.
        super().__init__(identificador, nombre, tarifa_base)

        # Atributos propios de la sala.
        self._tipo_sala = tipo_sala
        self._capacidad = capacidad
        self._disponible = disponible

        # Validamos los datos de la sala.
        # Si ocurre un error, validar_parametros lo registra.
        self.validar_datos()

        # Registramos la sala cuando su creación es correcta.
        GestorLogs.registrar_evento(
            f"Sala registrada correctamente: {self.identificador}"
        )

    # -------------------------------
    # PROPIEDADES Y ENCAPSULAMIENTO
    # -------------------------------

    @property
    def tipo_sala(self):
        return self._tipo_sala

    @tipo_sala.setter
    def tipo_sala(self, valor):
        anterior = self._tipo_sala
        self._tipo_sala = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._tipo_sala = anterior
            raise

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        anterior = self._capacidad
        self._capacidad = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._capacidad = anterior
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

    # -------------------------------
    # VALIDACIÓN DE PARÁMETROS
    # -------------------------------

    def validar_parametros(self):
        try:
            if (
                not isinstance(self._tipo_sala, str)
                or not self._tipo_sala.strip()
            ):
                raise ErrorServicio(
                    "El tipo de sala debe ser un texto válido."
                )

            if (
                not isinstance(self._capacidad, int)
                or isinstance(self._capacidad, bool)
                or self._capacidad <= 0
            ):
                raise ErrorServicio(
                    "La capacidad debe ser un número entero positivo."
                )

            if not isinstance(self._disponible, bool):
                raise ErrorServicio(
                    "La disponibilidad debe ser verdadera o falsa."
                )

        except ErrorServicio as error:
            GestorLogs.registrar_error(
                f"Error al validar los parámetros de la sala "
                f"{self.identificador}",
                error
            )
            raise

    def validar_datos(self):
        self.validar_parametros()

    # -------------------------------
    # CÁLCULO DEL COSTO
    # -------------------------------

    def calcular_costo(self, duracion, descuento=0):
        try:
            if not self.disponible:
                raise ServicioNoDisponible(
                    "La sala seleccionada no está disponible."
                )

            # Validamos duración y descuento usando la clase padre.
            self.validar_costo(duracion, descuento)

            costo = self.tarifa_base * duracion

            valor_descuento = costo * descuento / 100

            costo_final = round(costo - valor_descuento, 2)

            GestorLogs.registrar_evento(
                f"Costo calculado para la sala {self.identificador}. "
                f"Duración: {duracion} horas. "
                f"Descuento: {descuento}%. "
                f"Total: ${costo_final:,.2f}"
            )

            return costo_final

        except ServicioNoDisponible as error:
            GestorLogs.registrar_error(
                f"No fue posible calcular el costo de la sala "
                f"{self.identificador}",
                error
            )
            raise

        except ErrorServicio:
            # El método validar_costo de la clase padre
            # ya registra los errores de duración y descuento.
            raise

    # -------------------------------
    # DESCRIPCIÓN DEL SERVICIO
    # -------------------------------

    def describir_servicio(self):

        estado = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        return (
            f"Servicio: {self.nombre}\n"
            f"Tipo de sala: {self.tipo_sala}\n"
            f"Capacidad: {self.capacidad} personas\n"
            f"Tarifa por hora: ${self.tarifa_base:,.2f}\n"
            f"Estado: {estado}"
        )

    # -------------------------------
    # MOSTRAR INFORMACIÓN
    # -------------------------------

    def mostrar_informacion(self):

        return (
            f"Identificador: {self.identificador}\n"
            f"{self.describir_servicio()}"
        )