import csv

# Fonction pour lire le fichier texte, trier et écrire dans un CSV
def trier_et_convertir_fichier_txt_vers_csv(fichier_txt, fichier_csv):
    donnees = []
    
    # Lire le fichier texte
    with open(fichier_txt, 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            # Séparer la ligne en x, y, et nom de la gare
            x, y, nom_gare = ligne.strip().split(';')
            # Remplacer les '@' dans le nom de la gare par des espaces
            nom_gare = nom_gare.replace('@', ' ')
            # Ajouter à la liste des données
            donnees.append((int(x), int(y), nom_gare))
    
    # Trier les données par x puis par y (ou seulement par x ou par y)
    donnees_triees = sorted(donnees, key=lambda station: (station[0], station[1]))

    # Écrire les données dans un fichier CSV
    with open(fichier_csv, 'w', newline='', encoding='utf-8') as fichier_csv:
        writer = csv.writer(fichier_csv)
        # Écrire l'en-tête
        writer.writerow(['x', 'y', 'nom_de_la_gare'])
        # Écrire les lignes triées
        writer.writerows(donnees_triees)

# Appel de la fonction pour trier et convertir
fichier_txt = 'pospoints.txt'  # Remplace par ton fichier .txt
fichier_csv = 'stations_triees.csv'  # Nom du fichier CSV de sortie
trier_et_convertir_fichier_txt_vers_csv(fichier_txt, fichier_csv)
