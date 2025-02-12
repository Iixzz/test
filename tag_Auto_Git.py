import sys
import os

script_dir = str(input("Ordner zum hochladen (Dateipfad): ")) # Simuliert einen Fehler

try:
    vorhandene_dateien = os.listdir(script_dir)
except Exception as e:
    print(f"Fehler: {e}")
    sys.exit()

for i in range(100):
    print("1")