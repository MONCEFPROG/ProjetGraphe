import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Lire les données des stations et des connexions
stations_df = pd.read_csv('stations.csv')
connexions_df = pd.read_csv('liens.csv')

# Initialisation du graphe
G = nx.Graph()

# Ajouter les stations comme noeuds
for index, row in stations_df.iterrows():
    G.add_node(row['id'], nom_station=row['nom_station'], ligne=row['ligne'],
               terminus=row['terminus'], branchement=row['branchement'])

# Ajouter les connexions comme arêtes avec le temps comme poids
for index, row in connexions_df.iterrows():
    G.add_edge(row['station1'], row['station2'], weight=row['temps_en_secondes'])

# Afficher quelques informations sur le graphe
print(f"Nombre de stations: {G.number_of_nodes()}")
print(f"Nombre de connexions: {G.number_of_edges()}")

# Visualiser le graphe
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, seed=42)  # Layout pour la disposition des noeuds
nx.draw(G, pos, with_labels=True, node_size=50, node_color='blue', font_size=8, edge_color='gray')
plt.title("Graphique des stations de métro")
plt.show()
