from datetime import datetime
from datetime import timedelta

def diaSiguiente(fechaCadena):
    ahora = datetime.strptime(fechaCadena, '%d-%m-%Y')
    td = timedelta(1)
    print("El dia siguiente es: ", ahora + td)

fechaCadena = "02-04-2020"
diaSiguiente(fechaCadena)