#ELIZA Chatbot
import wetter
import random
import nwurzel
import wurzel


word = []
numbers = []
randomanswer = ["Das ist ja interessant!", "Kannst du mir mehr davon erzählen", "Was möchtest du sonst noch wissen?", "Das finde ich cool"]


answer = {}
answer['hallo'] = "Hallo. Mein Name ist Eliza"
answer['wetter'] = "1a Wetterüberprüfung"
answer['hems'] = "Die HEMS ist eine schöne Schule"
answer['n-wurzel'] = "Wurzelberechnung"
answer['wurzel'] = "Wunderbar"


randomstadt = ["karlstein", "darmstadt", "wallerstädten", "aschaffenburg", "stuttgart"]

user = " "
key = " "

def wurzelziehen(zahl1):
    erg = wurzel.wurzel(zahl1)
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

def nwurzeln(word):
    global numbers
    for x in word:
        if x.isdigit():
            numbers.append(x)

    erg = nwurzel.nteWurzel(numbers[1], numbers[0])
    return erg
            
def search(word):
    answerright = False
    for i in word:
        #print(i)
        if i in answer:
            answerright= True
            if i == "wetter":
                return weather(word)

            if i == "n-wurzel":
                return nwurzeln(word)

            if i == "wurzel":
                for x in word:
                    if x.isdigit():
                        x = float(x)
                        return wurzelziehen(x)

        
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


