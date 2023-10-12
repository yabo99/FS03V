#Wetterdaten

import requests

API_key = "12cd6ba246a3613d5d957f3e497c0fac"
Lat = 0
Lon = 0
def stadtchat():
    stadt="darmstadt"
    umwandeln(stadt)
    datenchat = wetterdaten(Lat, Lon)
    return datenchat

def eingabe():
    stadt=input("Welche Stadt wollen Sie abfragen? ")
    return stadt

def umwandeln(town):
    global Lat
    global Lon
    stadt=town
    
    geo = f'http://api.openweathermap.org/geo/1.0/direct?q={stadt}&limit=1&appid={API_key}'

    stadt=requests.get(geo)

    koordinaten = stadt.json()

    Lat = koordinaten[0]["lat"]
    Lon = koordinaten[0]["lon"]
    

def wetterdaten(Lat, Lon):
    wetter = f'https://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Lon}&appid={API_key}&lang=de'

    wetterdaten=requests.get(wetter)

    temperaturen=wetterdaten.json()
    Wetter = temperaturen['weather'][0]["description"]
    Wetter2 = round(temperaturen['main']["temp"]-273.15)

    return(Wetter, Wetter2)

def main():
    town= eingabe()
    umwandeln(town)
    
    w = wetterdaten(Lat, Lon)
    print("Das Wetter in " + town+" beträgt " +str(w[0]) + " und die Temperatur ist " +str(w[1])+" Grad")
    
    
if __name__=="__main__":
    main()
