import json

def Load():
    
#Mando a llamr la ruta y la guarda en la variable
    rutaConfig = "config.json"
#Abre la ruta del JSON utilizando el formato UTF-8 
#y retornando el contenido del JSON como objeto Python
    def LoadConfig():
        with open(rutaConfig, encoding="UTF-8") as archivo:
            return json.load(archivo)

    # Guarda en la variable el contenido del JSON
    Configuracion = LoadConfig()
    langueje = "es"
    return Configuracion, langueje