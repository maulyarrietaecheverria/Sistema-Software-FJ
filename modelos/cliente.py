"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene la clase Cliente, encargada de registrar,
almacenar y validar la información personal de los clientes.
"""

# Importamos las expresiones regulares.
import re

# Importamos la clase abstracta Entidad.
from modelos.entidad import Entidad

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import ErrorCliente

# Importamos el gestor de registros.
from utilidades.gestor_logs import GestorLogs


class Cliente(Entidad):
    """
    Representa un cliente registrado en Software FJ.
    """

    def __init__(self, identificacion, nombre, correo, telefono):

        try:
            # Inicializamos el identificador mediante la clase padre.
            super().__init__(identificacion)

            # Asignamos los atributos utilizando sus propiedades.
            self.nombre = nombre
            self.correo = correo
            self.telefono = telefono

            # Verificamos que todos los datos sean correctos.
            self.validar_datos()

            # Registramos la creación exitosa del cliente.
            GestorLogs.registrar_evento(
                f"Cliente registrado correctamente. "
                f"Identificación: {self.identificador}"
            )

        except ErrorCliente as error:

            # Registramos el error ocurrido durante el registro.
            GestorLogs.registrar_error(
                "No fue posible registrar el cliente",
                error
            )

            # Volvemos a lanzar la excepción para que pueda controlarse.
            raise

    # ==========================================
    # PROPIEDAD Y VALIDACIÓN DEL NOMBRE
    # ==========================================

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        try:
            if not isinstance(valor, str) or not valor.strip():
                raise ErrorCliente(
                    "El nombre del cliente no puede estar vacío."
                )

            if len(valor.strip()) < 3:
                raise ErrorCliente(
                    "El nombre debe tener al menos 3 caracteres."
                )

            self.__nombre = valor.strip()

        except ErrorCliente as error:
            GestorLogs.registrar_error(
                "Error en la validación del nombre del cliente",
                error
            )
            raise

    # ==========================================
    # PROPIEDAD Y VALIDACIÓN DEL CORREO
    # ==========================================

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        try:
            if not isinstance(valor, str):
                raise ErrorCliente(
                    "El correo debe ser un texto válido."
                )

            patron = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'

            if not re.match(patron, valor.strip()):
                raise ErrorCliente(
                    "El correo electrónico no tiene un formato válido."
                )

            self.__correo = valor.strip().lower()

        except ErrorCliente as error:
            GestorLogs.registrar_error(
                "Error en la validación del correo del cliente",
                error
            )
            raise

    # ==========================================
    # PROPIEDAD Y VALIDACIÓN DEL TELÉFONO
    # ==========================================

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        try:
            if not isinstance(valor, str):
                raise ErrorCliente(
                    "El teléfono debe ingresarse como texto."
                )

            # Eliminamos espacios, guiones y otros caracteres.
            numero = re.sub(r'\D', '', valor)

            # Validamos que tenga entre 7 y 10 dígitos.
            if not numero.isdigit() or not 7 <= len(numero) <= 10:
                raise ErrorCliente(
                    "El número de teléfono debe tener entre 7 y 10 dígitos."
                )

            self.__telefono = numero

        except ErrorCliente as error:
            GestorLogs.registrar_error(
                "Error en la validación del teléfono del cliente",
                error
            )
            raise

    # ==========================================
    # VALIDACIÓN GENERAL DEL CLIENTE
    # ==========================================

    def validar_datos(self):

        if not self.identificador:
            raise ErrorCliente(
                "La identificación es obligatoria."
            )

        if not self.nombre or not self.correo or not self.telefono:
            raise ErrorCliente(
                "Todos los datos del cliente son obligatorios."
            )

        return True

    # ==========================================
    # MOSTRAR INFORMACIÓN DEL CLIENTE
    # ==========================================

    def mostrar_informacion(self):

        return (
            f"Identificación: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )

    # ==========================================
    # REPRESENTACIÓN DEL OBJETO
    # ==========================================

    def __str__(self):

        return (
            f"Cliente: {self.nombre} | "
            f"Identificación: {self.identificador} | "
            f"Correo: {self.correo}"
        )