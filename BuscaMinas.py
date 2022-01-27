"""
#######################################################################################
#  02/01/2022 15:39                                                                   #
#  Ramón Panadero Dobarro                                                             #
#  DAW_D 1º                                                                           #
#  Busca minas V0.0 alpha                                                             #
#######################################################################################
"""
import random


def data_input():
    DATOS_CORRECTOS = False
    data = 0
    MINIMO = 3
    MAXIMO = 10
    data = int(input())

    return data


def generar_tablero():
    TABLERO_CORRECTO = False
    MINIMO = 3
    MAXIMO = 10
    eje_x = 0
    eje_y = 0
    contador = 0
    contador1 = 0
    tablero = []
    print("Introduce el ancho: ", end="")
    eje_x = data_input()
    print("Introduce el alto: ", end="")
    eje_y = data_input()
    while TABLERO_CORRECTO == False:
        if eje_x < MINIMO or eje_y < MINIMO:
            print("Introduce el ancho: ", end="")
            eje_x = data_input()
            print("Introduce el alto: ", end="")
            eje_y = data_input()
        elif eje_x > MAXIMO or eje_y > MAXIMO:
            print("Introduce el ancho: ", end="")
            eje_x = data_input()
            print("Introduce el alto: ", end="")
            eje_y = data_input()
        elif eje_x < MINIMO or eje_y > MAXIMO:
            print("Introduce el ancho: ", end="")
            eje_x = data_input()
            print("Introduce el alto: ", end="")
            eje_y = data_input()
        elif eje_x > MAXIMO or eje_y < MINIMO:
            print("Introduce el ancho: ", end="")
            eje_x = data_input()
            print("Introduce el alto: ", end="")
            eje_y = data_input()
        else:
            TABLERO_CORRECTO = True

    print(f"{eje_x}, {eje_y}") # Borrar
    tablero = [["x " for x in range(eje_x)] for y in range(eje_y)]

    return tablero, eje_x, eje_y


def mostar_tablero(tablero_puro, eje_x, eje_y):
    print(" ", end=" ")
    for _ in range(eje_x):
        print(_ + 1, end=" ")
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
    mina_grafica = "m "
    random_x = 0
    random_y = 0
    print("\n" * 20)
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
    porcentaje_de_minas = 0.10

    catidad_de_minas = 0
    catidad_de_minas = round(porcentaje_de_minas * casillas)
    return catidad_de_minas


def comprobar_datos( tablero_con_minas, eje_x, eje_y, vida, minas):
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
    casillas = 0
    vida = 0
    verdadero_faslo = True
    tablero = []

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
