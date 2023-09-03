from UI import salida_y_entrada_pantallas as salida_entrada
from API import obtencion_de_registros as obtener_datos
from API import estudio_de_datos as analisis


def main():
    departamento_a_consultar, municipio_a_consultar, cultivo_a_consultar, cantidad_de_registros = \
        salida_entrada.pedir_datos()

    registro_obtenido = obtener_datos.obtener_registros(departamento_a_consultar, municipio_a_consultar,
                                                        cultivo_a_consultar, cantidad_de_registros)

    registro_total = analisis.obtener_dataframe(registro_obtenido)

    salida_entrada.mostrar_registros(registro_total)


if __name__ == "__main__":
    main()
