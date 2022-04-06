# 7. Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
# misma es un Heterograma. Un Heterograma es una palabra o frase que no tiene ninguna letra repetida entre sus caracteres.

# Tener en cuenta 
# - Lo que no se puede repetir en la frase son sólo aquellos caracteres que sean
# letras. 
# - No se distingue entre mayúsculas y minúsculas, es decir si en la frase o palabra tenemos
# la letra “T” y la letra “t” la misma NO será un Heterograma. 
# - Para simplificar el ejercicio vamos a tomar como que las letras con tilde y sin tilde son distintas
# ya que Python las diferencia



def heterograma (frase):
    """ 
    crea un conjunto a partir de una frase. Compara las 2 long.
    """
    conjunto_frase = set(frase)
    
    if len(conjunto_frase) == len(frase):
        return "Es un heterograma"
    else:
        return "No es un heterograma"
    

frase = input("ingrese una frase o palabra: ")

print (heterograma(frase))