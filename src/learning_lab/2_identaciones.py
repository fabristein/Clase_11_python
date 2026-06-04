# Declaración de variables en infraestructura (Tipado Dinámico)
nombre_servicio = "api-gateway"  # Tipo: String (Texto)
puerto_escucha = 8080            # Tipo: Integer (Número entero)
estado_activo = True             # Tipo: Boolean (Verdadero/Falso)

# La función print() con f-strings permite inyectar variables directamente usando llaves
print(f"Servicio: {nombre_servicio} operando en el puerto: {puerto_escucha}")

# --- ANÁLISIS DE ERROR COMÚN EN CLASE ---
# El siguiente código está comentado porque detiene la ejecución del programa.
# Descomentarlo en vivo para mostrar el 'IndentationError' a los alumnos:
#if estado_activo:
#print("Esto causará un IndentationError porque no tiene los espacios de sangría")