datein_liste = []
while True:
    datei = str(input("Gib eine Dateinnamen ein (oder . für alle oder ENTER zum Beenden): "))
    if datei == "" :
        break
    elif datei == ".":
        datein_liste = "."
        break
    else:
        datein_liste.append(datei)

print(datein_liste)