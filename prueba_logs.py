"""
Pruebas del gestor de registros.
Proyecto Software FJ - UNAD.
"""

from utilidades.gestor_logs import GestorLogs

print("========================================")
print("       PRUEBAS DEL GESTOR DE LOGS")
print("========================================")

# PRUEBA 1: Registrar un evento.
GestorLogs.registrar_evento(
    "El sistema inició correctamente."
)
print("Evento registrado correctamente.")

# PRUEBA 2: Registrar una advertencia.
GestorLogs.registrar_advertencia(
    "Se realizó una prueba de advertencia."
)
print("Advertencia registrada correctamente.")

# PRUEBA 3: Registrar un error controlado.
try:
    resultado = 10 / 0

except ZeroDivisionError as error:
    GestorLogs.registrar_error(
        "Se presentó un error durante una operación matemática",
        error
    )
    print("Error registrado correctamente.")

print("========================================")
print("       PRUEBAS FINALIZADAS")
print("========================================")