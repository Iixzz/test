def push():
    print("Push wurde ausgeführt!")

def pull():
    print("Pull wurde ausgeführt!")


try:
    if aufgabe == 1:
        push()
    elif aufgabe == 2:
        pull()
    else:
        print("Ungültige Auswahl. Bitte 1 oder 2 eingeben.")
except ValueError:  # Falls die Eingabe keine Zahl ist
    print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
except NameError:  # Falls push() oder pull() nicht definiert sind
    print("Funktion nicht definiert!")
