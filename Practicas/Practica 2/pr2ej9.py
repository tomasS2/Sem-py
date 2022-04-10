# 9. La idea es tratar de programar una de las partes principales del juego “Buscaminas”. La idea
# es que dado una estructura que dice qué celdas tienen minas y qué celdas no las tienen, como
# la siguiente:

# [
# '-*-*-',
# '--*--',
# '----*',
# '*----',
# ]


# Generar otra que indique en las celdas vacías la cantidad de bombas que la rodean, para el ejemplo
# anterior, sería:

# [
# '1*3*1',
# '12*32',
# '1212*',
# '*1011',
# ]

# Nota: Defina al menos una función en el código (si hay mas mejor) y documente las mismas con
# docstring que es lo que hacen.



mapa = ['-*-*-','--*--','----*','*----']

res = ["asdfg","qwert","yuiop","zxcvb"]

for x, fila in enumerate(mapa):
    for y, elem in enumerate(fila):

        if (elem == "-"):

            if (x > 0) and (y > 0) and (x < len(mapa)) and (y < len(fila)):

                if (mapa[x+1][y+1] == "*"):
                    print (res[x][y])

                if (mapa[x-1][y-1] == "*"):
                    print (res[x][y])

                if (mapa[x][y+1] == "*"):
                    print (res[x][y])

                if (mapa[x][y-1] == "*"):
                    print (res[x][y])

                if (mapa[x+1][y] == "*"):
                    print (res[x][y])

                if (mapa[x-1][y] == "*"):
                    print (res[x][y])

                if (mapa[x-1][y+1] == "*"):
                    print (res[x][y])
                    
                if (mapa[x+1][y-1] == "*"):
                    print (res[x][y])
                

            else:
                if (x == 0):
                    if (y > 0) and (y < len(fila)):
                        if (mapa[x][y-1] == "*"):
                            print (res[x][y])
                        if (mapa[x+1][y-1] == "*"):
                            print (res[x][y])
                        if (mapa[x][y+1] == "*"):
                            print (res[x][y])
                        if (mapa[x+1][y+1] == "*"):
                            print (res[x][y])
                        














            # if mapa[x][y+1] == "*":
            #     res[x][y] =1

            # if mapa[x-1][y] == "*":
            #     res[x][y] =1

            # if mapa[x+1][y] == "*":
            #     res[x][y] =1

            # if mapa[x+1][y+1] == "*":
            #     res[x][y] =1

            # if mapa[x-1][y-1] == "*":
            #     res[x][y] =res[x][y]+ 1
                
#         else:   
#             res[][] = "*"
                

