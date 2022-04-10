# 11. Con la información de los archivos de texto que se encuentran disponibles en el curso:

# • nombres_1
# • nombres_2

# • Indique los nombres que se encuentran en ambos. Nota: pruebe utilizando list comprehension.
# • Genere tres variables con la lista de notas y nombres que se incluyen en los archivos: nombres_1, eval1.txt y eval2.txt e imprima con formato los nombres de los estudiantes con las
# correspondientes nota y la suma de ambas como se ve en la imagen

archivo = open ("eval1.txt","r")
notas1 = archivo.read().split(",")
archivo.close()
notas1 = list(map(int,notas1))  #genero una lista de enteros haciendo uso de la funcion map() e int().

archivo = open ("eval2.txt","r")
notas2 = archivo.read().split(",")
archivo.close()
notas2 = list(map(int,notas2))  #genero una lista de enteros haciendo uso de la funcion map() e int().

archivo = open ("nombres_1.txt","r")
nombres1 = archivo.read().lower().split("\n")
archivo.close()


archivo = open ("nombres_2.txt","r")
nombres2 = archivo.read().lower().split("\n")
archivo.close()

for i,nom in enumerate(nombres1):    #recorro la lista de nombres y reemplazo las comas por nada.
    nombres1[i] = nom.replace(",","")
for i,nom in enumerate(nombres2):    #recorro la lista de nombres y reemplazo las comas por nada.
    nombres2[i] = nom.replace(",","")

#estos 2 for estan raros, si lo hago en los fores anteriores no me saca la coma
for i,nom in enumerate(nombres1):    
    nombres1[i] = nom.replace("'","")
for i,nom in enumerate(nombres2):    
    nombres2[i] = nom.replace("'","")

print (nombres1)

#se genera la lista por comprension. 
nom_compartidos = [set(nombres1) & set(nombres2)]


#parte b 
print ("  Nombre",end="       ")
print ("Eval1",end="       ")
print (" Eval2",end="       ")
print ("  Total")

for i in range(len(nombres1)):
    print (i, end="")
    cant_espacios = (6-len(nombres1[i])) + 9
    if (i < 10) or (notas1[i]<10):
        cant_espacios = cant_espacios + 1
    if (notas2[i]<10):
        cant_espacios = cant_espacios + 1
    cad_espa = " "*cant_espacios
    print (f"{nombres1[i]}",end=cad_espa)
    print (f"{notas1[i]}",end="           ")
    print (f"{notas2[i]}",end="           ")
    print (f"{notas2[i]+notas1[i]}")
