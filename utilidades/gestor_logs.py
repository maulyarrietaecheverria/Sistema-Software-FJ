"""
Proyecto: Sistema Integral de Gestión de Clientes, Servicios y Reservas
Empresa: Software FJ
Curso: Programación - 213023
Universidad Nacional Abierta y a Distancia - UNAD

Descripción:
Este módulo permite registrar los eventos y errores del sistema
en un archivo de texto llamado sistema.log.
"""

import logging
from pathlib import Path


class GestorLogs:
    """
    Clase encargada de administrar los registros del sistema.
    """

    # Crear la ruta de la carpeta logs dentro del proyecto.
    RUTA_LOGS = Path(__file__).resolve().parent.parent / "logs"

    # Crear la carpeta automáticamente si todavía no existe.
    RUTA_LOGS.mkdir(parents=True, exist_ok=True)

    # Definir la ubicación del archivo de registros.
    RUTA_ARCHIVO = RUTA_LOGS / "sistema.log"

    # Configurar el sistema de registros.
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.INFO)

    # Evitar que se agreguen manejadores repetidos.
    if not logger.handlers:

        # Configurar el archivo donde se guardarán los registros.
        manejador = logging.FileHandler(
            RUTA_ARCHIVO,
            encoding="utf-8"
        )

        # Definir el formato de cada registro.
        formato = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        manejador.setFormatter(formato)

        # Conectar el archivo con el sistema de registros.
        logger.addHandler(manejador)

    @classmethod
    def registrar_evento(cls, mensaje):
        """
        Registra un evento normal del sistema.
        """
        cls.logger.info(mensaje)

    @classmethod
    def registrar_advertencia(cls, mensaje):
        """
        Registra una advertencia del sistema.
        """
        cls.logger.warning(mensaje)

    @classmethod
    def registrar_error(cls, mensaje, error=None):
        """
        Registra un error y, si se proporciona, su información técnica.
        """
        if error is not None:
            cls.logger.error(
                f"{mensaje}: {error}",
                exc_info=(
                    type(error),
                    error,
                    error.__traceback__
                )
            )
        else:
            cls.logger.error(mensaje)