from subprocess import run
import sys
from subprocess import PIPE
from pathlib import *

nom_fichier=Path(input("Nom du fichier : "))

taille=len(sys.argv)-1

liste_ini=['java', '-jar', 'Virus_old.jar', '-stop_all_sane=1', '-printout=2', '-gui=0', '-nb_snapshots=5000']

for i in range (1, taille):
	liste_ini.append(argv[i])

for i in range (1000):
	res = run(liste_ini, stdout=PIPE, stderr=PIPE)
	with open(nom_fichier,'a+') as f:
		f.write(res.stdout.decode('utf-8'))