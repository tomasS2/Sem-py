# Necesitamos procesar las notas de los estudiantes de este curso. Queremos
# saber:
# • cuál es el promedio de las notas.
# • qué estudiantes están por debajo del promedio.

nom_alumno =  input("Ingrese el nombre del alumno: ")
dicci_alu = {}
suma_notas = 0 
while nom_alumno != "fin":
    nota = int(input(f"Ingrese nota del alumno {nom_alumno} "))
    dicci_alu[nom_alumno] = nota #guarda para la clave "nom_alumno" su nota.
    suma_notas = suma_notas + nota
    nom_alumno = input("Ingrese el nombre del alumno: ")
promedio = suma_notas / len(dicci_alu)


#creo otra estructura donde guardo los alumnos con nota por debajo del promedio.
#se podria imprimir directamente el alumno pero queria probar esta forma:
dicci_debajo_prom={}
for elem in dicci_alu:
    if dicci_alu[elem]<promedio:
        dicci_debajo_prom[elem]=dicci_alu[elem]

print (dicci_debajo_prom)
