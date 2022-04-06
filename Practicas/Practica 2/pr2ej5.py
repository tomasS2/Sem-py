# 5. Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
# veces que se encuentra el string en la frase. No distingir entre mayúsculas y minúsculas.

from itertools import count

frase = input("Ingrese una frase ").lower()
str_buscar = input("Ingrese una palabra ").lower()
print (f"La palabra {str_buscar} se encuentra {frase.count(str_buscar)} veces en la frase '{frase}'")