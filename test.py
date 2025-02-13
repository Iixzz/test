datein_liste = []
datein_eingabe = "1;2;3;4"
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
        print(datein_eingabe)
    elif datein_eingabe == ".":
        datein_liste = "."

"""while True:
    if datein_eingabe in datein_liste:
        pass
    break    """      

asd(datein_eingabe)