# Usando expresiones lambda escribir una función que permita codificar una
# frase según el siguiente algoritmo:
# encripto("a") --> "b"
# encripto("ABC") --> "BCD"
# encripto("Rock2021") --> "Spdl3132"
#cifrado cesar



 

def encripto(cadena):
    return list(map(lambda elem: chr(ord(elem)+1),cadena))
       
    

cadena = input("Ingrese expresion: ")
encriptacion = (encripto(cadena))
encriptacion = " ". join(encriptacion)
print (encriptacion)