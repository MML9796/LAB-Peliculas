from datetime import date,datetime
from typing import List

def parser_date(cadena,formato="%d/%m/%Y"):
    return datetime.strptime(cadena, formato ).date()

def parser_cadena(cadena:str)->List[str]:
    lista=[]
    for e in cadena.split(","):
        lista.append(e)
    return lista
