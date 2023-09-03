from sodapy import Socrata

#  Unauthenticated client only works with public data sets. Note 'None'
#  in place of application token, and no username or password:


def obtener_cliente():
    client = Socrata('www.datos.gov.co', None)
    return client
