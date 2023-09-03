from UI import salida as presentar_datos
from UI import entrada as ingresar_datos
from API import obtencion_de_registros as obtener_datos
from API import estudio_de_datos as analisis


def main():

    variables_edaficas = ['ph_agua_suelo_2_5_1_0',
                          'f_sforo_p_bray_ii_mg_kg',
                          'potasio_k_intercambiable_cmol_kg']

    #  elementos necesarios para obtener los registros
    departamento_a_consultar, municipio_a_consultar, cultivo_a_consultar, cantidad_de_registros = \
        ingresar_datos.pedir_datos()

    #  obtener los registros con los datos ingresados
    registro_obtenido = obtener_datos.obtener_registros(departamento_a_consultar, municipio_a_consultar,
                                                        cultivo_a_consultar, cantidad_de_registros)

    #  convertir los registros con aquellos datos analizados
    registro_total = analisis.obtener_registro_final(registro_obtenido, variables_edaficas)

    #  presentar los registros con su analisis
    presentar_datos.mostrar_registros(registro_total)


if __name__ == "__main__":
    main()
