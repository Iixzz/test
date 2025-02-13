datein_liste = []
test = "Hallo;2"
datein_eingabe = test.strip()



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

     

asd(datein_eingabe)