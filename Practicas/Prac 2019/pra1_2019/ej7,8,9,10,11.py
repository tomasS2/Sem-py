# 7.Para registrar las actividades de un usuario en un juego dado se requiere guardar los siguientes 
#datos:nombre del jugador, nivel alcanzado en el juego, puntaje máximo y tiempo de juego.Utilizando la estructura que considere más adecuada,
#almacenar la información de varios usuarios ingresados desde teclado.
#Tener en cuenta que se necesita acceder a un usuario determinado en forma directa sin recorrerla.
#
#y 8 
# 8.Con la estructura generada en el ejercicio 7, imprimir los datos de un usuario dado sin recorrerla estructura. 
# ¿La elección sobre la estructura fue adecuada? ¿Cuál usó? 
#
# y 9
# 9.Con la estructura generada en el ejercicio 7, imprima solos los nombres de los usuarios que jugaron sin recorrer la estructura.
#
#y 10
# 10. Dada la estructura generada en el ejercicio 7 imprimir el usuario que obtuvo mayor puntaje
#y 11
# 11.Dada la estructura del ejercicio 7, ingresar los datos correspondientes a la jugada de un usuario.
# Si el usuario existe previamente, guardar los datos de mayor puntaje.
# Luego imprimir el ranking de los 10 mejores puntajes.

def ingresarUsuarios ():
    """ingresa usuarios y los almacena en un diciconario"""
    #pto 7

    diccio= {}
    nombre = input("ingrese nombre: ")
    while nombre != "zzz":
        nivel = int(input("ingrese nivel: "))
        puntaje_max = int(input("ingrese puntaje maximo: "))
        tiempo_juego = int(input("ingrese tiempo de juego: "))
        diccio[nombre] = [nivel, puntaje_max, tiempo_juego]
        nombre = input("ingrese nombre: ")

    return diccio


diccio_usuarios = ingresarUsuarios()

#pto 8
# nom = input("ingrese el nombre de uno de los usuarios ingresados: ")
# if nom in diccio_usuarios:
#     print (f"Los datos del usuario '{nom}' son: ",(diccio_usuarios[nom]))


#pto 9
#print (diccio_usuarios.keys())

#pto 10
# max = -1
# for valor in diccio_usuarios:
#     if (diccio_usuarios[valor][1] > max):
#         max = diccio_usuarios[valor][1]
#         usu_mayor = valor
    
# print (f"El usuario que saco mayor puntaje es: {usu_mayor}")
        

#pto 11
print ("nueva jugada de un usuario")
nom_nuevo = input("ingrese nombre: ")
nivel_nuevo = int(input("ingrese nivel: "))
puntaje_max_nuevo = int(input("ingrese puntaje maximo: "))
tiempo_juego_nuevo = int(input("ingrese tiempo de juego: "))
if nom_nuevo in diccio_usuarios:
    if puntaje_max_nuevo > diccio_usuarios[nom_nuevo][1]:
        diccio_usuarios[nom_nuevo] = [nivel_nuevo, puntaje_max_nuevo, tiempo_juego_nuevo]
else:
    diccio_usuarios[nom_nuevo] = [nivel_nuevo, puntaje_max_nuevo, tiempo_juego_nuevo]
  