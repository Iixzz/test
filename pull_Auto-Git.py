import os
import keyboard as kb
from time import sleep


class pull():
    def __init__(self):
        os.system("start cmd")


    def direct_cmd(self):
        self.script_dir = str(input("Ordner zum downlowden (Dateipfad): "))

        text("cd /d ", self.script_dir)
    
    def do_pull(self):
        self.repository_URL = str(input("URL des GitHub-Repository: "))
        
        text("git init", "")
        text("git remote add origin ", self.repository_URL)
        text("git pull origin master", "")



def text(msg1, msg2):
    kb.write(msg1 +msg2)
    kb.press_and_release("enter")

def main():
    git_pull = pull()
    git_pull.direct_cmd()
    git_pull.do_pull()

#Ausführung
if __name__ == "__main__":
    main()
