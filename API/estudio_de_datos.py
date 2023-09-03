from API import transformacion_de_datos as corregir
import pandas as pd


def obtener_dataframe(dato):
    dataframe = pd.DataFrame.from_records(dato)
    return dataframe


def agregar_mediana(registros, columnas_especificas):

    # se convierten los datos especificados del registro a numerico para procesarlos
    mediana = corregir.convertir_a_numerico(obtener_dataframe(registros), columnas_especificas)

    # se obtiene la mediana de estos datos; 'skipna=True' se salta los valores faltantes
    mediana['mediana_de_variables_edaficas (ph, fosforo (p), potasio (k))'] = (
        mediana[columnas_especificas].median(axis=1, skipna=True))

    return mediana


def eliminar_columnas(registros, columnas_especificas):

    # elimina las columnas de datos 'columnas_especificas'
    registros = registros.drop(columnas_especificas, axis=1).to_dict(orient='list')

    return registros


def obtener_registro_final(registros, variables_edaficas):

    # obtener el registro con la mediana de cada fila
    registro_mediana = agregar_mediana(registros, variables_edaficas)

    # eliminar las columnas de las variables edaficas
    registro_final = eliminar_columnas(registro_mediana, variables_edaficas)

    return registro_final
