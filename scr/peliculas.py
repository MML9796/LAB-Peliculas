import csv
from typing import NamedTuple,List,Optional,Dict,Set
from parsers import *
from collections import defaultdict

Pelicula = NamedTuple("Pelicula",[("fecha_estreno", date), ("titulo", str), ("director", str), ("generos",List[str]),
    ("duracion", int),("presupuesto", int),("recaudacion", int),("reparto", List[str])])

def lee_peliculas(fichero:csv)->List[Pelicula]:
    peliculas=[]
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f,delimiter=';')
        next(lector)
        for fecha_estreno,titulo,director,generos,duracion,presupuesto,recaudacion,reparto in lector:
            fecha_estreno=parser_date(fecha_estreno)
            generos=parser_cadena(generos)
            duracion=int(duracion)
            presupuesto=int(presupuesto)
            recaudacion=int(recaudacion)
            reparto=parser_cadena(reparto)
            peliculas.append(Pelicula(fecha_estreno,titulo,director,generos,duracion,presupuesto,recaudacion,reparto))
        return peliculas
    
def pelicula_mas_ganancias(peliculas:List[Pelicula],genero:Optional[str]=None)->[str,int]:
    dicc=defaultdict(int)
    for i in peliculas:
        if genero is None or genero in i.generos:
            dicc[i.titulo]=i.recaudacion-i.presupuesto
    return max(dicc.items(),key=lambda x:x[1])

def media_presupuesto_por_genero(peliculas:List[Pelicula])->Dict[str,int]:
    dicc=defaultdict(list)
    for i in peliculas:
        for generos in i.generos:
            dicc[generos].append(i.presupuesto)
    res={}
    for genero,pre in dicc.items():
        res[genero]=sum(pre)/len(pre)
    return res

def peliculas_por_actor(peliculas:List[Pelicula],fecha_ini:Optional[int]=None,fecha_fin:Optional[int]=None)->Dict[str,str]:
    dicc=defaultdict(int)
    for i in peliculas:
        if fecha_ini is None or fecha_fin is None or fecha_ini<=i.fecha_estreno.year<=fecha_fin:
            for actor in i.reparto:
                dicc[actor]+=1
    return dicc

def actores_mas_frecuentes(peliculas:List[Pelicula],n:int,fecha_ini:Optional[int]=None,fecha_fin:Optional[int]=None)->List[str]:
    dicc=peliculas_por_actor(peliculas,fecha_ini,fecha_fin)
    lista=sorted(dicc.items(),key=lambda x:x[1],reverse=True)[:3]
    return sorted(actor for actor,frecuencia in lista)

def recaudacion_total_por_año(peliculas:List[Pelicula],genero:Optional[Set[str]])->Dict[int,int]:
    dicc=defaultdict(int)
    for i in peliculas:
        if genero is None or len(genero.intersection(i.generos))>0:
            dicc[i.fecha_estreno.year]+=i.recaudacion
    return dicc

def incrementos_recaudacion_por_año(peliculas:List[Pelicula],genero:Optional[Set[str]])->List[int]:
    dicc=recaudacion_total_por_año(peliculas,genero)
    recaudacion=[recauda for fecha,recauda in sorted(dicc.items())]
    return [p2-p1 for p1,p2 in zip(recaudacion,recaudacion[1:])]