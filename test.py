import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Eingabe in Tkinter")
        self.geometry("400x200")

        # Label
        self.label = tk.Label(self, text="Gib deinen Namen ein:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entry-Feld
        self.entry = tk.Entry(self, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Button zum Anzeigen der Eingabe
        self.button = tk.Button(self, text="Anzeigen", command=self.zeige_eingabe)
        self.button.pack(pady=5)

        # Label für die Ausgabe
        self.output_label = tk.Label(self, text="", font=("Arial", 12, "bold"))
        self.output_label.pack(pady=10)

    def zeige_eingabe(self):
        eingabe = self.entry.get()  # Eingabe aus dem Feld holen
        self.output_label.config(text=f"Hallo, {eingabe}!")  # Text im Label ändern
        print(eingabe)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
