def pedir_datos():

    # 'str.upper()' convierte todas las letras de la cadena en mayúscula
    departamento_a_consultar = input("Que departamento desea consultar?\n>>").upper()
    municipio_a_consultar = input("Que municipio desea consultar?\n>>").upper()

    # 'str.capitalize()' convierte la primer letra de la cadena en mayuscula
    cultivo_a_consultar = input("Que cultivo desea consultar?\n>>").capitalize()

    cantidad_de_registros = int(input("Cuantos registros desea consultar? (MAX. 2000)\n>>"))

    return departamento_a_consultar, municipio_a_consultar, cultivo_a_consultar, cantidad_de_registros
