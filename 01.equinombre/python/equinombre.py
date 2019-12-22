"""
Dada una variable ristra la cual representa el nombre y los dos apellidos de una persona, realice una función llamada
"Equinombre" que obtenga y devuelva un nombre equivalente, en la forma de segundo apellido seguido de las iniciales
del nombre y primer apellido.
"""


def equinombre(fullname):
    """
        :param fullname:    Nombre Apellido1 Apellido2
        :return:            Apellido2 Inicial_Nombre Inicial_Apellido1
    """
    fullname_list = fullname.split()
    cont_palabras = len(fullname_list)
    if cont_palabras >= 3:
        nombre_equivalente = fullname_list[2] + ' ' + fullname_list[0][0] + ' ' + fullname_list[1][0]
    elif cont_palabras == 2:
        nombre_equivalente = fullname_list[1] + ' ' + fullname_list[0][0]
    elif cont_palabras == 1:
        nombre_equivalente = fullname_list[0]
    else:
        nombre_equivalente = ''

    return nombre_equivalente


def main():
    fullname = "Pepito Grillo Conejo"
    print(fullname)
    nombre_equivalente = equinombre(fullname)
    print(nombre_equivalente)


if __name__ == "__main__":
    main()
