# Queremos escribir una función que imprima sus argumentos agregando de
# qué tipo son.

def indicarType (*args):#args es una tupla que representa a los parametros pasados
    for elem in args:
        print(type(elem))


indicarType(1,[1,2],"f")







