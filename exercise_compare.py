def compare():
    """
    Ejercicio 4 - Comparar Dos Números

    Leer dos números enteros mediante input(). Compararlos e imprimir si el primero
    es mayor, menor o igual al segundo.

    Ejemplo:
        Para las entradas "10" y "5", la salida esperada es:
        10 es mayor que 5

        Para las entradas "3" y "8", la salida esperada es:
        3 es menor que 8

        Para las entradas "7" y "7", la salida esperada es:
        7 es igual a 7
    """
    a = int(input())
    b = int(input())

    if a == b:
        print(f"{a} es igual a {b}")
    elif a > b:
        print(f"{a} es mayor a {b}")
    elif b > a:
        print(f"{a} es menor a {b}")