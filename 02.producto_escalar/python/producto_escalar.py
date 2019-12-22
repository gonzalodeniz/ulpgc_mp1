# -*- coding: utf-8 -*-
"""
Desarrolle una función que calcule el producto escalar de dos vectores.
"""


def main():
    u = (3, 0, 0)  # X, Y, Z
    v = (5, 5, 0)  # X, Y, Z
    r = producto_escalar(u, v)
    print(r)


def producto_escalar(u, v):
    ''' El producto escalar de dos vectores se calcula con la siguiente ecuación:
            u x v = u1 * v1 + u2 * v2 + u3 * v3
        :param
            u y v - Tuplas de tres elementos que representa (x, y, z) de un vector
        :return
            Número real
    '''
    assert isinstance(u[0], int), "El vector de entrada no cumple el formato correcto"
    assert isinstance(u[1], int), "El vector de entrada no cumple el formato correcto"
    assert isinstance(u[2], int), "El vector de entrada no cumple el formato correcto"
    assert isinstance(v[0], int), "El vector de entrada no cumple el formato correcto"
    assert isinstance(v[1], int), "El vector de entrada no cumple el formato correcto"
    assert isinstance(v[2], int), "El vector de entrada no cumple el formato correcto"

    return u[0] * v[0] + u[1] * v[1] * u[2] * v[2]


if __name__ == "__main__":
    main()
