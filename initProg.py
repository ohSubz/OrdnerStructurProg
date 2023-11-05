# ProInit 1.0
# Beschreibung:
'''
=====================================================================================================
ProInit dient dazu, für angefangene Projekte die vordefinierte Ordnerstruktur automatisch zu erstellen. 
Die Ordnerstruktur wird über eine Excel-Tabelle vordefiniert (siehe Beispiel). 
Beim Ausführen des Programms wird zu Beginn der Projektname abgefragt. 
Anschließend muss der Benutzer die Ordnerdatei auswählen sowie das gewünschte Verzeichnis angeben.
=====================================================================================================
'''
# Import Bibs
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import os

# Hilfsfunktionen - Zum wählen der Mapping-Datei für die Ordnerstruktur

root = tk.Tk()
root.withdraw()  # Verstecke das Hauptfenster von tkinter

# Funktion für die Auswahl der Excel-Vorlageliste
def get_file():
    root = tk.Tk()
    root.withdraw() # Ausblenden des Hauptfenster von tkinter

    path_file = filedialog.askopenfilename(title="Datei auswählen", filetypes=[("xlsx-Dateien", "*.xlsx")])

    if path_file:
        return path_file
    else:
        print("Keine Datei ausgewählt!")
        return none
# Funktion für die Bestimmung des Projekt-Verzeichnisses
def get_projectPlace():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Ordner für base_path auswählen")
    
    if folder_path:
        return folder_path
    else:
        print("Kein Ordner ausgewählt.")
        return None


# Begin des Programms

# Projektnam
project_name = simpledialog.askstring("Projektnamen", "Geben Sie den Projektnamen ein:")
# Laden der Mapping-Datei
path_file = get_file()
base_path = get_projectPlace()

if path_file:
    df = pd.read_excel(path_file)

if project_name:
    # base_path auswählen
    #base_path = get_projectPlace()

    if base_path:
        # Erstellen des Verzeichnis mit dem Projektnamen
        project_path = os.path.join(base_path, project_name)
        os.makedirs(project_path)

        # Schleife für die Hauptordner
        for column in df.columns:
            main_folder = os.path.join(project_path, column)

            # Überprüfen, ob der Ordner bereits existiert.
            if not os.path.exists(main_folder):
                os.makedirs(main_folder)

            # Schleife für die Unterordner
            for subfolder in df[column]:
                if not pd.isna(subfolder):
                    subfolder_path = os.path.join(main_folder, subfolder)

                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path)

        print("Die Ordnerstruktur wurde erstellt in:", project_path)









