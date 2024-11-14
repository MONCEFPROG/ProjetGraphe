from AlgoGraphe import initGraph, checkConnexity, bellmanFord, plusCourtChemin, prim
import pandas as pd

# Charger les données des stations
stations_df = pd.read_csv("./stationsV2.csv")

# Initialiser le graphe
graphe = initGraph("./liensV2.csv")

# Obtenir les entrées de l'utilisateur pour les stations de départ et d'arrivée
nom_station_depart = input("Entrez la station de départ: ")
nom_station_arrivee = input("Entrez la station d'arrivée: ")

# Trouver les IDs des stations
try:
    id_station_depart = stations_df[stations_df['nom_sommet'] == nom_station_depart].iloc[0]['num_sommet']
    id_station_arrivee = stations_df[stations_df['nom_sommet'] == nom_station_arrivee].iloc[0]['num_sommet']
except IndexError:
    print("L'une des stations saisies n'existe pas. Veuillez vérifier les noms des stations.")
    exit()



# 3.1 Connexité
connexite = checkConnexity(graphe)
if connexite:
    print("Le graphe est connexe")
else: 
    print("Le graphe n'est pas connexe")



# 3.2 Le plus court chemin
# Calculer le plus court chemin
distances, predecesseurs = bellmanFord(id_station_depart, graphe)
chemin = plusCourtChemin(id_station_depart, id_station_arrivee, predecesseurs)

# Afficher l'itinéraire
if chemin:
    print(f"Vous êtes à {nom_station_depart}.")
    for i in range(len(chemin) - 1):
        station_actuelle = stations_df[stations_df['num_sommet'] == chemin[i]].iloc[0]
        station_suivante = stations_df[stations_df['num_sommet'] == chemin[i + 1]].iloc[0]
        if station_actuelle['numero_ligne'] != station_suivante['numero_ligne']:
            print(f"A {station_actuelle['nom_sommet']}, changez et prenez la ligne {station_suivante['numero_ligne']} direction {station_suivante['nom_sommet']}.")
    temps_de_trajet_minutes = round(distances[id_station_arrivee] / 60)  # Convertir les secondes en minutes et arrondir à l'entier
    print(f"Vous devriez arriver à {nom_station_arrivee} dans environ {temps_de_trajet_minutes} minutes.")
else:
    print("Aucun chemin trouvé.")