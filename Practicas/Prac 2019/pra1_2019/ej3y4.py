# 3.Genere una nueva lista con todas las palabras de la frase dada en el ejercicio 1 en mayúsculas.
# y 4
# 4.Dada la lista de palabras generada en el ejercicio 3, arme un string con la frase
#  armada contodas ellas separadas por un único espacio en blanco



frase= "Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaríaautomatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en ungran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotosde una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada,o una aplicación especializada con interfaz gráfica, o un juego simple."

frase = frase.upper().split()
#hasta aca arriba el ejer 3


#a partir de aca el 4
string = " ".join(frase)

print (string)