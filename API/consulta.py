from sodapy import Socrata

#  Unauthenticated client only works with public data sets. Note 'None'
#  in place of application token, and no username or password:


def obtener_cliente():
    # obtener accesso a los datos publicos en 'www.datos.gov.co'
    client = Socrata('www.datos.gov.co', None)
    return client
