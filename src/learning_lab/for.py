# Mapeo de puertos de red estándares de un servidor Linux
puertos_servicios = {
    "http": 80,
    "https": 443,
    "ssh": 22
}

print("--- Mapeo Activo de Puertos (.items()) ---")
# .items() nos entrega el par clave-valor en cada ciclo, inyectándolos en 'servicio' y 'puerto'
for servicio, puerto in puertos_servicios.items():
    print(f"El protocolo de red {servicio} utiliza el puerto estándar: {puerto}")

print("\n--- Auditoría de Puertos Activos (.values()) ---")
# .values() extrae únicamente los números de los puertos, aislándolos de sus etiquetas
total_puertos = list(puertos_servicios.values())
print(f"Lista pura de puertos activos para escaneo: {total_puertos}")