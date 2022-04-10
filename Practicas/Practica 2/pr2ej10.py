# 10. Trabajando con los contenidos de los archivos que pueden acceder en el curso:
#     -nombres
#     -eval1
#     -eval2
# Manipule estos archivos para realizar lo siguiente:
# • Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
# • Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
# promedio.

archivo = open ("eval1.txt","r")
notas1 = archivo.read().split(",")
archivo.close()
notas1 = list(map(int,notas1))  #genero una lista de enteros haciendo uso de la funcion map() e int().

archivo = open ("eval2.txt","r")
notas2 = archivo.read().split(",")
archivo.close()
notas2 = list(map(int,notas2))  #genero una lista de enteros haciendo uso de la funcion map() e int().

archivo = open ("nombres_1.txt","r")
nombres = archivo.read().split("\n")
archivo.close()


def generarEstructuraEstudiantes (nombres,notas_suma):
    """calcula el promedio de las notas y 
    genera diccionario que tiene como clave los nombre de 
    los alumnos y como valores la suma de sus notas.  """

    info_alum = {}
    for i in range(len(nombres)):
        info_alum[nombres[i]] = notas_suma[i]
    prom = sum(notas_suma) / (len(notas_suma))
    return info_alum, prom


def informarPromedioInferior(diccio_alum,prom):
    """informa los alumnos que sacaron una nota inferior al promedio"""

    for elem in diccio_alum:
        if diccio_alum.get(elem) < prom:
            print (f"alumno/a {elem} obtuvo una nota inferior al promedio")


notas_suma = []

for i in range(len(notas1)):
    notas_suma.append(notas1[i] + notas2[i])

for i,nom in enumerate(nombres):    #recorro la lista de nombres y reemplazo las comas por nada.
    nombres[i] = nom.replace(",","")


diccio_alum,prom = generarEstructuraEstudiantes(nombres,notas_suma)
informarPromedioInferior(diccio_alum,prom)