# -*- coding: utf-8 -*-

'''
Clase Matriz que contiene funciones para operar con matrices
'''

import random
import pymatriz.matriz_ordenar as ordenacion
import pymatriz.matriz_submatrices as submatriz

class Matriz:
    m = None        # Matriz
    filas = 0       # Numero de filas
    columnas = 0    # Número de columnas

    def __init__(self, filas, columnas, valor=None):
        ''' Crea matriz indicando número de filas y columnas de la matriz e inicializando con un valor.
            Ej: Matriz(3,5,0)   # Crea una matriz de 3x5 y lo inicializa todo a cero
        '''

        assert type(filas) == int,      "Se esperaba el número de 'filas' de la matriz. Debe ser un entero."
        assert type(columnas) == int,   "Se esperaba el número de 'columnas' de la matriz. Debe ser un entero."

        self.m = []
        self.filas = filas
        self.columnas = columnas

        # Inicializa la matriz
        for x in range(filas):
            self.m.append([])
            for y in range(columnas):
                self.m[x].append(valor)

    @classmethod
    def de_listas(cls, matriz_lists):
        ''' Devuelve una instancia con la matriz de listas [[],[]] que se ha pasado por parámetros. '''

        assert type(matriz_lists) == list, " Se esperaba una matriz de listas, ej: [[1,2], [3,4]]"

        filas = len(matriz_lists)
        columnas = len(matriz_lists[0])
        matriz = cls(filas, columnas)
        matriz.m = list(matriz_lists)
        return matriz

    @classmethod
    def random(cls, filas, columnas, random_max=9):
        ''' Crea matriz de tamaño "filas" x "columnas" con valores aleatorios.
            random_max es el valor máximo en el que se generará los números aleatorios. Por defecto es 9,
            significa que los valores aleatorios serán del 0 al 9.

            param:
                filas - número de filas
                columnas - número de columnas
                random_max - Número maximo de los valores aleatorios
        '''

        assert type(filas) == int,      "Se esperaba el número de 'filas' de la matriz. Debe ser un entero."
        assert type(columnas) == int,   "Se esperaba el número de 'columnas' de la matriz. Debe ser un entero."
        assert type(random_max) == int, "Se esperaba el número de 'random_max' de la matriz. Debe ser un entero."
        assert random_max >= 0, "Se esperaba el número de 'random_max' de la matriz. Debe ser un entero positivo."

        matriz_list = []
        matriz = cls(filas, columnas)   # Inicializa la matriz

        # Genera una lista de listas de valores aleatorios
        for i in range(0, filas):
            fila = []
            for j in range(0, columnas):
                fila.append(random.randint(0, random_max))
            matriz_list.append(fila)

        # Copia la matriz (lista de listas) en el objeto creado con 'cls'
        matriz.m = list(matriz_list)
        return matriz

    def print(self):
        ''' Imprime la matriz'''
        for x in range(self.filas):
            print(str(self.m[x]))

    def get(self, x, y):
        ''' Obtiene el valor de una coordenada'''
        assert type(x) == int, "Se una fila. Debe ser un entero."
        assert type(y) == int, "Se esperaba una columna. Debe ser un entero."
        assert x < self.filas, "Error, 'x' supera el número de filas."
        assert y < self.columnas, "Error, 'y' supera el número de columnas."

        fila = self.m[x]
        return fila[y]

    def set(self, x, y, valor=None):
        ''' Modifica el valor de la matriz'''
        assert type(x) == int, "Se una fila. Debe ser un entero."
        assert type(y) == int, "Se esperaba una columna. Debe ser un entero."
        assert x < self.filas, "Error, 'x' supera el número de filas."
        assert y < self.columnas, "Error, 'y' supera el número de columnas."

        fila = self.m[x]
        fila[y] = valor

    def copy(self):
        ''' Devuelve un clone del objeto actual '''
        return self.de_listas(self.m)

    # Métodos de ordenacion
    def get_ordena_extraccion_menor(self):
        ''' Devuelve una matriz ordenada en base a la columna 1 por el método de extracción del menor.
            Se van buscando las filas menores y se mueven a la matriz nueva de manera ordenada. Cada vez q se mueve
            una fila se elimina de la matriz original
        '''
        m_ordenada = ordenacion.ordena_extraccion_menor(self.m)
        return Matriz.de_listas(m_ordenada)

    def set_ordena_extraccion_menor(self):
        ''' Ordenada la matriz en base a la columna 1 por el método de extracción del menor.
            Se van buscando las filas menores y se mueven a la matriz nueva de manera ordenada. Cada vez q se mueve
            una fila se elimina de la matriz original
        '''
        m_ordenada = ordenacion.ordena_extraccion_menor(self.m)
        self.m = m_ordenada

    def get_ordena_por_intercambio(self):
        ''' Devuelve una matriz ordenada por el método de intercambio de filas
            Método de intercambio entre dos filas. Si la fila actual es mayor a la siguiente se intercambia.
            Se repite tantas veces hasta que no haya ninguna permutación.'''
        m_ordenada = ordenacion.ordena_por_intercambio(self.m)
        return Matriz.de_listas(m_ordenada)

    def set_ordena_por_intercambio(self):
        ''' Ordenada la matriz ordenada por intercambio de filas
            Método de intercambio entre dos filas. Si la fila actual es mayor a la siguiente se intercambia.
            Se repite tantas veces hasta que no haya ninguna permutación.
        '''
        m_ordenada = ordenacion.ordena_por_intercambio(self.m)
        self.m = m_ordenada

    # FRECUENCIAS Y REPETICIONES
    def get_frecuencia_valores(self):
        ''' Devuelve un diccionario con la frecuencia con que se repiten los valores de la matriz'''
        frecuencias = {}
        for fila in self.m:
            for num in fila:
                if num in frecuencias:
                    frecuencias[num] += 1
                else:
                    frecuencias[num] = 1
        return frecuencias

    def get_repetidos_x_cero(self):
        '''Dada una matriz conteniendo números enteros entre 1 y 100,
       escribir un algoritmo que detecte todos los número repetidos,
       reemplazándolos por ceros, e indique cuantos hay sin repetir.

       1 3 4        0 0 0
       2 1 4    =>  2 0 0  => 2 numeros sin repetir
       5 1 3        5 0 0

       return Matriz sin repetidos, numeros_sin_repetir
       '''

        # Contador de los valores no repetidos
        no_repetidos = 0

        # Crea una copia de la matriz para no modificar el original
        m = self.copy()

        # Obtiene la frecuencia de los elementos
        frecuencia = m.get_frecuencia_valores()

        # Recorre la matriz sustituyendo por ceros los repetidos
        for i in range(m.filas):
            for j in range(m.columnas):
                valor = m.get(i, j)
                if frecuencia[valor] > 1:
                    m.set(i, j, 0)
                else:
                    no_repetidos += 1

        # Devuelve la matriz sin repetidos y el numeo de valores no repetidos
        return m, no_repetidos


    def contador_submatriz(self, mb):
            ''' Dada dos matrices enteras ma y mb, devuelve cuántas veces se halla contenidad la matriz mb en la ma.
                Las ocurrencias de la matriz B no puede solaparse'''

            ma = self.copy()
            return submatriz.submatriz_esta_en(ma, mb)









