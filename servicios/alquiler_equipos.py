"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene la clase AlquilerEquipos, encargada de gestionar
el alquiler de equipos tecnológicos y audiovisuales.
"""

# Importamos la clase abstracta Servicio.
from modelos.servicio import Servicio

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import ErrorServicio

# Importamos el gestor de registros.
from utilidades.gestor_logs import GestorLogs


class AlquilerEquipos(Servicio):

    # Constructor de la clase.
    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        tipo_equipo,
        cantidad_disponible,
        disponible=True
    ):

        # Inicializamos los atributos heredados.
        super().__init__(identificador, nombre, tarifa_base)

        # Guardamos las características de los equipos.
        self._tipo_equipo = tipo_equipo
        self._cantidad_disponible = cantidad_disponible
        self._disponible = disponible

        # Validamos la información del equipo.
        self.validar_datos()

        # Registramos la creación exitosa del servicio.
        GestorLogs.registrar_evento(
            f"Servicio de alquiler de equipos registrado: "
            f"{self.identificador}"
        )

    # ---------------------------------
    # PROPIEDADES Y ENCAPSULAMIENTO
    # ---------------------------------

    @property
    def tipo_equipo(self):
        return self._tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, valor):

        anterior = self._tipo_equipo
        self._tipo_equipo = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._tipo_equipo = anterior
            raise

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, valor):

        anterior = self._cantidad_disponible
        self._cantidad_disponible = valor

        try:
            self.validar_parametros()
        except ErrorServicio:
            self._cantidad_disponible = anterior
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
                not isinstance(self._tipo_equipo, str)
                or not self._tipo_equipo.strip()
            ):
                raise ErrorServicio(
                    "Debe especificar el tipo de equipo."
                )

            if (
                not isinstance(self._cantidad_disponible, int)
                or isinstance(self._cantidad_disponible, bool)
                or self._cantidad_disponible < 0
            ):
                raise ErrorServicio(
                    "La cantidad disponible debe ser un entero "
                    "igual o mayor que cero."
                )

            if not isinstance(self._disponible, bool):
                raise ErrorServicio(
                    "La disponibilidad debe ser verdadera o falsa."
                )

        except ErrorServicio as error:

            GestorLogs.registrar_error(
                f"Error al validar los parámetros del equipo "
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
    # VALIDACIÓN DE CANTIDADES
    # ---------------------------------

    def validar_cantidad(self, cantidad):

        try:

            if (
                not isinstance(cantidad, int)
                or isinstance(cantidad, bool)
                or cantidad <= 0
            ):
                raise ErrorServicio(
                    "La cantidad solicitada debe ser un entero positivo."
                )

            if not self.disponible or self.cantidad_disponible == 0:
                raise ErrorServicio(
                    "El equipo no se encuentra disponible."
                )

            if cantidad > self.cantidad_disponible:
                raise ErrorServicio(
                    "No hay suficientes equipos disponibles."
                )

            return True

        except ErrorServicio as error:

            GestorLogs.registrar_error(
                f"Error al validar la cantidad solicitada "
                f"para el equipo {self.identificador}",
                error
            )

            raise

    # ---------------------------------
    # CÁLCULO DEL COSTO DEL ALQUILER
    # ---------------------------------

    def calcular_costo(self, duracion, descuento=0, cantidad=1):

        # Validamos la duración y el descuento.
        # Este método ya registra sus propios errores.
        self.validar_costo(duracion, descuento)

        # Comprobamos la cantidad solicitada.
        self.validar_cantidad(cantidad)

        # Calculamos el valor según horas y unidades.
        costo = self.tarifa_base * duracion * cantidad

        # Aplicamos el descuento correspondiente.
        costo_final = round(
            costo - (costo * descuento / 100),
            2
        )

        # Registramos el cálculo exitoso.
        GestorLogs.registrar_evento(
            f"Costo de alquiler calculado para el equipo "
            f"{self.identificador}. "
            f"Duración: {duracion} horas. "
            f"Cantidad: {cantidad}. "
            f"Descuento: {descuento}%. "
            f"Total: ${costo_final:,.2f}"
        )

        return costo_final

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
            f"Tipo de equipo: {self.tipo_equipo}\n"
            f"Cantidad disponible: {self.cantidad_disponible}\n"
            f"Tarifa por hora y unidad: ${self.tarifa_base:,.2f}\n"
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