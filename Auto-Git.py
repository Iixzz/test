import os
import keyboard as kb
from time import sleep


#Abfrage ob push oder pull
"""
aufgabe = int(input("push(1) oder pull(2): "))
message = str(input("commit Message: "))
repository = str(input("URL des GitHub-Repository: "))
datei = str(input("Dateiname zum hinzufügen (für alle "."): "))
"""

aufgabe = 1
repository = "https://github.com/Iixzz/Auto-Git.git"
datei = str(input("Dateiname zum hinzufügen: "))

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



