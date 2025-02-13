datein_liste = []
test = "Hallo;2"
datein_eingabe = test.strip()


"""
try:
    self.vorhandene_dateien = os.listdir(self.script_dir)
except Exception as e:
    print(f"Fehler: {e}")
    sys.exit()
    """

def asd(datein_eingabe): 
    if ";" in datein_eingabe:
        datein_ = datein_eingabe.split(";")
        print(type(datein_eingabe))
        for datei in datein_:
            print(datei)
    elif datein_eingabe == ".":
        datein_liste = "."
        print(datein_liste)
    elif not datein_eingabe:
        print("3")
    else:
        datein_liste = datein_eingabe
        print(datein_liste)


"""while True:
    if datein_eingabe in datein_liste:
        pass
    break    """      

asd(datein_eingabe)