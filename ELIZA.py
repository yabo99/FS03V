#ELIZA Chatbot
import wetter
import random

word = []
randomanswer = ["Das ist ja interessant!", "Kannst du mir mehr davon erzählen", "Was möchtest du sonst noch wissen?", "Das finde ich cool"]


answer = {}
answer['hallo'] = "Hallo. Mein Name ist Eliza"
answer['wetter'] = "1a Wetterüberprüfung"
answer['hems'] = "Die HEMS ist eine schöne Schule"

randomstadt = ["karlstein", "darmstadt", "wallerstädten", "aschaffenburg"]

user = " "
key = " "
def weather(word):
    for i in word:
        if i in randomstadt:
            wetterstadt = wetter.stadtchat()
            ergebnis= f'Das Wetter in  {(i)} ist  {wetterstadt[0]} und die Temperatur beträgt {wetterstadt[1]} Grad'
            return ergebnis
            
def search(word):
    answerright = False
    for i in word:
        #print(key)
        if i in answer:
            answerright= True
            if i == "wetter":
                return weather(word)
        
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


