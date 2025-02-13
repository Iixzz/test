import os
import keyboard as kb
from time import sleep
import sys





class push():
    def __init__(self, ordner, repository, message, datein):
        self.script_dir = ordner
        self.repository_URL = repository
        self.commit_message = message
        self.convert_commit_message = f'"{self.commit_message}"'


        self.doPush(datein)

    def checkDatein(self, datein):
        self.datein_push = []
        self.datein_eingabe = datein.strip()

        try:
            self.vorhandene_dateien = os.listdir(self.script_dir)
        except Exception as e:
            print(f"Fehler: {e}")
            sys.exit()

        if ";" in self.datein_eingabe:
            self.datein_liste = self.datein_eingabe.split(";")
            for datei in self.datein_liste:
                if datei in self.vorhandene_dateien:
                    self.datein_push.append(datei)
                else:
                    print(f"{datei} nicht vorhanden")
                    sys.exit()
        elif self.datein_eingabe == ".":
            self.datein_push = "."
        elif not self.datein_eingabe:
            print("Fehler: Keine Datei eingegeben")
            sys.exit(1)
        else:
            self.datein_push = self.datein_eingabe



        return self.datein_push
    
    
    def doPush(self, datein):
        try:
            self.checkDatein(datein)
            os.system("start cmd")
            sleep(1)

            text("cd /d ", self.script_dir)
            text("git init", "")
            text("git remote add origin ", self.repository_URL)

            if self.datein_push == ".":
                text("git add ", self.datein_push)
            else:
                for datei in self.datein_push:
                    text("git add ", datei)

            text("git commit -m ", self.convert_commit_message)
            text("git push origin master", "")
            text("git remote rm origin", "")
            sleep(1)

            """os.system("taskkill /F /IM cmd.exe")"""

        except Exception as e:  # Ausnahmeobjekt als 'e' referenzieren
            print(f"Fehler: {e}")  # 'e' gibt die Ausnahme-Details an
            sys.exit()

def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

#Ausführung
def main():
    git_push = push()
    


if __name__ == "__main__":
    main()
