#Wurzelberechnung
#Zum Benutzen der Funktion einen Wert übergeben und das Ergebnis wird zurückgegeben
def wurzel(z1):
    erg = round(z1**0.5, 2)
    return erg

#Wird nur bei Standalone Berieb aufgerufen
def main():
    print("Programm zur Wurzelberechnung!")
    z1 = float(input("Bitte eine Zahl eingeben!")) #Eingabe der Zahl
    erg = wurzel(z1) #Aufruf der Funktion

    print("Die Wurzel von " + str(z1) + " ist --> " + str(erg)+"!")



if __name__=="__main__":
    main()