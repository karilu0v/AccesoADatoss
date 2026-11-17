from pathlib import Path

#método que calcula la media del presupuesto a través del budget puesto en el fichero de cada película
def media_presupuesto(peliculas): 
    media = 0
    num_peliculas = 0
    for p in peliculas:
        for c,v in p.items(): #recorro cada clave y valor para comprobar si la clave es budget y ya poder calcular con su valor
            if(c == "budget"):
                try:
                    media = media + float(v)
                except:
                    continue
                num_peliculas = num_peliculas + 1
    try:
        media = media/num_peliculas
    except:
        media = 0
    return media
          
def mejor_pelicula_ano(peliculas): #devuelve un diccionario con las mejores películas por año
    mejor_peli_ano = {}
    puntuacion = 0
    for p in peliculas:
        try:
            ano = int(p["startyear"])
        except:
            continue
        titulo = p["originalTitle"]
        try:
            rating = float(p["averageRating"])
        except:
            continue
        if mejor_peli_ano.__contains__(titulo): #comprueba si el diccionario tiene ese título
            if puntuacion < rating: 
                try:
                    puntuacion = rating
                    mejor_peli_ano[ano] = titulo
                except:
                    continue
        else: #si no lo tiene, lo crea
            mejor_peli_ano[ano] = titulo
            
    return mejor_peli_ano
               
            
def porcentaje_fracaso(peliculas): #devuelve el porcentaje de fracasos
    fracaso = 0
    num_pelis = 0
    for p in peliculas:
        #print(p)
        try:
            #print(p["budget"], p["grossWorldwide"])
            perdida = float(p["budget"]) - float(p["grossWorldwide"])
        except:
            continue
        if perdida < 0:
            fracaso = fracaso+1
        num_pelis = num_pelis+1
        try:
            porcentaje = (fracaso*100)/num_pelis
        except:
            porcentaje = 0
    return porcentaje
            


p = Path(__file__).parent / "imdb_top_250_movies.csv"

lineas = []
with open(p, "r", encoding="utf-8") as f:
    f.readline()
    for linea in f:
        lineas.append(linea)
    #print(lineas)

peliculas = []
pelicula ={}


for l in lineas: #para cada linea separo cada fila por comas y lo meto en el diccionario
    fila = l.split(",")
    pelicula["originalTitle"] = fila[0]
    pelicula["startyear"] = fila[2]
    pelicula["budget"] = fila[3]
    pelicula["grossWorldwide"] = fila[4]
    pelicula["averageRating"] = fila[6]
    peliculas.append(pelicula)
    pelicula= {}
    
print("media del presupuesto: ") 
print(media_presupuesto(peliculas))
print("mejor película por año: ")
print(mejor_pelicula_ano(peliculas))
print("porcentajes de fracasos: ")
print(porcentaje_fracaso(peliculas))
    