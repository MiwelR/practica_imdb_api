import requests
from config import *

url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            return datos["Error"]
        else: 
            return datos
    else: 
        return "Error en consulta por ID: ", respuesta.status_code

busqueda = True
while busqueda == True:
    pregunta = input("Buscar Película por Título: ")
    respuesta = peticion(url_template.format(API_KEY, 's', pregunta))
    if isinstance(respuesta, str):
        print(respuesta)
    else:
        primera_peli = respuesta['Search'][0]
        clave = primera_peli['imdbID']

        respuesta = peticion(url_template.format(API_KEY, 'i', clave))
        if isinstance(respuesta, str):
            print(respuesta)
        else:
            titulo = respuesta['Title']
            agno = respuesta['Year']
            director = respuesta ['Director']
            print("La película {}, estrenada en el año {}, fue dirigida por: {}".format(titulo, agno, director))

    repeat = input("¿Quieres realizar otra búsqueda? S/N: ")
    if repeat.upper() == 'S':
        busqueda = True
    elif repeat.upper() == 'N':
        print("Hasta su próxima búsqueda...")
        busqueda = False
    else:
        print("Como no sabemos exactamente si quiere buscar de nuevo o no, ejecute de nuevo la aplicación para buscar. Que tenga un buen día...")
        busqueda = False
