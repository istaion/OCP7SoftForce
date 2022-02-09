import csv
from time import time

t1 = time()
#  Récupération des données actions

chemin = 'donnees/actions.csv'

listeaction = []

with open(chemin, 'r') as CSVFILE:
    csvreader = csv.reader(CSVFILE)
    next(csvreader)
    for ligne in csvreader:
        listeaction.append([ligne[0], int(float(ligne[1])*100), int(round(float(ligne[2])*float(ligne[1])*100))])

argent = 50000
nombre = len(listeaction)
tableau = []

for i in range(argent+1):
    tableau.append([0])

for n in range(nombre):
    for p in range(argent+1):
        if p >= listeaction[n][1]:
            tableau[p].append(max(tableau[p][n], tableau[p-listeaction[n][1]][n] + listeaction[n][2]))
        else:
            tableau[p].append(tableau[p][n])


soluce=(0,0)
for i in range(argent+1):
    if tableau[i][nombre] > soluce[1]:
        soluce = (i, tableau[i][nombre])


def resolution(p, a, res):
    if tableau[p][a] == 0:
        print(res)
    else:
        if tableau[p][a] == tableau[p][a-1]:
            resolution(p, a-1, res)
        else:
            res.append(a-1)
            resolution(p-listeaction[a-1][1], a-1, res)


print(resolution(argent, nombre, []))


t = time() - t1
print("le programme a mit", round(t, 2), "s à s'éxecuter")