import os
import keyboard as kb
from time import sleep



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
if __name__ == "__main__":
    git_tag = tag()