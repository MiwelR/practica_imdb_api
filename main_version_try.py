import requests
from config import *

url_template = "http://www.omdbapi.com/?apikey={}&{}={}"

class PeticionError(Exception):
    pass

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == "False":
            raise PeticionError(datos["Error"])
        else: 
            return datos
    else: 
        raise PeticionError("Error en consulta: {}".format(respuesta.status_code))

repeat = 'S'
while repeat == 'S':
    try:
        pregunta = input("Buscar Película por Título: ")
        respuesta = peticion(url_template.format(API_KEY, 's', pregunta))
        primera_peli = respuesta['Search'][0]
        clave = primera_peli['imdbID']

        respuesta = peticion(url_template.format(API_KEY, 'i', clave))
        titulo = respuesta['Title']
        agno = respuesta['Year']
        director = respuesta ['Director']
        print("La película {}, estrenada en el año {}, fue dirigida por: {}".format(titulo, agno, director))

        repeat = input("¿Quieres realizar otra búsqueda? S/N: ").upper()
        if repeat == 'N':
            print("Hasta su próxima búsqueda...")
        elif repeat != ('N' and 'S'):
            print("Como no sabemos exactamente si quiere buscar de nuevo o no, ejecute de nuevo la aplicación para buscar. Que tenga un buen día...")
    except PeticionError as e: # PeticionError en variable 'e'
        print(e)
