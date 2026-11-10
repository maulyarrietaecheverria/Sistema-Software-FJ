"""
Pruebas de funcionamiento de la clase Reserva.
Proyecto Software FJ - UNAD.
"""

# Importamos las clases necesarias.
from modelos.cliente import Cliente
from modelos.reserva import Reserva

from servicios.reserva_salas import ReservaSalas
from servicios.alquiler_equipos import AlquilerEquipos
from servicios.asesoria import Asesoria

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import (
    ErrorReserva,
    ErrorSistema,
    OperacionNoPermitida
)


print("================================================")
print("       PRUEBAS DEL SISTEMA DE RESERVAS")
print("================================================")


# Creamos un cliente para realizar las pruebas.
cliente = Cliente(
    "1001234567",
    "Carlos Pérez",
    "carlos@gmail.com",
    "3001234567"
)


# PRUEBA 1: Crear una reserva de sala.
print("\nPRUEBA 1: Crear reserva de sala")

try:
    sala = ReservaSalas(
        "SAL001",
        "Sala de reuniones",
        50000,
        "Ejecutiva",
        15,
        True
    )

    reserva1 = Reserva(
        "RES001",
        cliente,
        sala,
        2,
        10
    )

    print("Reserva creada correctamente.")
    print(reserva1.mostrar_informacion())

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 2: Confirmar la reserva.
print("\nPRUEBA 2: Confirmar reserva")

try:
    print(reserva1.confirmar())
    print("Estado actual:", reserva1.estado)

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 3: Procesar la reserva.
print("\nPRUEBA 3: Procesar reserva")

try:
    print(reserva1.procesar())
    print("Estado actual:", reserva1.estado)

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 4: Intentar cancelar una reserva procesada.
print("\nPRUEBA 4: Cancelar reserva procesada")

try:
    print(reserva1.cancelar())

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 5: Crear una reserva de alquiler de equipos.
print("\nPRUEBA 5: Reserva de alquiler de equipos")

try:
    equipo = AlquilerEquipos(
        "EQ001",
        "Alquiler de computadores",
        15000,
        "Portátil",
        10,
        True
    )

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
    print("Error controlado:", error)


# PRUEBA 6: Cancelar una reserva pendiente.
print("\nPRUEBA 6: Cancelar reserva pendiente")

try:
    reserva3 = Reserva(
        "RES003",
        cliente,
        sala,
        1
    )

    print(reserva3.cancelar())
    print("Estado actual:", reserva3.estado)

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 7: Crear una reserva de asesoría.
print("\nPRUEBA 7: Reserva de asesoría")

try:
    asesoria = Asesoria(
        "ASE001",
        "Asesoría tecnológica",
        80000,
        "Desarrollo de software",
        "Carlos Rodríguez",
        True
    )

    reserva4 = Reserva(
        "RES004",
        cliente,
        asesoria,
        2
    )

    print(reserva4.mostrar_informacion())

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 8: Crear una reserva con duración inválida.
print("\nPRUEBA 8: Duración incorrecta")

try:
    reserva5 = Reserva(
        "RES005",
        cliente,
        sala,
        -3
    )

except ErrorReserva as error:
    print("Error controlado:", error)

    if error.__cause__:
        print("Causa original:", error.__cause__)


# PRUEBA 9: Intentar confirmar una reserva cancelada.
print("\nPRUEBA 9: Confirmar reserva cancelada")

try:
    reserva3.confirmar()

except OperacionNoPermitida as error:
    print("Error controlado:", error)


print("\n================================================")
print("             PRUEBAS FINALIZADAS")
print("================================================")