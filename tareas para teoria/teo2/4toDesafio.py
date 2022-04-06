# Queremos implementar una función que dada una colección con datos de usuarios de un
# determinado juego (por ejemplo nombre, nivel y puntaje), queremos retornar esta colección
# ordenada de acuerdo al nombre.

#res profesora: 
def ordenoColeccion (usuarios):
    return sorted(usuarios, key = lambda usuarios: usuarios[0].lower())

usuarios = [("Pepe", 10, 100),("aartin", 12, 14),("tinuti", 0, 10)]

print (ordenoColeccion(usuarios))