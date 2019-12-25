# -*- coding: utf-8 -*-
''' Procedimientos de ordenación'''



def ordena_extraccion_menor(matriz):
    ''' Devuelve una matriz ordenada en base a la columna 1 por el método de extracción del menor.
        Se van buscando las filas menores y se mueven a la matriz nueva de manera ordenada. Cada vez q se mueve
        una fila se elimina de la matriz original
    '''
    matriz_ordenada = []
    n_filas = len(matriz)                   # Numero de filas
    filas_eliminadas = [False] * n_filas    # Lista del número de filas inicializado a False

    # Inicializa lista de filas eliminadas
    for i in range(0, n_filas):
        fila_menor = _extrae_fila_menor(matriz, filas_eliminadas)
        matriz_ordenada.append(fila_menor)

    return matriz_ordenada

def ordena_por_intercambio(matriz):
    '''Método de intercambio entre dos filas. Si la fila actual es mayor a la siguiente se intercambia.
    Se repite tantas veces hasta que no haya ninguna permutación.'''
    matriz = list(matriz)
    hay_intercambio = True
    while hay_intercambio:
        hay_intercambio = False
        for i in range(0, len(matriz)-1):
            if matriz[i] > matriz[i+1]:
                matriz = _intercambiar(matriz, i, i+1)
                hay_intercambio = True
    return matriz

def _intercambiar(matriz, pos1, pos2):
    ''' Devuelve la matriz con las posiciones pos1 y pos2 intercambiadas'''
    aux = matriz[pos1]
    matriz[pos1] = matriz[pos2]
    matriz[pos2] = aux
    return matriz

def _extrae_fila_menor(matriz, filas_eliminadas):
    ''' Extrae la fila menor de la matriz, teniendo en cuenta las filas eliminadas
        La fila es marcada como eliminada
    '''
    fila_menor = None
    pos_menor = None
    for pos, fila_eliminada in enumerate(filas_eliminadas):
        if not fila_eliminada:
            # La primera fila no eliminada siempre es la menor hasta que no se compara con otra fila
            if fila_menor is None:
                fila_menor = matriz[pos]
                pos_menor = pos
            else:
                # Compara la fila_menor con la siguiente de la matriz
                if fila_menor > matriz[pos]:
                    fila_menor = matriz[pos]
                    pos_menor = pos

    # Si se extrae una fila se marca como eliminada
    if fila_menor is not None:
        filas_eliminadas[pos_menor] = True

    return fila_menor