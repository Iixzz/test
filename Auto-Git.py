import os
import keyboard as kb
from time import sleep


#Abfrage ob push oder pull

aufgabe = int(input("push(1) oder pull(2): "))
repository = str(input("URL des GitHub-Repository: "))

datein_liste = []
while True:
    datei = str(input("Gib eine Dateinnamen ein (oder . für alle oder ENTER zum Beenden): "))
    if datei == "" :
        break
    datein_liste.append(datei)

message = str(input("commit Message: "))
#tag = str(input("Wollen Sie der Versin einen tag geben: (y/n)"))

#Text eingeben
def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

if aufgabe == 1:
    #Terminal öffnen und auf Arbeitsverzeichnis leiten
    os.system("start cmd")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sleep(0.5)

    text("cd /d ", script_dir)
    sleep(0.5)

    #git initiieren
    text("git init" , "")
    sleep(0.5)

    #repository einrichten
    text("git remote add origin ", repository)
    sleep(0.5)

    #git Datein hinzufügen
    vorhandene_datein = os.listdir(script_dir)
    if datein_liste[0] == ".":
        text("git add .", "")
    else:
        for datei in datein_liste:
            if datei in vorhandene_datein:
               text("git add ", datei)
            else:
                print(f"{datei} nicht vorhanden! Überprüfen Sie die Schreibweise.")
                
    sleep(0.5)

    #Datein commiten
    if message != "": 
        text("git commit -m ", message)
    else:
        print("Üngültige eingabe")
        message = str(input("commit Message: "))
    sleep(0.5)

    #Datein auf GitHub pushen 
    text("git push origin master", "")

elif aufgabe == 2:
    pass

else:
    print("üngültige Eingabe")
    aufgabe = int(input("push(1) oder pull(2): "))