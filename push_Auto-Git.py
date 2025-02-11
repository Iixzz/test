import os
import keyboard as kb
from time import sleep





class push():
    def __init__(self):
        self.script_dir = str(input("Ordner zum hochladen (Dateipfad): "))
        self.repository_URL = str(input("URL des GitHub-Repository: "))
        self.commit_message = str(input("message: "))
        self.convert_commit_message = f'"{self.commit_message}"'

        self.doPush()

    def checkDatein(self):
        self.datein_liste = []
        self.vorhandene_dateien = os.listdir(self.script_dir)
        while True:
            self.datei = str(input("Gib eine Dateinnamen ein (oder . für alle oder ENTER zum Beenden): "))
            if self.datei == "" :
                break
            elif self.datei == ".":
                self.datein_liste = "."
                break
            else:
                if self.datei in self.vorhandene_dateien:
                    self.datein_liste.append(self.datei)
                else:
                    print("datei nicht vorhanden")
                    pass
        return self.datein_liste
    
    def doPush(self):
        self.checkDatein()

        os.system("start cmd")
        sleep(1)

        text("cd /d ", self.script_dir)

        text("git init", "")
        text("git remote add origin ", self.repository_URL)

        if self.datein_liste == ".":
            text("git add ", self.datein_liste)
        else:
            for datei in self.datein_liste:
                text("git add ", datei)

        text("git commit -m ", self.convert_commit_message)
        text("git push origin master", "")
        sleep(1)

        os.system("taskkill /F /IM cmd.exe")

def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

#Ausführung
def main():
    git_push = push()
    


if __name__ == "__main__":
    main()
