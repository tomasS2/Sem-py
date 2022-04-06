# 8. Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada
# la siguiente tabla de valores del juego Scrabble:
# A, E, I, O, U, L, N, R, S, T          1
# D, G                                  2
# B, C, M, P                            3
# F, H, V, W, Y                         4
# K                                     5
# J, X                                  8
# Q, Z                                  10



def valor (pal,valores_juego):
    """calcula el valor total, basandose en el juego scrabble, de una palabra"""
    contador = 0
    for letra in pal:
        for clave in valores_juego:
            if letra in clave:
                contador = contador + valores_juego[clave]
    return contador





valores_juego = {"A E I O U L N R S T": 1, "D G" : 2, "B C M P":3, "F H V W Y":4, "K":5, "J X":8, "Q Z":10}
palabra = input("Ingrese una palabra: ")
print (f"El valor de la palabra '{palabra}' segun la tabla de valores del juego Scrabble es: ",valor(palabra.upper(),valores_juego))



