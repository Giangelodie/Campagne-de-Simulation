from numpy import *
from pandas import *
import time
import statistics
import json
from matplotlib import pyplot
from pathlib import *

fichier=input("Nom du fichier :")
s=Path("ex2_res_duree_epi_"+fichier+".txt")
with open (s, "r") as f:
	variance=json.loads(f.readline())
	lis_var_mean=json.loads(f.readline())
	df = DataFrame()
	df['c']=Series(lis_var_mean, index=variance)
	df['c'].plot(label="duree_epidemie")
	pyplot.legend()
	pyplot.show()