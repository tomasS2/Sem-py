# Queremos implementar una función que dada una cadena de texto, retorne las palabras que
# contiene en orden alfabético.

#ejemplos de la profesora:
 
# Una posible solución
# def ordeno1(cadena="ss"):
#     """ Implementación usando sort"""
#     lista = cadena.split()
#     lista.sort(key=str.lower)##la ordena por orden alfabetico en minuscula.
#     #lista.sort() ##no la ordena bien porque si hay una palabra en mayus la pone primera, por mas que no cumpla con el orden alfabetico
#     return lista

# print(ordeno1("Hoy puede ser un gran día. "))

# Otra posible solución

def ordeno2(cadena):
    """ Implementación usando sorted"""
    lista = cadena.split()
    return sorted(lista, key=str.lower)
print(ordeno2("Hoy puede ser un gran día. "))
