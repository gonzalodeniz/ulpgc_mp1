# -*- coding: utf-8 -*-
''' Procedimientos de submatrices'''

import pymatriz.matriz

def _submatriz_esta_en_posicion(ma, mb, x, y):
    ''' Devuelve Verdadero si una submatriz esta en una posicion x, y'''

    # Comprueba que mb esta dentro de los margen de ma según la posición x,y
    if (mb.filas + x) > ma.filas:
        return False
    if (mb.columnas + y) > ma.columnas:
        return False

    # Compara cada elemento de la matriz b en matriz a y devuelve falso si son diferentes
    for i in range(mb.filas):
        for j in range(mb.columnas):
            if mb.get(i, j) != ma.get(x + i, y + j):
                return False

    # Si todos los elementos son iguales devuelve True
    return True


def _modificar_subconjunto(m, x0, y0, x1, y1, valor):
    ''' Modifica una submatriz de una matriz más grande con un valor
        Param:
            m - Matriz
            x0       - Posición X inicial donde comienza la submatriz
            y0       - Posición Y inicial donde comienza la submatriz
            x1       - Posición X final donde termina la submatriz
            y1       - Posición Y final donde termina la submatriz
            valor       - Valor por el que se modifica la submatriz
    '''
    alto = x1 - x0
    ancho = y1 - y0

    for i in range(alto):
        for j in range(ancho):
            m.set(x0 + i, y0 + j, valor)

def submatriz_esta_en(ma, mb):
    ''' Dada dos matrices enteras ma y mb, devuelve cuántas veces se halla contenidad la matriz mb en la ma.
        Las ocurrencias de la matriz B no puede solaparse'''
    marcado = pymatriz.matriz.Matriz(ma.filas, ma.columnas, False)
    contador = 0

    for i in range(ma.filas):
        for j in range(ma.columnas):
            if not marcado.get(i, j):
                if _submatriz_esta_en_posicion(ma, mb, i, j):
                    contador += 1
                    _modificar_subconjunto(marcado, i, j, i + mb.filas, j + mb.columnas, True)

    return contador
