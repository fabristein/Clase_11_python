# Ejemplo de tipado dinámico y naturaleza de objetos
estado_activo = True  # El intérprete deduce automáticamente que es un booleano (bool)

# Al ser un objeto en memoria, podemos inspeccionar su "caja de herramientas" interna
print("--- Métodos internos del objeto booleano ---")
#print(dir(estado_activo))
def suma(a,b):
    return a + b
mi_lista = [1, 2, 3]
print(dir(mi_lista))
help(mi_lista.pop)
# Uso de la variable en una estructura lógica básica
if estado_activo:
    print("El sistema está operativo.")

# Demostración de que las funciones en Python también son objetos en memoria
def saludar():
    print("Conexión establecida")

# Verificamos su tipo: mostrará <class 'function'> evidenciando que es un objeto de clase función
print(type(saludar))