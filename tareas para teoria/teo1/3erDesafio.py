# Necesitamos procesar las notas de los estudiantes de este curso. Queremos
# saber:
# • cuál es el promedio de las notas;
# • cuántos estudiantes están por debajo del promedio
from csv import list_dialects


lista_notas=[]
suma_notas=0
nota=int (input ("Ingrese nota "))

while nota != -1:
    lista_notas.append(nota)
    suma_notas=suma_notas+nota
    nota=int (input ("Ingrese nota"))
promedio=suma_notas/len(lista_notas)

#otra forma de usar el for.
# cant_menor_prom=0
# for elem in lista_notas:
#     if (elem<promedio):
#         cant_menor_prom=cant_menor_prom+1

cant_menor_prom=0
for i in range(len(lista_notas)):
    if (lista_notas[i]<promedio):
        cant_menor_prom=cant_menor_prom+1

print(f"el valor del promedio es: {promedio}")
print(f"la cantidad de alumnos cuyo promedio esta por debajo del promedio es de: {cant_menor_prom}")
