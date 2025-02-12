import sys

fehlerFrei = 0

def asd(fehlerFrei):
    print(f"Fehler: ")
    sys.exit()
    fehlerFrei += 1
    return fehlerFrei

asd()
print(fehlerFrei)
