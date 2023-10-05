#Aufgabe 4: Anwendung zweier Zahlen, wo die Summe, die Differenz, die Summe und den Quotienten berechnet 
#und mit dem jeweiligen Ergebis, des Benutzers vergleicht.
#Von Yannic Bohn
#Version 1.0

print('Hallo lieber Benutzer!')
Zahl1 = float(input('Bitte geben Sie die erste Zahl ein: '))
print('Vielen Dank für die erste Ziffer!')
Zahl2 = float(input('Bitte geben Sie die zweite Zahl ein: '))
print('Sehr gut gemacht!')

Summe1 = float(input('Bitte geben Sie die Summe beider Zahlen ein: '))
Summe2 = Zahl1 + Zahl2
if Summe2 == Summe1:
    print('Antwort ist richtig! Super gemacht!')
else:
    print('Antwort ist falsch, du Versager!')
    print('Das Ergebnis ist: '+ str(Summe2))

Diff1 = float(input('Bitte geben Sie die Differenz beider Zahlen ein: '))
Diff2 = Zahl1 - Zahl2
if Diff2 == Diff1:
    print('Antwort ist richtig! Super gemacht!')
else:
    print('Antwort ist falsch, du Versager!')
    print('Das Ergebnis ist: '+ str(Diff2))

Pro1 = float(input('Bitte geben Sie das Produkt beider Zahlen ein: '))
Pro2 = Zahl1 * Zahl2
if Pro2 == Pro1:
    print('Antwort ist richtig! Super gemacht!')
else:
    print('Antwort ist falsch, du Versager!')
    print('Das Ergebnis ist: '+ str(Pro2))

Quo1 = float(input('Bitte geben Sie den Quotienten beider Zahlen ein: '))
Quo2 = Zahl1 / Zahl2
if Quo2 == Quo1:
    print('Antwort ist richtig! Super gemacht!')
else:
    print('Antwort ist falsch, du Versager!')
    print('Das Ergebnis ist: '+ str(Quo2))

if Summe1 == Summe2:
    if Diff1 == Diff2:
        if Pro1 == Pro2:
                if Quo1 == Quo2:
                    print('Wow, Sie haben 100 Prozent erreicht! Glückwunsch!😊')

if Summe1 != Summe2:
    if Diff1 == Diff2:
        if Pro1 == Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 75 Prozent erreicht! Glückwunsch!')

if Summe1 == Summe2:
    if Diff1 != Diff2:
        if Pro1 == Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 75 Prozent erreicht! Glückwunsch!')

if Summe1 == Summe2:
    if Diff1 == Diff2:
        if Pro1 != Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 75 Prozent erreicht! Glückwunsch!')

if Summe1 == Summe2:
    if Diff1 == Diff2:
        if Pro1 == Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 75 Prozent erreicht! Glückwunsch!')

if Summe1 != Summe2:
    if Diff1 != Diff2:
        if Pro1 == Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 50 Prozent erreicht! Ist ausreichend!')

if Summe1 != Summe2:
    if Diff1 == Diff2:
        if Pro1 != Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 50 Prozent erreicht! Ist ausreichend!')

if Summe1 != Summe2:
    if Diff1 == Diff2:
        if Pro1 == Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 50 Prozent erreicht! Ist ausreichend!')

if Summe1 == Summe2:
    if Diff1 != Diff2:
        if Pro1 != Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 50 Prozent erreicht! Ist ausreichend!')

if Summe1 == Summe2:
    if Diff1 != Diff2:
        if Pro1 == Pro2:
                if Quo1 != Quo2:
                    print(' Sie haben 50 Prozent erreicht! Ist ausreichend!')

if Summe1 == Summe2:
    if Diff1 == Diff2:
        if Pro1 != Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 50 Prozent erreicht! Ist ausreichend!')

if Summe1 != Summe2:
    if Diff1 != Diff2:
        if Pro1 != Pro2:
                if Quo1 == Quo2:
                    print('Sie haben 25 Prozent erreicht! Durchgefallen!')

if Summe1 != Summe2:
    if Diff1 != Diff2:
        if Pro1 == Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 25 Prozent erreicht! Durchgefallen!')

if Summe1 != Summe2:
    if Diff1 == Diff2:
        if Pro1 != Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 25 Prozent erreicht! Durchgefallen!')

if Summe1 == Summe2:
    if Diff1 != Diff2:
        if Pro1 != Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 25 Prozent erreicht! Durchgefallen!')

if Summe1 != Summe2:
    if Diff1 != Diff2:
        if Pro1 != Pro2:
                if Quo1 != Quo2:
                    print('Sie haben 0 Prozent erreicht! Sie sind übel shit!')