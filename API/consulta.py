from sodapy import Socrata


def obtener_cliente():
    # obtener accesso a los datos publicos en 'www.datos.gov.co'
    client = Socrata('www.datos.gov.co', None)
    return client
