def wurzel(z1):
    erg = round(z1**0.5, 2)
    return erg


def main():
    print("Programm zur Wurzelberechnung!")
    z1 = float(input("Bitte eine Zahl eingeben!"))
    erg = wurzel(z1)

    print("Die Wurzel von " + str(z1) + " ist --> " + str(erg)+"!")



if __name__=="__main__":
    main()