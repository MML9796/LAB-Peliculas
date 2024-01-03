from peliculas import *

def test_lee_peliculas(registro:str)->None:
    print(f'Se han leido {len(registro)} peliculas')
    print(f'Las tres primeras son: {registro[:3]}')

def test_pelicula_mas_ganancias(registro:str,genero:Optional[str]=None)->None:
    res=pelicula_mas_ganancias(registro,genero)
    print(f'La pelicula con mas ganancias en el genero {genero} es: {res}')

def test_media_presupuesto_por_genero(registro:str)->None:
    res=media_presupuesto_por_genero(registro)
    print(f'La media de presupuestos por genero es: {res}')

def test_peliculas_por_actor(registro:str,fecha_ini:Optional[int]=None,fehca_fin:Optional[int]=None)->None:
    res=peliculas_por_actor(registro,fecha_ini,fehca_fin)
    print(f'Las peliculas realizadas por los actores entre las fechas {fecha_ini} y {fehca_fin} son: {res}')

def test_actores_mas_frecuentes(registro:str,n:int,fecha_ini:Optional[int]=None,fecha_fin:Optional[int]=None)->None:
    res=actores_mas_frecuentes(registro,n,fecha_ini,fecha_fin)
    print(f'Los {n} actores más frecuentes en las peliculas entre los años {fecha_ini} y {fecha_fin} son: {res}')
def test_recaudacion_total_por_año(registro:str,genero:Optional[str]=None)->None:
    res=recaudacion_total_por_año(registro,genero)
    print(f'La recaudación total por año en el género {genero} es: {res}')

def test_incremento_recaudacion_por_año(registro:str,genero:Optional[str]=None)->None:
    res=incrementos_recaudacion_por_año(registro,genero)
    print(f'Los incrementos de recaudación por año en los generos {genero} son: {res}')

if __name__=='__main__':
    datos=lee_peliculas('data\peliculas.csv')
    #test_lee_peliculas(datos)
    #test_pelicula_mas_ganancias(datos)
    #test_pelicula_mas_ganancias(datos,'Drama')
    #test_media_presupuesto_por_genero(datos)
    #test_peliculas_por_actor(datos,2010,2020)
    #test_actores_mas_frecuentes(datos,3,2005,2015)
    # test_recaudacion_total_por_año(datos,{'Drama','Acción'})
    # test_recaudacion_total_por_año(datos)
    test_incremento_recaudacion_por_año(datos)
    test_incremento_recaudacion_por_año(datos,{'Drama','Acción'})