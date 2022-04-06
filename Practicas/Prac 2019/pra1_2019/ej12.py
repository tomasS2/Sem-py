# 12.Dado el siguiente diccionario donde las claves son nombres de animales y los valores representan posiciones:
# anim={’Gato Montes’:2,’Yacare overo’:4,’Boa acuática’:5}
# Imprimir un string por cada animal de la estructura, reemplazando sus caracteres por el string’_ ’ 
# (inclusive los espacios en blanco) salvo el caracter correspondiente al valor del mismo
# .Ejemplo: Gato Montes tiene asociado el valor 2:
# _ _ t _ _ _ _ _ _ _ _
# 0 1 2 3 4 5 6 7 8 9 10


anim={'Gato Montes':2,'Yacare overo':4,'Boa acuática':5}

for animal in anim:
    num = anim[animal]
    x=0
    while x < len(animal):
        if num != x:
            print('_',end = "")
        else:
            print(x,end = "")
            
        x = x + 1
    print("")
    for i in range(len(animal)):
        print(i,end = "")
    print("")