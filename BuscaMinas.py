"""
Ramon panadero dobarro
DAW 1
31/01/2022
Busca minas V1.0
"""

import random


def data_input():
    # funcion que recoje los datos introduciodos por el ususario
    return int(input())


def tablero_valdio(eje_x, eje_y):
    # FunciÃ³n que comprueba que el tablero es valido
    MINIMO = 3
    MAXIMO = 10
    if eje_x < MINIMO or eje_y < MINIMO:
        return False
    elif eje_x > MAXIMO or eje_y > MAXIMO:
        return False
    elif eje_x < MINIMO or eje_y > MAXIMO:
        return False
    elif eje_x > MAXIMO or eje_y < MINIMO:
        return False
    else:
        return True


def generar_tablero():
    # FunciÃ³n que genera el tablero y comprueba que sea vÃ¡lido
    VEDADERO_FALSO = False
    TABLERO_CORRECTO = False

    eje_x = 0
    eje_y = 0
    tablero = []
    print("Introduce el ancho: ", end="")
    eje_x = data_input()
    print("Introduce el alto: ", end="")
    eje_y = data_input()
    # Parte que compruba si los datos son validos
    while TABLERO_CORRECTO == VEDADERO_FALSO:
        TABLERO_CORRECTO = tablero_valdio(eje_x, eje_y)
        if TABLERO_CORRECTO == VEDADERO_FALSO:
            print("No son datos correctos ")
            print("Introduce el ancho: ", end="")
            eje_x = data_input()
            print("Introduce el alto: ", end="")
            eje_y = data_input()

    tablero = [["x " for x in range(eje_x)] for y in range(eje_y)]

    return tablero, eje_x, eje_y


def mostar_tablero(tablero_puro, eje_x, eje_y):
    # Funcion que pinta el tablero correctamente
    print(" ", end=" ")
    for contador0 in range(eje_x):
        print(contador0 + 1, end=" ")
    print("")
    for contador in range(eje_y):
        print(contador + 1, end=" ")
        for contador1 in range(eje_x):
            if tablero_puro[contador][contador1] == "m ":
                print("x ", end="")
            else:
                print(f"{tablero_puro[contador][contador1]}", end="")
        print("")


def colocar_minas(minas, eje_x, eje_y, tablero_con_minas):
    # FunciÃ³n que coloca la mina en el tablero
    mina_grafica = "m "
    random_x = 0
    random_y = 0
    random_x = random.randrange(eje_x - 1)
    random_y = random.randrange(eje_y - 1)
    for _ in range(minas):
        if tablero_con_minas[random_x][random_y] == mina_grafica:
            while tablero_con_minas[random_x][random_y] == mina_grafica:
                random_x = random.randrange(eje_x)
                random_y = random.randrange(eje_y)
                tablero_con_minas[random_x][random_y] = mina_grafica
        else:
            tablero_con_minas[random_x][random_y] = mina_grafica
        random_x = random.randrange(eje_x)
        random_y = random.randrange(eje_y)
    return tablero_con_minas


def generar_minas(casillas):
    # Funcion que calcula la cantidad de minas para el juego
    porcentaje_de_minas = 0.10

    catidad_de_minas = 0
    catidad_de_minas = round(porcentaje_de_minas * casillas)
    return catidad_de_minas


def comprobar_datos(tablero_con_minas, eje_x, eje_y, vida, minas):
    # Funcion que comprueba si las cordenadas metidas por el juador son correctas
    dato_x = 0
    dato_y = 0
    mina = "m "

    print("Introduce el eje y:", end="")
    dato_x = data_input() - 1
    print("Introduce el eje x:", end="")
    dato_y = data_input() - 1
    if dato_x in range(eje_x) and dato_y in range(eje_y):
        if tablero_con_minas[dato_x][dato_y] == mina:
            tablero_con_minas[dato_x][dato_y] = "V "
            minas -= 1
            return tablero_con_minas, vida, minas
        else:
            vida -= 1
            print("Una vida menos")
            print(f"cantidad de vidas {vida}")
            return tablero_con_minas, vida, minas
    else:
        print("Sos re bobo")
    return tablero_con_minas, vida


def jugar_buscaminas():
    # FunciÃ³n que inicializa el juego
    eje_x = 0
    eje_y = 0
    casillas = 0
    vida = 0
    minas = 0
    tablero = []
    tablero_con_minas = []

    tablero, eje_x, eje_y = generar_tablero()
    casillas = eje_x * eje_y
    minas = generar_minas(casillas)
    tablero_con_minas = colocar_minas(minas, eje_x, eje_y, tablero)
    mostar_tablero(tablero_con_minas, eje_x, eje_y)
    vida = minas * 2
    print(f"cantidad de vidas {vida}")
    while vida != 0 and minas != 0:
        tablero, vida, minas = comprobar_datos(tablero_con_minas, eje_x, eje_y, vida, minas)
        mostar_tablero(tablero, eje_x, eje_y)
    print("Fin del juego")


jugar_buscaminas()
