from numpy import *
from pandas import *
import time
import statistics
import json
from matplotlib import pyplot
from pathlib import *

def distance_var(fichier):
	with open(fichier, "r") as f:
		distance=[]
		cpt=0
		data=False
		read=f.readline().split()
		final_list=[]
		while(read):
			if("-----" in read):
				cpt+=1
				if (cpt%2!=0):
					if (len(final_list)!=0):
						distance.append(len(final_list))
					final_list=[]
					data=False
				else :
					data=True
			if (data==True):
				if ("-----" not in read):
					final_list.append(read)
			read=f.readline().split()
			if (read==[]):
				distance.append(len(final_list))
		return distance
		

fichier=input("Nom du fichier : ")
mini=int(input("mini : "))
pas=int(input("pas : "))
limit=0
variance=[]
while (limit<30):
	variance.append(mini)
	mini+=pas
	limit+=1
lis_var=[]
for j in variance :
	fichier2=Path(fichier+str(j)+".txt")
	print(fichier2)
	dist=distance_var(fichier2)
	lis_var.append(dist)
	
lis_var=array(lis_var)
lis_var_mean=lis_var.mean(axis=1)
print("lis_var = ", lis_var)
print("lis_var_mean = ",lis_var_mean)
print("variance = ", variance)

s=Path("ex2_res_duree_epi_" + fichier+".txt")
with open (s, "w") as f:
	json.dump(variance, f)
	f.write("\n")
	json.dump(lis_var_mean.tolist(),f)
