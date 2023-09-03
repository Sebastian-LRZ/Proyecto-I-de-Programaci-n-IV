import pandas as pd


def convertir_a_numerico(registro, columnas_variables_edaficas):

    # Convertir las columnas especificadas de cadenas de texto a numéricos
    for columna in columnas_variables_edaficas:

        # 'coerce' convierte valores no numéricos a NaN
        registro[columna] = pd.to_numeric(registro[columna], errors='coerce')

    return registro
