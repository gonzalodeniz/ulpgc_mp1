# -*- coding: utf-8 -*-
"""
Desarrolle un procedimiento para obtener el elemento máximo de una matriz de ristras y su posición.
"""

from pymatriz.matriz import *


def maximo(matriz):
    ''' Devuelve el elemento máximo y su posición de una matriz
        param:
            matriz - Objeto de tipo Matriz
        return:
            elemento_máximo, posición
     '''
    max = 0
    pos = None

    for i in range(matriz.filas):
        for j in range(matriz.columnas):
            if matriz.get(i, j) > max:
                max = matriz.get(i,j)
                pos = (i, j)
    return max, pos



def main():
    # Crea una matriz aleatoria de 10x10 y la imprime por consola
    FILAS = 10
    COLUMNAS = 10
    VALOR_MAXIMO = 99
    m = Matriz.random(FILAS, COLUMNAS, VALOR_MAXIMO)
    m.print()

    # Devuelve el elemento máximo y su posición de una matriz
    max, pos = maximo(m)
    print('Valor máximo: ' + str(max))
    print('Posición: ' + str(pos))


if __name__ == "__main__":
    main()