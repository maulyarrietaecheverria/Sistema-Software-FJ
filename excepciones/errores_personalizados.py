"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo contiene las excepciones personalizadas utilizadas
para controlar los errores que puedan presentarse en el sistema.
"""


# Excepción general para los errores del sistema.
class ErrorSistema(Exception):
    """Representa un error general dentro de Software FJ."""
    pass


# Error cuando los datos de un cliente son incorrectos.
class ErrorCliente(ErrorSistema):
    """Se genera cuando los datos de un cliente no son válidos."""
    pass


# Error cuando un servicio presenta información incorrecta.
class ErrorServicio(ErrorSistema):
    """Se genera cuando un servicio tiene parámetros inválidos."""
    pass


# Error cuando se intenta realizar una reserva incorrecta.
class ErrorReserva(ErrorSistema):
    """Se genera cuando ocurre un problema con una reserva."""
    pass


# Error cuando un servicio no está disponible.
class ServicioNoDisponible(ErrorServicio):
    """Se genera cuando el servicio solicitado no está disponible."""
    pass


# Error cuando se intenta realizar una operación no permitida.
class OperacionNoPermitida(ErrorSistema):
    """Se genera cuando una operación no está permitida."""
    pass


# Error cuando faltan parámetros obligatorios.
class ParametroFaltante(ErrorSistema):
    """Se genera cuando no se proporciona un dato obligatorio."""
    pass