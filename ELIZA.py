#ELIZA Chatbot
import wetter
import random
import nwurzel
import wurzel
import picalculator
import muenzwurf
import bild
import bild_sascha
import my_turtle_bohn
<<<<<<< HEAD
import turtle_jb

=======
import tim_turtle
>>>>>>> d39a2fc8da14f818a726cdb7781eb098ddba9a97

word = []
numbers = []
randomanswer = ["Das ist ja interessant!", "Kannst du mir mehr davon erzählen", "Was möchtest du sonst noch wissen?", "Das finde ich cool"]

#Einträge im Dictionary
answer = {}
answer['hallo'] = "Hallo. Mein Name ist Eliza"
answer['wetter'] = "1a Wetterüberprüfung"
answer['hems'] = "Die HEMS ist eine schöne Schule"
answer['n-wurzel'] = "Wurzelberechnung"
answer['wurzel'] = "Bitte zur Wurzelberechnung eine Zahl eingeben!"
answer['muenze'] = "Ich werfe eine Münze"
answer['zeichnung'] = "Zeichnung"
answer['logfile'] = "Logfileprogramm"



randomstadt = ["karlstein", "darmstadt", "wallerstädten", "aschaffenburg", "stuttgart"]

user = " "
key = " "

def wurzelziehen(zahl1): #Funktion zur Wurzelberechnung
    erg = wurzel.wurzel(zahl1) #Aufruf der importierten Funktion mit dem Parameter
    x = ("Die Wurzel ist " + str(erg) + "!")
    return x

def weather(word): 
    for i in word:
        if i in randomstadt:
            wetterstadt = wetter.stadtchat()
            ergebnis= f'Das Wetter in  {(i)} ist  {wetterstadt[0]} und die Temperatur beträgt {wetterstadt[1]} Grad'
            return ergebnis
    
    ergebnis1 = f'Bitte gebe eine Stadt ein'
    return ergebnis1

def nwurzeln(word): #Aufruf der nWurzel Funktion, n muss bei der Benutzereingabe immer als erstes angegeben werden
    global numbers
    for x in word:
        if x.isdigit(): #liest die Zahlen aus der Benutzereingabe und schreibt sie in eine extra Liste
            numbers.append(x)

    erg = nwurzel.nteWurzel(numbers[1], numbers[0]) #übergibt an Programm die beiden Werte
    erg2 = ("Das Ergebis lautet: " + str(erg))
    return erg2

def muenzenwerfen():
    
    zufall =muenzwurf.muenzwurf1()
    return zufall

def zeichnen(word):
    for y in word:
        if y == 'yannick':
            bild.zeichnen_yannick()

        elif y == 'sascha':
            bild_sascha.zeichnung_sascha()

        elif y == 'bohn':
            my_turtle_bohn.zeichne_bohn()
<<<<<<< HEAD
        
        elif y == 'janeck':
            turtle_jb.draw_janeck()
=======

        elif y == 'tim':
            tim_turtle.zeichnung()

def protokoll(file):
    data = open(f'{file}', 'r')
    print(data.read())

>>>>>>> d39a2fc8da14f818a726cdb7781eb098ddba9a97
            
            
def search(word):
    answerright = False
    for i in word:
        #print(i)
        if i in answer:
            answerright= True
            if i == "wetter":
                return weather(word)

            if i == "n-wurzel": #suche nach -Wurzel in Dictionary
                return nwurzeln(word)

            if i == "wurzel":
                for x in word:
                    if x.isdigit():
                        x = float(x)
                        return wurzelziehen(x)
                    
            if i == "pi":#Sonderfall Pi
                return picalculator.picalc()
            
            if i == "zeichnung":
                return zeichnen(word)
            

            if i == "logfile":
                x = word.index("logfile")
                x = x + 1 
                file = word[x]
                return protokoll(file)
                
            
            if i == "muenze":
                return muenzenwerfen()

                  
            return answer[i]
            
    
    if answerright == False:
        return random.choice(randomanswer)
    

def main():
    print("Willkommen zum Eliza Chatbot\n")
    print("Sie können jederzeit die Anwendung mit dem Befehl bye beenden")




    global user
    while user != "bye":
        #Benutzereingabe und alle Buchstaben klein
        user = input("Ihre Eingabe:")
        user_small= user.lower()


        #jedes Wort einzeln in Liste
        word = user_small.split(" ")
        print(search(word))

    print("Ciao Kakao")


if __name__=="__main__":
    main()


