"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene la clase Reserva, encargada de relacionar
los clientes con los servicios y administrar el estado de las reservas.
"""

# Importamos la clase Entidad.
from modelos.entidad import Entidad

# Importamos las clases Cliente y Servicio.
from modelos.cliente import Cliente
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import (
    ErrorReserva,
    ErrorServicio,
    OperacionNoPermitida,
    ServicioNoDisponible
)

# Importamos el gestor de registros.
from utilidades.gestor_logs import GestorLogs


# Clase Reserva que hereda de Entidad.
class Reserva(Entidad):

    # Constructor de la clase.
    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion,
        descuento=0,
        cantidad=1
    ):

        # Inicializamos el identificador heredado.
        super().__init__(identificador)

        # Guardamos la información de la reserva.
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._descuento = descuento
        self._cantidad = cantidad

        # Toda reserva comienza en estado pendiente.
        self._estado = "Pendiente"

        try:
            # Validamos la información de la reserva.
            self.validar_datos()

            # Registramos la creación exitosa.
            GestorLogs.registrar_evento(
                f"Reserva creada correctamente. "
                f"Identificador: {self.identificador}. "
                f"Cliente: {self._cliente.nombre}. "
                f"Servicio: {self._servicio.nombre}. "
                f"Estado: {self._estado}"
            )

        except (ErrorReserva, ErrorServicio) as error:

            # Registramos los errores durante la creación.
            GestorLogs.registrar_error(
                f"No fue posible crear la reserva "
                f"{self.identificador}",
                error
            )

            raise

    # ---------------------------------
    # PROPIEDADES Y ENCAPSULAMIENTO
    # ---------------------------------

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    # ---------------------------------
    # VALIDACIÓN DE LA RESERVA
    # ---------------------------------

    def validar_datos(self):

        # Comprobamos que exista un cliente válido.
        if not isinstance(self._cliente, Cliente):
            raise ErrorReserva(
                "Debe proporcionar un cliente válido."
            )

        # Comprobamos que exista un servicio válido.
        if not isinstance(self._servicio, Servicio):
            raise ErrorReserva(
                "Debe proporcionar un servicio válido."
            )

        # Comprobamos la disponibilidad del servicio.
        if not self._servicio.disponible:
            raise ServicioNoDisponible(
                "El servicio seleccionado no está disponible."
            )

        try:

            # Validamos la duración y el descuento.
            self._servicio.validar_costo(
                self._duracion,
                self._descuento
            )

            # Si el servicio controla cantidades,
            # comprobamos que existan suficientes unidades.
            if hasattr(self._servicio, "validar_cantidad"):

                self._servicio.validar_cantidad(
                    self._cantidad
                )

            elif self._cantidad != 1:

                raise ErrorReserva(
                    "La cantidad debe ser 1 para este tipo de servicio."
                )

        except ErrorServicio as error:

            # Conservamos la causa original del error.
            raise ErrorReserva(
                "No fue posible validar los datos de la reserva."
            ) from error

        return True

    # ---------------------------------
    # CÁLCULO DEL COSTO DE LA RESERVA
    # ---------------------------------

    def calcular_costo(self):

        # Si el servicio controla cantidades,
        # enviamos también la cantidad solicitada.
        if hasattr(self._servicio, "validar_cantidad"):

            costo = self._servicio.calcular_costo(
                self._duracion,
                self._descuento,
                self._cantidad
            )

        else:

            # Para los demás servicios utilizamos
            # la duración y el descuento.
            costo = self._servicio.calcular_costo(
                self._duracion,
                self._descuento
            )

        # Registramos el valor calculado para la reserva.
        GestorLogs.registrar_evento(
            f"Costo de reserva calculado. "
            f"Identificador: {self.identificador}. "
            f"Total: ${costo:,.2f}"
        )

        return costo

    # ---------------------------------
    # CONFIRMAR RESERVA
    # ---------------------------------

    def confirmar(self):

        try:

            if self._estado != "Pendiente":
                raise OperacionNoPermitida(
                    "Solamente se pueden confirmar reservas pendientes."
                )

            if not self._servicio.disponible:
                raise ServicioNoDisponible(
                    "El servicio ya no está disponible."
                )

            # Actualizamos el estado.
            self._estado = "Confirmada"

            # Registramos la confirmación.
            GestorLogs.registrar_evento(
                f"Reserva confirmada. "
                f"Identificador: {self.identificador}"
            )

            return "La reserva fue confirmada correctamente."

        except (OperacionNoPermitida, ServicioNoDisponible) as error:

            GestorLogs.registrar_error(
                f"Error al confirmar la reserva "
                f"{self.identificador}",
                error
            )

            raise

    # ---------------------------------
    # CANCELAR RESERVA
    # ---------------------------------

    def cancelar(self):

        try:

            if self._estado not in ("Pendiente", "Confirmada"):
                raise OperacionNoPermitida(
                    "No se puede cancelar una reserva que ya fue procesada."
                )

            # Actualizamos el estado.
            self._estado = "Cancelada"

            # Registramos la cancelación.
            GestorLogs.registrar_evento(
                f"Reserva cancelada. "
                f"Identificador: {self.identificador}"
            )

            return "La reserva fue cancelada correctamente."

        except OperacionNoPermitida as error:

            GestorLogs.registrar_error(
                f"Error al cancelar la reserva "
                f"{self.identificador}",
                error
            )

            raise

    # ---------------------------------
    # PROCESAR RESERVA
    # ---------------------------------

    def procesar(self):

        try:

            if self._estado != "Confirmada":
                raise OperacionNoPermitida(
                    "Solamente se pueden procesar reservas confirmadas."
                )

            # Actualizamos el estado.
            self._estado = "Procesada"

            # Registramos el procesamiento.
            GestorLogs.registrar_evento(
                f"Reserva procesada correctamente. "
                f"Identificador: {self.identificador}"
            )

            return "La reserva fue procesada correctamente."

        except OperacionNoPermitida as error:

            GestorLogs.registrar_error(
                f"Error al procesar la reserva "
                f"{self.identificador}",
                error
            )

            raise

    # ---------------------------------
    # MOSTRAR INFORMACIÓN DE LA RESERVA
    # ---------------------------------

    def mostrar_informacion(self):

        return (
            f"Identificador de reserva: {self.identificador}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}\n"
            f"Costo total: ${self.calcular_costo():,.2f}"
        )

    # ---------------------------------
    # REPRESENTACIÓN DE LA RESERVA
    # ---------------------------------

    def __str__(self):

        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Estado: {self.estado}"
        )