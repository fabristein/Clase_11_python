# Listado de inventario de infraestructura
servidores = ["web-01", "web-02", "db-01", "cache-01"]

print("--- Revisión Automatizada de Inventario ---")
for servidor in servidores:
    # Verificamos si la subcadena 'db' está presente dentro del nombre del servidor
    if "db" in servidor:
        print(f"Alerta de Seguridad: {servidor} es un nodo crítico de Base de Datos.")
    else:
        print(f"Nodo estándar detectado: {servidor}")

print("\n--- Simulación de Daemon de Red (Bucle While) ---")
# Control de reintentos de conexión ante caída de un servicio
reintentos = 0
while reintentos < 3:
    print(f"Intentando reconexión con el servidor... Intento número {reintentos + 1}")
    reintentos += 1  # Incrementamos obligatoriamente el contador para evitar un bucle infinito