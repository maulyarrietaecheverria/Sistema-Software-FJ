"""
Programa principal del Sistema Integral de Gestión
de Clientes, Servicios y Reservas.
Proyecto Software FJ - UNAD.
"""

# Importamos las clases principales del sistema.
from modelos.cliente import Cliente
from modelos.reserva import Reserva

# Importamos los servicios especializados.
from servicios.reserva_salas import ReservaSalas
from servicios.alquiler_equipos import AlquilerEquipos
from servicios.asesoria import Asesoria

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import (
    ErrorSistema,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    OperacionNoPermitida
)

# Importamos el gestor de registros.
from utilidades.gestor_logs import GestorLogs


def mostrar_titulo():
    """Muestra la presentación inicial del sistema."""

    print("\n" + "=" * 60)
    print("       SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("                  PROYECTO UNAD")
    print("=" * 60)


def mostrar_separador():
    """Separa visualmente las operaciones."""

    print("\n" + "-" * 60)


def ejecutar_sistema():
    """
    Ejecuta las operaciones de demostración del sistema.
    Los errores son controlados para permitir que el programa
    continúe funcionando.
    """

    mostrar_titulo()

    # --------------------------------------------------
    # OPERACIÓN 1: Crear un cliente válido.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 1: Registro de cliente")

    try:
        cliente = Cliente(
            "1001234567",
            "Carlos Pérez",
            "carlos@gmail.com",
            "3001234567"
        )

    except ErrorCliente as error:
        print("No fue posible registrar el cliente:", error)

    else:
        print("Cliente registrado correctamente.")
        print(cliente.mostrar_informacion())

    finally:
        print("Finalizó la operación de registro de cliente.")

    # --------------------------------------------------
    # OPERACIÓN 2: Intentar registrar un cliente inválido.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 2: Validación de cliente incorrecto")

    try:
        cliente_invalido = Cliente(
            "1009876543",
            "Laura Martínez",
            "correo_invalido",
            "3009876543"
        )

    except ErrorCliente as error:
        print("Error controlado al registrar el cliente:", error)

    else:
        print("Cliente registrado:", cliente_invalido.nombre)

    finally:
        print("Finalizó la validación del cliente.")

    # --------------------------------------------------
    # OPERACIÓN 3: Registrar una sala de reuniones.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 3: Registro de sala")

    try:
        sala = ReservaSalas(
            "SAL001",
            "Sala de reuniones",
            50000,
            "Ejecutiva",
            15,
            True
        )

        print("Sala registrada correctamente.")
        print(sala.mostrar_informacion())

    except ErrorServicio as error:
        print("Error al registrar la sala:", error)

    # --------------------------------------------------
    # OPERACIÓN 4: Registrar equipos disponibles.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 4: Registro de alquiler de equipos")

    try:
        equipo = AlquilerEquipos(
            "EQ001",
            "Alquiler de computadores",
            15000,
            "Portátil",
            10,
            True
        )

        print("Servicio de alquiler registrado correctamente.")
        print(equipo.mostrar_informacion())

    except ErrorServicio as error:
        print("Error al registrar los equipos:", error)

    # --------------------------------------------------
    # OPERACIÓN 5: Registrar un servicio de asesoría.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 5: Registro de asesoría")

    try:
        asesoria = Asesoria(
            "ASE001",
            "Asesoría tecnológica",
            80000,
            "Desarrollo de software",
            "Carlos Rodríguez",
            True
        )

        print("Asesoría registrada correctamente.")
        print(asesoria.mostrar_informacion())

    except ErrorServicio as error:
        print("Error al registrar la asesoría:", error)

    # --------------------------------------------------
    # OPERACIÓN 6: Crear una reserva de sala.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 6: Crear reserva de sala")

    try:
        reserva1 = Reserva(
            "RES001",
            cliente,
            sala,
            2,
            10
        )

        print(reserva1.mostrar_informacion())

    except ErrorSistema as error:
        print("Error al crear la reserva:", error)

    # --------------------------------------------------
    # OPERACIÓN 7: Confirmar y procesar una reserva.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 7: Confirmación y procesamiento")

    try:
        print(reserva1.confirmar())
        print(reserva1.procesar())
        print("Estado final:", reserva1.estado)

    except ErrorSistema as error:
        print("No fue posible completar la operación:", error)

    # --------------------------------------------------
    # OPERACIÓN 8: Crear una reserva de equipos.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 8: Reserva de alquiler de equipos")

    try:
        reserva2 = Reserva(
            "RES002",
            cliente,
            equipo,
            4,
            10,
            3
        )

        print(reserva2.mostrar_informacion())
        print(reserva2.confirmar())

    except ErrorSistema as error:
        print("Error al crear la reserva de equipos:", error)

    # --------------------------------------------------
    # OPERACIÓN 9: Crear una reserva de asesoría.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 9: Reserva de asesoría")

    try:
        reserva3 = Reserva(
            "RES003",
            cliente,
            asesoria,
            2
        )

        print(reserva3.mostrar_informacion())

    except ErrorSistema as error:
        print("Error al crear la reserva de asesoría:", error)

    # --------------------------------------------------
    # OPERACIÓN 10: Cancelar una reserva pendiente.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 10: Cancelación de reserva")

    try:
        reserva4 = Reserva(
            "RES004",
            cliente,
            sala,
            1
        )

        print(reserva4.cancelar())
        print("Estado actual:", reserva4.estado)

    except ErrorSistema as error:
        print("Error al cancelar la reserva:", error)

    # --------------------------------------------------
    # OPERACIÓN 11: Intentar reservar más equipos
    # de los disponibles.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 11: Validación de disponibilidad de equipos")

    try:
        reserva_invalida = Reserva(
            "RES005",
            cliente,
            equipo,
            2,
            0,
            15
        )

        print(reserva_invalida.mostrar_informacion())

    except ErrorReserva as error:
        print("Error controlado:", error)

        if error.__cause__:
            print("Causa original:", error.__cause__)

    # --------------------------------------------------
    # OPERACIÓN 12: Intentar crear una reserva
    # con duración incorrecta.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 12: Validación de duración incorrecta")

    try:
        reserva_invalida = Reserva(
            "RES006",
            cliente,
            sala,
            -3
        )

    except ErrorReserva as error:
        print("Error controlado:", error)

        if error.__cause__:
            print("Causa original:", error.__cause__)

    # --------------------------------------------------
    # OPERACIÓN 13: Intentar cancelar una reserva
    # que ya fue procesada.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 13: Validación de estado de reserva")

    try:
        print(reserva1.cancelar())

    except OperacionNoPermitida as error:
        print("Operación no permitida:", error)

    # --------------------------------------------------
    # OPERACIÓN 14: Intentar registrar una asesoría
    # sin especificar su especialidad.
    # --------------------------------------------------

    mostrar_separador()
    print("OPERACIÓN 14: Validación de servicio incorrecto")

    try:
        asesoria_invalida = Asesoria(
            "ASE002",
            "Asesoría general",
            50000,
            "",
            "Laura Martínez",
            True
        )

    except ErrorServicio as error:
        print("Error controlado:", error)

    # --------------------------------------------------
    # FINALIZACIÓN DEL SISTEMA.
    # --------------------------------------------------

    mostrar_separador()
    print("PROCESO FINALIZADO")
    print("Las operaciones simuladas han terminado.")
    print("Los eventos y errores fueron registrados en el log.")

    GestorLogs.registrar_evento(
        "Finalización de la ejecución principal del sistema."
    )

    print("=" * 60)
    print("          SISTEMA SOFTWARE FJ - UNAD")
    print("=" * 60)


# Punto de entrada del programa.
if __name__ == "__main__":
    try:
        ejecutar_sistema()

    except Exception as error:
        GestorLogs.registrar_error(
            "Se produjo un error inesperado en el programa principal",
            error
        )

        print("\nSe presentó un error inesperado:", error)

    finally:
        print("\nEjecución del programa principal terminada.")