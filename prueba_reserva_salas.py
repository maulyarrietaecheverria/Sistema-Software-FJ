"""
Pruebas de funcionamiento de la clase ReservaSalas.
Proyecto Software FJ - UNAD.
"""

# Importamos la clase que vamos a probar.
from servicios.reserva_salas import ReservaSalas

# Importamos las excepciones personalizadas.
from excepciones.errores_personalizados import ErrorSistema


print("========================================")
print("    PRUEBAS DE RESERVA DE SALAS")
print("========================================")


# PRUEBA 1: Registrar una sala correctamente.
print("\nPRUEBA 1: Registro de una sala")

try:
    sala = ReservaSalas(
        "SALA001",
        "Sala de reuniones",
        50000,
        "Ejecutiva",
        15,
        True
    )

    print("Sala registrada correctamente.")
    print(sala.mostrar_informacion())

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 2: Calcular el costo de una reserva.
print("\nPRUEBA 2: Cálculo del costo")

try:
    duracion = 2
    descuento = 10

    costo = sala.calcular_costo(duracion, descuento)

    print("Duración:", duracion, "horas")
    print("Descuento:", descuento, "%")
    print(f"Costo total: ${costo:,.2f}")

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 3: Intentar calcular con duración inválida.
print("\nPRUEBA 3: Duración inválida")

try:
    sala.calcular_costo(-2)

except ErrorSistema as error:
    print("Error controlado:", error)


# PRUEBA 4: Intentar registrar una sala con capacidad inválida.
print("\nPRUEBA 4: Capacidad inválida")

try:
    sala_invalida = ReservaSalas(
        "SALA002",
        "Sala pequeña",
        30000,
        "Estándar",
        -5,
        True
    )

except ErrorSistema as error:
    print("Error controlado:", error)


print("\n========================================")
print("       PRUEBAS FINALIZADAS")
print("========================================")