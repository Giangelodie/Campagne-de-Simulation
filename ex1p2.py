from subprocess import run
import sys
from subprocess import PIPE
from pathlib import *


nom_fichier=input("Nom du fichier : ")

taille=len(sys.argv)-1

parametre=input("Paramètre à faire varier : ")
mini=int(input("mini : "))
pas=int(input("pas : "))
limit=0
variance=[]
while (limit<30):
	variance.append(mini)
	mini+=pas
	limit+=1
print(variance)

for j in variance :
	s=str(j)
	para=parametre+ "="+ s
	nom_fichier2=Path(nom_fichier+s+".txt")
	print(nom_fichier2)

	liste_ini=['java', '-jar', 'Virus_old.jar', '-stop_all_sane=1', '-printout=2', '-gui=0', '-nb_snapshots=5000']

	for i in range (1, taille):
		liste_ini.append(sys.argv[i])
	
	liste_ini.append(para)
	print(liste_ini)

	for i in range (50):
		res = run(liste_ini, stdout=PIPE, stderr=PIPE)
		with open(nom_fichier2,'a+') as f:
			f.write(res.stdout.decode('utf-8'))