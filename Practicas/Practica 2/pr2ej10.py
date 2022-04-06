# 10. Trabajando con los contenidos de los archivos que pueden acceder en el curso:
#     -nombres
#     -eval1
#     -eval2
# Manipule estos archivos para realizar lo siguiente:
# • Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
# • Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
# promedio.


# with open ("nombres_1.txt") as file_object:
#     nombres = file_object.read()
with open ("eval1.txt") as file_object:
    eval1 = file_object.read()
with open ("eval2.txt") as file_object:
    eval2 = file_object.read()



def generarEstructuraEstudiantes (nombres,eval1,eval2):
    """calcula el promedio de las notas y 
    genera diccionario que tiene como clave los nombre de 
    los alumnos y como valores la suma de sus notas.  """

    diccio_alum = {}
    sumador_prom = 0
    prom = 0
    for i in range(len(nombres)):
        diccio_alum[nombres[i]]=eval1[i]+eval2[i]
        sumador_prom = sumador_prom + eval1[i]+eval2[i]
    prom = sumador_prom/(len(eval1)+len(eval2))
    return diccio_alum, prom


def informarPromedioInferior(diccio_alum,prom):
    """informa los alumnos que sacaron una nota inferior al promedio"""

    for elem in diccio_alum:
        if diccio_alum.get(elem) < prom:
            print (f"alumno/a {elem} obtuvo una nota inferior al promedio")



#nombres = nombres.split(",")#problemas con los \n
nombres = 'Agustin','Alan','Andrés','Ariadna','Bautista','CAROLINA','CESAR','David','Diego','Dolores','DYLAN','ELIANA','Emanuel','Fabián','Facundo','Facundo','FEDERICO','FEDERICO','GONZALO','Gregorio','Ignacio','Jonathan','Jonathan','Jorge','JOSE','JUAN','Juan','Juan','Julian','Julieta','LAUTARO','Leonel','LUIS','Luis','Marcos','María','MATEO','Matias','Nicolás','NICOLAS','Noelia','Pablo','Priscila','TOMAS','Tomás','Ulises','Yanina'
eval1 = eval1.split(",")
eval1 = list(map(int,eval1))
eval2 = eval2.split(",")
eval2 = list(map(int,eval2))


diccio_alum,prom = generarEstructuraEstudiantes(nombres,eval1,eval2)
informarPromedioInferior(diccio_alum,prom)