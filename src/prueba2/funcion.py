#print hola mundo
#print("hola mundo")
#nombre = "alumnos"
#print(f"bienvenidos {nombre}")
#input y operaciones basicas
#print("ingrese su nombre:")
#nombre = input()
#print(f"bienvenido {nombre}")

numero = 3
# numero1 = int(input("ingrese un numero: "))
# resultado = numero + numero1
# print(resultado)
#bloque if,elif,else
# if resultado < 5:
#     print("el resultado es menor que 5")
#     if resultado == 4:
#         print("el resultado es 4")
#     else:
#         print("el resultado es diferente de 4")
# elif resultado == 5:
#     print("el resultado es igual a 5")
# else:
#     print("el resultado es mayor que 5")
    
#bloque while
# contador=0
# while contador < 5:
#     print(contador)
#     contador += 1

#bloque for
array = [1, 2, 3, 4, 5]
# for i in array:
#         if i != 4:
#             print(i)


#bloque slicing
# for i in array[2:4]:
#     print(i)
# array+= [3]
# print(array)
# #bloque funcion
# #print(dir(array))
# descartado = array.pop(0)
# print(descartado)
# print(array)
# help(array)
###tuplas
tupla = (1,2)
print(id(tupla))
tupla = (3,4)
print(id(tupla))
print(tupla)

##funciones
import funciones
print(funciones.suma(1,2))
print(funciones.aprobado(5,2))

#diccionarios
auto={
    "patente":123,
    "duenio":{
        "nombre":"Juan",
        "edad":30
    },
    "color":"rojo"
}
print(auto["patente"])

#print(resultado) -> no se puede acceder a la variable resultado fuera de la funcion