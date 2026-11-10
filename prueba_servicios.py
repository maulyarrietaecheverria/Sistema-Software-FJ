"""
Pruebas de funcionamiento de los servicios de Software FJ.
Proyecto de Programación - UNAD.
"""

# Importamos los tres servicios especializados.
from servicios.reserva_salas import ReservaSalas
from servicios.alquiler_equipos import AlquilerEquipos
from servicios.asesoria import Asesoria

# Importamos la excepción personalizada.
from excepciones.errores_personalizados import ErrorServicio


print("==============================================")
print("       PRUEBAS DE SERVICIOS - SOFTWARE FJ")
print("==============================================")


# PRUEBA 1: Reserva de salas.
print("\nPRUEBA 1: Servicio de reserva de salas")

try:
    sala = ReservaSalas(
        "SAL001",
        "Sala de reuniones",
        50000,
        "Ejecutiva",
        15,
        True
    )

    print(sala.mostrar_informacion())
    print(f"Costo por 2 horas: ${sala.calcular_costo(2):,.2f}")

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 2: Alquiler de equipos.
print("\nPRUEBA 2: Servicio de alquiler de equipos")

try:
    equipo = AlquilerEquipos(
        "EQ001",
        "Alquiler de computadores",
        15000,
        "Portátil",
        10,
        True
    )

    print(equipo.mostrar_informacion())

    costo = equipo.calcular_costo(4, 10, 3)

    print("Cantidad solicitada: 3 computadores")
    print("Duración: 4 horas")
    print("Descuento: 10%")
    print(f"Costo total: ${costo:,.2f}")

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 3: Asesorías especializadas.
print("\nPRUEBA 3: Servicio de asesorías")

try:
    asesoria = Asesoria(
        "ASE001",
        "Asesoría tecnológica",
        80000,
        "Desarrollo de software",
        "Carlos Rodríguez",
        True
    )

    print(asesoria.mostrar_informacion())
    print(f"Costo por 2 horas: ${asesoria.calcular_costo(2):,.2f}")

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 4: Intentar alquilar más equipos de los disponibles.
print("\nPRUEBA 4: Cantidad de equipos no disponible")

try:
    costo = equipo.calcular_costo(2, 0, 15)
    print(f"Costo total: ${costo:,.2f}")

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 5: Intentar crear una asesoría sin especialidad.
print("\nPRUEBA 5: Especialidad inválida")

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


print("\n==============================================")
print("             PRUEBAS FINALIZADAS")
print("==============================================")