# 5_b. Retomamos el código visto en la teoría, que informaba si los caracteres “@” o “!” formaban
# parte de una palabra ingresada

#simplificar:
# cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no ,→contener los símbolos:@ y !):")
# if len(cadena) > 10:
#     print("Ingresaste más de 10 carcateres")
# cant = 0
# for car in cadena:
#     if car == "@" or car == "!":
#         cant = cant + 1
# if cant >= 1:
#     print("Ingresaste alguno de estos símbolos: @ o !" )
# else:
#     print("Clave válida")



cadena = input("Ingresa la clave (debe tener menos de 10 caracteres y no ,→contener los símbolos:@ y !):")
caracter_invalido = False
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
if ("@" or "!") in cadena:
    print("ingresó un caracter inválido")
else:   
    print("clave valida")