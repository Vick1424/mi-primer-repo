def duplicar(lista):
    return [x * 2 for x in lista]


def maximo(lista):
    if len(lista) == 0:
        return None
    return max(lista)


def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def principal():
    listas = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [-5, 0, 5, 10],
    ]

    for indice, lista in enumerate(listas, start=1):
        print(f"\nLista {indice}: {lista}")
        print("Doble:", duplicar(lista))
        print("Máximo:", maximo(lista))
        print("Promedio:", promedio(lista))


if __name__ == "__main__":
    principal()
