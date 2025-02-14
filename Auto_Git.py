from module import pull_Auto_Git as pullAG
from module import push_Auto_Git as pushAG
from module import tag_Auto_Git as tagAG

import tkinter as tk


class mainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hauptfenster")
        self.geometry("600x300")

        self.label = tk.Label(self, text="Auf GitHub Hochladen", font = ("Arial", 18, "underline"))
        self.label.pack()

        self.button_push = tk.Button(self, text= "Push", command = self.oeffne_push_window)
        self.button_push.place(x = 75, y = 150, width= 90, height= 20)

        self.button_pull = tk.Button(self, text= "Pull", command = self.oeffne_pull_window)
        self.button_pull.place(x = 255 , y = 150, width= 90, height= 20)

        self.button_tag = tk.Button(self, text= "Tag", command = self.oeffne_tag_window)
        self.button_tag.place(x = 435, y = 150, width= 90, height= 20)

    def oeffne_push_window(self):
        PushWindow()

    def oeffne_pull_window(self):
        PullWindow()

    def oeffne_tag_window(self):
        TagWindow()

    

class PushWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Push Window")
        self.geometry("600x350")

        self.label = tk.Label(self, text="Push-Optionen", font=("Arial", 14, "bold"))
        self.label.pack(pady=10)

        #Ordner eingabe
        self.label_ordner = tk.Label(self, text="Ordner zum hochladen (Dateipfad)")
        self.label_ordner.place(x= 150, y=70, height=15)

        self.entry_ordner = tk.Entry(self, width=50)
        self.entry_ordner.place(x= 150, y= 85 )

        #Repository eingabe
        self.label_repository = tk.Label(self, text="URL des GitHub-Repository: ")
        self.label_repository.place(x= 150, y=120, height=15)

        self.entry_repository = tk.Entry(self, width=50)
        self.entry_repository.place(x= 150, y= 135)

        #Message eingabe
        self.label_message = tk.Label(self, text="Commit message: ")
        self.label_message.place(x= 150, y=170, height=15)

        self.entry_message = tk.Entry(self, width=50)
        self.entry_message.place(x= 150, y= 185)

        #Datein eingabe
        self.label_datein = tk.Label(self, text="Datein eingeben (mit ; trennen) oder für alle .")
        self.label_datein.place(x= 150, y=220, height=15)

        self.entry_datein = tk.Entry(self, width=50)
        self.entry_datein.place(x= 150, y= 235)

        #Eingabe bestätigen button 
        self.button_eingabe = tk.Button(self, text= "Eingabe bestätigen", command = self.eingabe)
        self.button_eingabe.place(x = 225 , y = 270, width= 160, height= 20)

    def eingabe(self):
        ordner = self.entry_ordner.get()
        repository = self.entry_repository.get()
        message = self.entry_message.get()
        datein = self.entry_datein.get()
        pushAG.push(ordner, repository, message, datein)
        self.beenden()

    def beenden(self):
        self.destroy()
        run()



class PullWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pull Window")
        self.geometry("600x300")

        label = tk.Label(self, text="Pull-Optionen", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        #Ordner eingabe
        self.ordner_label = tk.Label(self, text="Ordner zum hochladen (Dateipfad)")
        self.ordner_label.place(x= 150, y=70, height=15)

        self.entry_ordner = tk.Entry(self, width=50)
        self.entry_ordner.place(x= 150, y= 85 )

        #Repository eingabe
        self.repository_label = tk.Label(self, text="URL des GitHub-Repository: ")
        self.repository_label.place(x= 150, y=120, height=15)

        self.entry_repository = tk.Entry(self, width=50)
        self.entry_repository.place(x= 150, y= 135)

        #Eingabe bestätigen button 
        self.button_eingabe = tk.Button(self, text= "Eingabe bestätigen", command = self.eingabe)
        self.button_eingabe.place(x = 225 , y = 270, width= 160, height= 20)

    def eingabe(self):
        ordner = self.entry_ordner.get()
        repository = self.entry_repository.get()
        pullAG.pull(ordner, repository)

    def beenden(self):
        self.destroy()
        run()
class TagWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tag Window")
        self.geometry("600x300")

        label = tk.Label(self, text="Tag-Optionen", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        #Ordner eingabe
        self.label_ordner = tk.Label(self, text="Ordner zum hochladen (Dateipfad)")
        self.label_ordner.place(x= 150, y=70, height=15)

        self.entry_ordner = tk.Entry(self, width=50)
        self.entry_ordner.place(x= 150, y= 85 )

        #Repository eingabe
        self.label_repository = tk.Label(self, text="URL des GitHub-Repository: ")
        self.label_repository.place(x= 150, y=120, height=15)

        self.entry_repository = tk.Entry(self, width=50)
        self.entry_repository.place(x= 150, y= 135)

        #Message eingabe
        self.label_tag = tk.Label(self, text="Version: ")
        self.label_tag.place(x= 150, y=170, height=15)

        self.entry_tag = tk.Entry(self, width=50)
        self.entry_tag.place(x= 150, y= 185)

        #Eingabe bestätigen button
        self.button_eingabe = tk.Button(self, text= "Eingabe bestätigen", command = self.eingabe)
        self.button_eingabe.place(x = 255 , y = 270, width= 160, height= 20)

    def eingabe(self):
        ordner = self.entry_ordner.get()
        repository = self.entry_repository.get()
        version = self.entry_tag.get()
        tagAG.tag(version, ordner, repository)
    
    def beenden(self):
        self.destroy()
        run()


def run():
    app = mainWindow()
    app.mainloop()

if __name__ == "__main__":
    run()