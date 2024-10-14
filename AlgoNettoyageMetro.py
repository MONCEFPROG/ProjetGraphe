import csv

# Fichiers de sortie
fichier_stations_csv = 'stations.csv'
fichier_liens_csv = 'liens.csv'

# Listes pour stocker les données nettoyées
stations = []
liens = []

# Chemin vers le fichier source
fichier_texte = 'metro.txt'

# Lecture et nettoyage du fichier texte
with open(fichier_texte, 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        
        # Si la ligne décrit un sommet (station)
        if ligne.startswith('V '):
            # Supprimer le 'V' et diviser par les points-virgules
            partie = ligne[2:].split(';')
            if len(partie) >= 3:
                sommet_parties = partie[0].split()
                num_sommet = sommet_parties[0]  # Numéro du sommet
                nom_sommet = " ".join(sommet_parties[1:]).replace(',', '')  # Nom du sommet
                numero_ligne = partie[1].strip()  # Numéro de ligne
                terminus = partie[2].strip()  # True/False pour terminus
                branchement = partie[3].strip() if len(partie) > 3 else "0"  # Branchement (optionnel)

                # Ajouter à la liste des stations
                stations.append([num_sommet, nom_sommet, numero_ligne, terminus, branchement])

        # Si la ligne décrit une arête (lien entre stations)
        elif ligne.startswith('E '):
            # Supprimer le 'E' et diviser par les espaces
            parties = ligne[2:].split()
            if len(parties) == 3:
                num_sommet1 = parties[0]  # Première station
                num_sommet2 = parties[1]  # Deuxième station
                temps_en_secondes = parties[2]  # Temps en secondes

                # Ajouter à la liste des liens
                liens.append([num_sommet1, num_sommet2, temps_en_secondes])

# Écriture des stations dans un fichier CSV
with open(fichier_stations_csv, 'w', newline='', encoding='utf-8') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['num_sommet', 'nom_sommet', 'numero_ligne', 'terminus', 'branchement'])
    writer.writerows(stations)

# Écriture des liens dans un autre fichier CSV
with open(fichier_liens_csv, 'w', newline='', encoding='utf-8') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['num_sommet1', 'num_sommet2', 'temps_en_secondes'])
    writer.writerows(liens)

print("Fichiers CSV créés : stations.csv et liens.csv")
