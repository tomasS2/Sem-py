#3. Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string

#print(texto.split()[0].startswith(caracter))



texto = input ("Ingrese un texto: ")
letra = input("Ingrese una letra: ")
lista_texto = texto.lower().split()

if letra.isalpha():
    for elem in lista_texto:    
        if elem.startswith(letra):
            print(elem)
else:
    print("no ingreso una letra")



