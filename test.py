# Benutzer gibt mehrere Werte ein, durch Komma getrennt
eingabe = input("Gib mehrere Werte ein, getrennt durch Komma: ")

# Aufteilen der Eingabe an den Kommata
werte = eingabe.split(",")  # Hier wird die Eingabe an jedem Komma aufgeteilt

# Ausgabe der aufgeteilten Werte
print("Aufgeteilte Werte:")
for wert in werte:
    print(wert.strip())
