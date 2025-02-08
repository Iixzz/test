import os
import keyboard as kb
from time import sleep

aufgabe = int(input("push(1) oder pull(2) oder mit tag(3): "))


class push():
    def __init__(self):
        pass

class pull():
    def __init__(self):
        self.script_dir = str(input("Ordner zum hochladen (Dateipfad): "))
        self.repository_URL = str(input("URL des GitHub-Repository: "))
        
        os.system("start cmd")
        sleep(0.5)

        text("cd /d ", self.script_dir)

        text("git init", "")
        text("git remote add origin ", self.repository_URL)
        text("git pull origin master", "")

class tag():
    def __init__(self):
        self.script_dir = str(input("Ordner zum hochladen (Dateipfad): "))
        self.repository_URL = str(input("URL des GitHub-Repository: "))
        os.system("start cmd")
        sleep(0.5)

        text("cd /d ", self.script_dir)

        text("git init", "")
        text("git remote add origin ", self.repository_URL)
        text("git pull origin master", "")


def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")


#Ausführung
try:
    if aufgabe == 1:
        push()
    elif aufgabe == 2:
        pull()
    elif aufgabe == 3:
        tag()
    else:
        print("Ungültige Auswahl. Bitte 1 oder 2 eingeben.")
except ValueError:  # Falls die Eingabe keine Zahl ist
    print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
