#4. Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que
# deben cumplir y recomendaciones de escritura:
# • título: 10 palabras como máximo
# • cada oración del resumen:
#   – hasta 12 palabras: fácil de leer
#   – entre 13-17 palabras: aceptable para leer
#   – entre 18-25 palabras: difícil de leer
#    – mas de 25 palabras: muy difícil
# Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones tiene de cada categoría. El formato estándar 
# en que recibe el string tiene la siguiente forma:(texto en la variable "evaluar")



# En este ejemplo debería informar:
# • titulo está ok
# • Cantidad de oraciones fáciles de leer: 1, aceptables para leer: 2, dificil de leer: 1, muy dificil
# de leer: 2
# Notas: * investigue Pattern Matching para una solución simplificada. * ¿cuántas variables utilizó
# para guardar la cantidad de cada categoría, se podría usar alguna estructura? 

evaluar = """título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
""" 
titulo = evaluar[:evaluar.index("resumen:")]
resumen = evaluar[evaluar.index("resumen:")+len("resumen: "):]
titulo_lista = titulo.split()

if (len(titulo_lista[titulo_lista.index("título:")+1:]))<=(10):
    print ("El titulo cumple")
else:   
    print ("El titulo no cumple")
contador = 0
diccio_oraciones = {"Facil de leer": 0,"Aceptable para leer": 0,"Difícil de leer": 0,"Muy difícil de leer": 0}


#se podria hacer en un modulo que reciba el resumen.
"""
se itera sobre las oraciones que fueron separadas por puntos.
"""
resumen_lista = resumen.split(".")
for oracion in resumen_lista:
    len_oracion = len(oracion.split())
    if oracion != "\n":
        match len_oracion:
            case len_oracion if (len_oracion <= 12):
                diccio_oraciones["Facil de leer"] += 1
            case len_oracion if (len_oracion <= 17):
                diccio_oraciones["Aceptable para leer"] += 1
            case len_oracion if (len_oracion <= 25):
                diccio_oraciones["Difícil de leer"] += 1
            case len_oracion if (len_oracion > 25):
                diccio_oraciones["Muy difícil de leer"] += 1
    
print (f"Oraciones: {diccio_oraciones}")



# for elem in resumen_lista:
#     contador += 1
#     if "." in elem:
#         match contador:
            # case contador if (len_oracion <= 12):
            #     diccio_oraciones["Facil de leer"]+= 1
            # case contador if (len_oracion<=17):
            #     diccio_oraciones["Aceptable para leer"]+= 1
            # case contador if (len_oracion<=25):
            #     diccio_oraciones["Difícil de leer"]+= 1
            # case contador if (len_oracion>25):
            #     diccio_oraciones["Muy difícil de leer"]+= 1
          #contador=0
