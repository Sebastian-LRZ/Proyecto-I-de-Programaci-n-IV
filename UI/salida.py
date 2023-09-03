from tabulate import tabulate


def mostrar_registros(registro_lista):
    print(tabulate(registro_lista, headers='keys', tablefmt="simple"))
