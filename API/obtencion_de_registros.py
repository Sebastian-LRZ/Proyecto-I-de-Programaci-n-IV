from API import consulta as consulta


#  Función que obtiene los datos solicitados


def obtener_registros(departamento_a_consultar=None,
                      municipio_a_consultar=None,
                      cultivo_a_consultar=None,
                      cantidad_de_registros=None):

    results = consulta.obtener_cliente().get("ch4u-f3i5",
                                             limit=cantidad_de_registros,
                                             select="departamento, municipio, "
                                                    "cultivo, topografia, "
                                                    "ph_agua_suelo_2_5_1_0, "
                                                    "f_sforo_p_bray_ii_mg_kg, "
                                                    "potasio_k_intercambiable_cmol_kg",
                                             departamento=departamento_a_consultar,
                                             municipio=municipio_a_consultar,
                                             cultivo=cultivo_a_consultar)

    return results
