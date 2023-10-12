def nteWurzel(a, n):
    a=float(a) #Umwandeln
    n=float(n)
    return (round(a**(1/n), 2)) #Berechnung der n-ten Wurzel von einer Zahl




def main():
    
    zahl=float(input("Von welcher Zahl wollen Sie die n-te Wurzel berechnen: "))
    wurzel=float(input("Welche Wurzel wollen Sie berechnen: "))
    print(nteWurzel(zahl, wurzel))


if __name__=="__main__":
    main()