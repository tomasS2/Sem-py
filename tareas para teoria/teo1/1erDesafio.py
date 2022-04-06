#modificar este cod.
# for i in range(4):
#     cadena = input("Ingresá una palabra")
#     if "r" in cadena:
#         print("TIENE R")
#     else:
#         print("NO TIENE R")



#modificacion.
for i in range(4):
    cadena = input("Ingresá una palabra ")
    #otra solucion: print("TIENE R" if "r" in cadena else "NO TIENE R")
    str= "tiene r" if "r" in cadena else "no tiene r"
    print(str)
