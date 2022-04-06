"""
Quiz 8.
Realizado por Juleisy Porras Díaz
"""

def Euclides(x,y):
    """
    Función recursiva que calcula el mcd entre dos valores.

    Entradas y restricciones:
    - x: número entero positivo
    - y: número entero positivo

    Salidas:
    - MCD entre los dos valores
    """
    
    if type(x) != int or type(y) != int or x < 0 or y < 0:
        raise Exception("x, y deben ser números enteros positivos.")
    return EuclidesAux(x,y)

def EuclidesAux(x,y):
    """
    Función auxiliar de Euclides(x,y)
    """
    
    if y == 0:
        return x
    else:
        return EuclidesAux(y, x % y)
