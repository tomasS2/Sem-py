# x = 12
# a = 13
# def funcion(a):
#     #global x ## con esta linea se trabaja sobre la variable global
#     x = 2
#     a = 10
# funcion(a)
# print(a)
# print(x)





# def uno():
#     def uno_uno():
#         print("uno_uno")
#     def uno_dos():
#         print("uno_ddos")

#     print("uno")
#     uno_uno()

# def dos():
#     print("dos")
#     uno_dos() ##este no se hace porque esta funcion es local a la funcion "uno()"". Si solamente se invoca a la funcion "uno()", y no a "dos()", no va a dar error porque python es un lenguaje interpretado (se va a dar cuenta del error a medida que ejecute lo que se le pide, no se compila previamente.)
# uno()





# x = 0
# def uno():
    
#     x = 1
#     def uno_uno():
#         nonlocal x ##trabaja sobre la que tiene inmediatamente arriba
#         #global x   ##trabaja sobre la global del pp.
#         x = 2
        
#         def uno_uno_uno():
#            global x 
#            x = 3 
#            print(f"En uno_uno_uno: {x}")
           
#         uno_uno_uno()
#         print(f"En uno_uno: {x}")
#     uno_uno()
#     print(f"En uno: {x}")
# uno()
# print(f"En ppal: {x}")

