# 2.Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras(separadas por ’ ’), 
# y sobre ella, informe la cantidad de palabras en las que se encuentra el string. No importan las mayúsculas y minúsculas.
# Nota:este ejercicio se deberá resolver en el curso online y probar su ejecución con casos provistos en el mismo.

frase = input("ingre frase").lower()
string = input("ingre palabra").lower()

frase = frase.split()
cant = 0
for palabra in frase:
    if palabra == string:
        cant += 1

print (cant)

