import os
import keyboard as kb

def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

script_dir = os.path.dirname(os.path.abspath(__file__))
datein_liste = []
while True:
    datei = str(input("Gib eine Dateinnamen ein (oder . für alle oder ENTER zum Beenden): "))
    if datei == "" :
        break
    datein_liste.append(datei)
vorhandene_datein = os.listdir(script_dir)

if datein_liste[0] == ".":
    text("git add .", "")
else:
    for datei in datein_liste:
        if datei in vorhandene_datein:
            text("git add ", datei)
        else:
            print(f"{datei} nicht vorhanden! Überprüfen Sie die Schreibweise.")