import tkinter as tk
from PIL import Image, ImageTk
import csv

# Fonction pour lire le fichier CSV et retourner une liste de tuples (x, y, nom_de_la_gare)
def lire_stations_csv(fichier_csv):
    stations = []
    with open(fichier_csv, 'r', encoding='utf-8') as fichier:
        lecteur_csv = csv.reader(fichier)
        next(lecteur_csv)  # Ignorer l'en-tête du CSV
        for ligne in lecteur_csv:
            x, y, nom_gare = ligne
            stations.append((int(x), int(y), nom_gare))
    return stations

# Fonction appelée lorsque le bouton est cliqué
def on_station_click(station_name):
    print(f"Gare sélectionnée : {station_name}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Carte du Métro")

# Charger l'image de la carte du métro
original_image = Image.open("metrof_r.png")  # Remplace par ton chemin d'image
tk_image = ImageTk.PhotoImage(original_image)

# Créer une frame contenant l'image
frame = tk.Frame(root)
frame.pack()

# Ajouter un canvas à la frame
canvas = tk.Canvas(frame, width=tk_image.width(), height=tk_image.height())
canvas.pack()

# Afficher l'image sur le canvas
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Lire les stations depuis le fichier CSV
stations = lire_stations_csv('stations_triees.csv') 

# Créer des boutons et les placer sur l'image
buttons = []
for (x, y, station_name) in stations:
    button = tk.Button(frame, text="", width=1, height=1, command=lambda name=station_name: on_station_click(name))
    buttons.append(button)
    button.place(x=x, y=y)

# Empêcher le canvas et la frame de redimensionner avec la fenêtre
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Démarrer la boucle principale Tkinter
root.mainloop()
