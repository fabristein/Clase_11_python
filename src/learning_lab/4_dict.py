# Lista de imágenes oficiales de Docker disponibles localmente en el servidor
imagenes_disponibles = ["nginx", "postgres", "redis"]

# Diccionario complejo que representa la configuración de un contenedor de base de datos
configuracion_db = {
    "image": "postgres:15",
    "environment": {
        "user": "admin",
        "pass": "secret123"
    },
    "ports": ["5432:5432"]
}

# Demostración de acceso indexado a listas y acceso por clave a diccionarios
print(f"Iniciando servicio desde la imagen: {imagenes_disponibles[1]}") # Accede a 'postgres'
print(f"Mapeo de puertos configurado: {configuracion_db['ports']}")