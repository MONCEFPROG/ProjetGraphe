import pandas as pd
import matplotlib.pyplot as plt
import csv



def initGraph(filename):
    """
    :param filename: qui correspond au nom du fichier contentant les liens
    :return: un dictionnaire qui a pour clé le numéro du sommet et en valeur une liste de tuple avec le sommet relié et le temps
    """
    graph={}
    with open(filename, 'r') as f:
        csvReader = csv.reader(f)
        next(csvReader, None) # sauter l'en tête
        for row in csvReader:
            sommet1 = int(row[0])
            sommet2 = int(row[1])
            poids = float(row[2])

            if sommet1 not in graph:
                graph[sommet1] = []
            graph[sommet1].append((sommet2, poids))

            if sommet2 not in graph:
                graph[sommet2] = []
            graph[sommet2].append((sommet1, poids))

        return graph


def checkConnexity(graph) -> bool:
    """
    :param graph: prend en paramètre un graphe
    :return: booleen

    Fonction qui implémente un parcours en largeur pour vérifier si le graphe est connexe

    """
    if not graph: return False

    racine = next(iter(graph))
    visite = set()
    file = [racine]

    while file :
        current = file.pop(0)
        if current not in visite:
            visite.add(current)
            for voisin,poids in graph[current]:
                if voisin not in visite:
                    file.append(voisin)

    return len(graph) == len(visite)


def bellmanFord(source,graph):

    nbSommets = len(graph)
    longChemins = {s:float('inf') for s in graph} # initialise la longueur des chemins depuis chacun des sommets a l'infini
    predecesseurs = {s: None for s in graph} # initialise les predecesseurs
    longChemins[source] = 0 # initialise le sommet source a 0
    for i in range(nbSommets-1):
        for sommet in graph:
            for voisin,poids in graph[sommet]:
                if longChemins[sommet]+poids < longChemins[voisin]:
                    longChemins[voisin] = longChemins[sommet]+poids
                    predecesseurs[voisin] = sommet

    return longChemins,predecesseurs

def plusCourtChemin(source,destination,predecesseurs):

    if not predecesseurs : return None

    chemin=[]
    tmp = destination
    while tmp :
        if tmp == source :
            break
        chemin.append(tmp)
        tmp = predecesseurs[tmp]

    chemin.append(source)
    chemin.reverse()

    return chemin


def prim(graph):
    sommetsVisite = set()
    candidats = []  # aretes candidates
    cc = []  # sommets du acpm
    coutTotal = 0
    source = next(iter(graph)) # on attribue la source au premier element du graphe (pas important)

    sommetsVisite.add(source)
    for voisin,poids in graph[source] :
        candidats.append((source,voisin,poids)) # on ajoute les voisins du sommet de départ aux candidats

    while len(sommetsVisite) < len(graph) :
        plusPetiteArete = None
        for arrete in candidats:
            if arrete[1] not in sommetsVisite:
                if not plusPetiteArete or arrete[2] < plusPetiteArete[2] :
                    plusPetiteArete = arrete

        if not plusPetiteArete : break

        sommetSource,voisin,poids = plusPetiteArete
        sommetsVisite.add(voisin)
        cc.append(plusPetiteArete)
        coutTotal += poids

        for prochainVoisin,poids in graph[voisin]:
            if prochainVoisin not in sommetsVisite:
                candidats.append((voisin,prochainVoisin,poids))


    return cc,coutTotal

