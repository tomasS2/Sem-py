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

res = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]

for x, fila in enumerate(mapa):
    for y, elem in enumerate(fila):

        if (elem == "-"):

            #caso que este el guion entre espacios.
            if (x > 0) and (y > 0) and (x < len(mapa)-1) and (y < len(fila)-1):
                if (mapa[x+1][y+1] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x-1][y-1] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x][y+1] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x][y-1] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x+1][y] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x-1][y] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x-1][y+1] == "*"):
                    res[x][y] = res[x][y] + 1

                if (mapa[x+1][y-1] == "*"):
                    res[x][y] = res[x][y] + 1


            else:
                #caso que el guion este en la pos 'x' 0
                if (x == 0):
                    # caso que el guion este en la pos 'x' 0 e 'y' no este en la pos 0 ni len.
                    if (y > 0) and (y < len(fila)-1):
                        if (mapa[x][y-1] == "*"):
                            res[x][y] = res[x][y] + 1
                        if (mapa[x+1][y-1] == "*"):
                            res[x][y] = res[x][y] + 1                  
                        if (mapa[x][y+1] == "*"):
                            res[x][y] = res[x][y] + 1
                        if (mapa[x+1][y] == "*"):
                            res[x][y] = res[x][y] + 1
                        if (mapa[x+1][y+1] == "*"):
                            res[x][y] = res[x][y] + 1
                    else:
                        # caso que el guion este en la pos 'x' 0 e 'y' este en la pos 0
                        if (y == 0):
                            if (mapa[x][y+1] == "*"):
                                res[x][y] = res[x][y] + 1
                            if (mapa[x+1][y] == "*"):
                                res[x][y] = res[x][y] + 1
                            if (mapa[x+1][y+1] == "*"):
                                res[x][y] = res[x][y] + 1
                        else:
                             # caso que el guion este en la pos 'x' 0 e 'y' este en la pos len
                            if (y == len(fila)-1):
                                if (mapa[x+1][y] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x][y-1] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x+1][y-1] == "*"):
                                    res[x][y] = res[x][y] + 1


                else:
                    #caso que el guion este en la pos 'x' len.
                    if (x == len(mapa)-1):
                        # caso que el guion este en la pos 'x' len e 'y' no este en la pos 0 ni len.
                        if (y > 0) and (y < len(fila)-1):
                            if (mapa[x][y-1] == "*"):
                                res[x][y] = res[x][y] + 1
                            if (mapa[x-1][y-1] == "*"):
                                res[x][y] = res[x][y] + 1
                            if (mapa[x][y+1] == "*"):
                                res[x][y] = res[x][y] + 1
                            if (mapa[x-1][y+1] == "*"):
                                res[x][y] = res[x][y] + 1

                        else:
                            # caso que el guion este en la pos 'x' len e 'y'  este en la pos 0.
                            if (y == 0):
                                if (mapa[x-1][y] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x][y+1] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x-1][y+1] == "*"):
                                    res[x][y] = res[x][y] + 1
                            else:
                                # caso que el guion este en la pos 'x' len e 'y' este en la pos len
                                if (y == len(fila)-1):
                                    if (mapa[x-1][y] == "*"):
                                        res[x][y] = res[x][y] + 1
                                    if (mapa[x][y-1] == "*"):
                                        res[x][y] = res[x][y] + 1
                                    if (mapa[x-1][y-1] == "*"):
                                        res[x][y] = res[x][y] + 1


                    ## CASO Y
                    else:
                    #caso que el guion este en la pos 'y' 0
                        if (y == 0):
                    # caso que el guion este en la pos 'y' 0 e 'x' no este en la pos 0 ni len.
                            if (x > 0) and (x < len(mapa)-1):
                                if (mapa[x+1][y] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x+1][y+1] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x-1][y+1] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x-1][y] == "*"):
                                    res[x][y] = res[x][y] + 1
                        else:
                            if (y == len(fila)-1):
                                if (mapa[x+1][y] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x+1][y-1] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x-1][y-1] == "*"):
                                    res[x][y] = res[x][y] + 1
                                if (mapa[x-1][y] == "*"):
                                    res[x][y] = res[x][y] + 1
        else:
            res[x][y] = "*"
# for x, fila in enumerate(mapa):
#     for y, elem in enumerate(fila):
#         if x == 0:
#             res[x][y] =  res[x][y] +1



print (res)