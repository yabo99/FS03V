import random

def muenzwurf():
    #Diese Funkton liefert einen String(Kopf oder Zahl) zurück.
    münzwurf = ["Kopf", "Zahl"]
    return random.choice(münzwurf)


if __name__=="__main__":
    #String wird in der Variable m gespeichert und ausgegben.
    m = muenzwurf()
    print(m)