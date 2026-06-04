# --- MANEJO AVANZADO DE LISTAS ---
letras = ["A", "B", "C", "D"]
print(f"Lista completa: {letras}")
print(f"Primer elemento (Índice 0): {letras[0]}") # Acceso por indexación directa

# Slicing: Extrae desde el índice 1 inclusive, hasta el 3 sin incluirlo (índices 1 y 2)
print(f"Subconjunto extraído (Slicing): {letras[1:3]}") 

# --- APLICACIÓN PRÁCTICA DE SETS ---
# Imaginemos un log del sistema con IDs de procesos o contenedores duplicados
ids_sucios = [101, 102, 105, 101, 102]
# Al castearlo con set(), eliminamos los duplicados de forma nativa e inmediata
ids_unicos = set(ids_sucios)
print(f"IDs únicos limpios: {ids_unicos}") 

# --- DICCIONARIOS ANIDADOS (Estructura Base Config) ---
# Esta sintaxis es el equivalente lógico a las líneas de código de una receta de Docker
config = {
    "version": "3.9",
    "servicios": ["auth", "db"] # Un valor puede ser perfectamente una lista
}
print(f"Versión de la estructura: {config['version']}")