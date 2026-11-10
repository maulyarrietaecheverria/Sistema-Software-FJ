"""
Pruebas de validación de la clase abstracta Servicio.
Proyecto Software FJ - UNAD.
"""

from servicios.reserva_salas import ReservaSalas
from excepciones.errores_personalizados import ErrorServicio

print("========================================")
print("    PRUEBAS DE LA CLASE SERVICIO")
print("========================================")

# PRUEBA 1: Crear un servicio válido.
print("\nPRUEBA 1: Creación de servicio válido")

try:
    sala = ReservaSalas(
        "SAL001",
        "Sala de reuniones",
        50000,
        "Ejecutiva",
        15,
        True
    )

    print("Servicio creado correctamente.")
    print(sala.describir_servicio())

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 2: Crear un servicio con tarifa incorrecta.
print("\nPRUEBA 2: Tarifa inválida")

try:
    sala_invalida = ReservaSalas(
        "SAL002",
        "Sala de capacitación",
        -50000,
        "Capacitación",
        20,
        True
    )

    print("Servicio creado correctamente.")

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 3: Duración incorrecta.
print("\nPRUEBA 3: Duración inválida")

try:
    sala.validar_costo(-2)

except ErrorServicio as error:
    print("Error controlado:", error)


# PRUEBA 4: Descuento incorrecto.
print("\nPRUEBA 4: Descuento inválido")

try:
    sala.validar_costo(2, 150)

except ErrorServicio as error:
    print("Error controlado:", error)


print("\n========================================")
print("       PRUEBAS FINALIZADAS")
print("========================================")