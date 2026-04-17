def grades():
    """
    Ejercicio 5 - Clasificar Notas

    Leer una nota (0-10) mediante input(). Clasificar la nota e imprimir:
    - "Excelente" si está entre 9 y 10
    - "Bueno" si está entre 7 y 8
    - "Regular" si está entre 5 y 6
    - "Insuficiente" si está entre 0 y 4

    Ejemplo:
        Para la entrada "9", la salida esperada es:
        Excelente

        Para la entrada "6", la salida esperada es:
        Regular

        Para la entrada "3", la salida esperada es:
        Insuficiente
    """
    a = float(input())

    if 10 >= a >= 9:
        print("Excelente")
    elif 8 >= a >= 7:
        print("Bueno")
    elif 6 >= a >= 5:
        print("Regular")
    elif 4 >= a >= 0:
        print("Insuficiente")
