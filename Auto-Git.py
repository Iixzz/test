import os
import keyboard as kb
from time import sleep


#Abfrage ob push oder pull

aufgabe = int(input("push(1) oder pull(2): "))
repository = str(input("URL des GitHub-Repository: "))
datei = str(input("Dateiname zum hinzufügen (für alle .): "))
message = str(input("commit Message: "))


#Text eingeben
def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

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
if datei == ".":
    text("git add .", "")
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

