# Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
# aquellas que empiecen y terminen con la misma letra.

palabra=input("ingrese una palabra: ")
while (palabra != "fin"):
    if (palabra.endswith(palabra[0])):
        print(palabra)
    palabra=input("ingrese una palabra: ")
