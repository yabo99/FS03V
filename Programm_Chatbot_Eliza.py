#Programm_Eliza
#Sebastian_Freiberger
#20.09.2023
#Version 1.0

import random

#Wörterliste auf die Später reagiert werden soll.
woerterliste = {
    'hallo' : 'Guten Tag',
    'name ': 'Mein Name ist Eliza',
    'wetter': 'Das Wetter ist Heute sehr Schön',
    'haarfarbe' : 'Als Ai habe ich kein wirkliches aussehen!',
    'temperatur':'Die Temperaturen sind sehr angenehm!',
    'sport': 'Als Ai ohne beine kann ich leider keinen Sport machen...'
}

#zufalls antworten
zufalls_antworten = [
'Oh interessant...',
'Das klingt spannend erzaehl mir mehr!',
'Ich verstehe....',
'Ich weis nicht recht',
'stell mir doch eine andere Frage']

#begrüßung

print('Hallo ich bin Eliza, du kannst die Unterhaltung jeder Zeit mit "bye" beenden!')
print('Gibt es etwas worüber sie reden wollen?')
print('')


#Eingabe

nutzereingabe = ''
antworten_richtig = False
        


while nutzereingabe != "bye": #while Schleife um einen loop bis zum beenden des users zu haben.
    nutzereingabe = input("Wie lautet ihre Frage/Antwort? : ")
    ne_klein = nutzereingabe.lower()
    ne_teile = ne_klein.split(" ")
    for wort in ne_teile:
        if wort in woerterliste:
            antworten_richtig = True
            print(woerterliste[wort])
            

    if antworten_richtig == False:
        print(random.choice(zufalls_antworten))
        break

 


print('Ich hoffe ich konnte helfen. Bis zum nächsten Mal!')
