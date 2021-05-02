from numpy import *
from pandas import *
import time
import statistics
import json
from matplotlib import pyplot
from pathlib import *

def distri_per_line(line, tab):
	for i in range (len(line)):
		if (int(line[i])==1)and (tab[i][1]==True):
			tab[i][0]+=1
			tab[i][1]=False
		else :
			if(int(line[i])==0)and (tab[i][1]==False):
				tab[i][1]=True
	return tab
	
def clean(tab):
	final_tab={}
	for i in range (len(tab)):
		if(tab[i][0] not in final_tab.keys()):
			final_tab[tab[i][0]]=1
		else :
			final_tab[tab[i][0]]+=1
	return final_tab
	
def distance_var(fichier):
	with open(fichier, "r") as f:
		distri=[]
		cpt=0
		cpt2=0
		data=False
		read=f.readline().split()
		final_list=[]
		while(read):
			if("-----" in read):
				cpt+=1
				if (cpt%2!=0):
					if (len(final_list)!=0):
						distri.append(clean(final_list))
					cpt2=0
					final_list=[]
					data=False
				else :
					data=True
			if (data==True):
				if ("-----" not in read):
					if cpt2==0:
						for i in range (len(read)):
							final_list.append([0,True])
					final_list=distri_per_line(read, final_list)
					cpt2+=1
			read=f.readline().split()
			if(read==[]):
				distri.append(clean(final_list))
		return distri

def mean_val(lis):
	som=0
	for i in lis:
		som+=i
	return som/len(lis)
	
def complete_dic(dic):
	key=[]
	for d in dic :
		for k in d.keys():
			if k not in key:
				key.append(k)
	for d in dic :
		for k in key:
			if k not in d.keys():
				d[k]=0
				
	return dic
		
def mean_distri(dic):
	mean_list=[]
	for d in dic :
		dic_temp={}
		dic2=complete_dic(d)
		for i in dic2 :
			for cle, val in i.items():
				if cle not in dic_temp.keys():
					dic_temp[cle]=[val]
				else :
					dic_temp[cle].append(val)
		mean_list.append(dic_temp)
	for m in mean_list :
		for k in m.keys():
			m[k]=mean_val(m[k])
	return mean_list

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
#print(lis_var)
lis_var_mean=mean_distri(lis_var)
print(lis_var_mean)

s=Path("ex2_res_distri_multi_infected_"+fichier+".txt")
with open (s, "w") as f:
	json.dump(variance, f)
	f.write("\n")
	json.dump(lis_var_mean,f)
'''
#df = DataFrame()
#df['c']=Series(lis_var_mean.tolist(), index=variance)
#df['c'].plot(label="duree_epidemie")
#pyplot.legend()
#pyplot.show()
'''