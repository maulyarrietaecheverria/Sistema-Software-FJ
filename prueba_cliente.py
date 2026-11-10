"""
Pruebas de funcionamiento de la clase Cliente.
Proyecto Software FJ - UNAD.
"""

from modelos.cliente import Cliente
from excepciones.errores_personalizados import ErrorCliente

print("========================================")
print("     PRUEBAS DE LA CLASE CLIENTE")
print("========================================")

# PRUEBA 1: Registro de cliente válido.
print("\nPRUEBA 1: Registro de cliente válido")

try:
    cliente1 = Cliente(
        "1001234567",
        "Carlos Pérez",
        "carlos@gmail.com",
        "3001234567"
    )

    print("Cliente registrado correctamente.")
    print(cliente1.mostrar_informacion())

except ErrorCliente as error:
    print("Error controlado:", error)


# PRUEBA 2: Registro con correo inválido.
print("\nPRUEBA 2: Registro de cliente con correo inválido")

try:
    cliente2 = Cliente(
        "1001234568",
        "María López",
        "maria_correo_invalido",
        "3001234568"
    )

    print("Cliente registrado correctamente.")

except ErrorCliente as error:
    print("Error controlado:", error)


# PRUEBA 3: Registro con teléfono inválido.
print("\nPRUEBA 3: Registro de cliente con teléfono inválido")

try:
    cliente3 = Cliente(
        "1001234569",
        "Andrés Gómez",
        "andres@gmail.com",
        "123"
    )

    print("Cliente registrado correctamente.")

except ErrorCliente as error:
    print("Error controlado:", error)


print("\n========================================")
print("       PRUEBAS FINALIZADAS")
print("========================================")