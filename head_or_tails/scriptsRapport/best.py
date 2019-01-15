#!/usr/bin/env python
#-*- coding: utf-8 -*-

from benchmarks import newbch as bch
import os
from predictors import class_Predictor as prd 
import matplotlib.pyplot as plt
import time

def get_bch(bch_L,bchName,bch_available):
    if (bchName in bch_available):
        print("\nYou have chosen a benchmark in the list above ! \n")
        bch.load_bch(bch_L,bchName)
    else:
        print("\nYou have chosen to make your own benchmark\n")
        decision = raw_input("Do you want to enter your benchmark by hand ? [Y/n] : ")
        if "Y" in decision:
            bch.handMadeBenchmark(bch_L,bchName)
            return
            
        size = int(raw_input("\nQuelle doit etre au plus la taille de votre benchmark ? : "))
        decision = raw_input("Do you want to make it all randomly ? [Y/n] : ")
        if "Y" in decision:
            bch.randomBenchmark(bch_L,bchName,size)
            return
                
        bch.benchmarks(bch_L,bchName,size)

bchName_L = [] 
memory = 6

for bchName in bchName_L:
    bch_L = []
    percent = []
    success = 0
    bar = [0]
    predictor = prd.Predictor(memory)
    res_L = []
    
    os.chdir("./benchmarks")
    bch.load_bch(bch_L,bchName)
    os.chdir("../")

    for turn in range(0,len(bch_L)):
        res_L.append(predictor.all_bits_pattern_Memory_optimised(bch_L[:turn]))
        # res_L.append(predictor.predict(bch_L[:turn]))
        nb_0_and_1[bch_L[turn]]+=1
        if res_L[turn] == bch_L[turn]:
            success+= 1
            bar.append(bar[-1]+1)
            percent.append(float(success)*100/(turn+1))
        else:
            bar.append(bar[-1]-1)
            percent.append(float(success)*100/(turn+1))

plt.plot(percent,linewidth=2)
titre = "Pourcentage de reussite cumule"
plt.title(titre)
plt.xlabel("n (n ieme prediction)")
plt.ylabel("Pourcentage de reussite") 
#plt.axis([0,len(percent),0,100])
plt.autoscale() 
          
plt.figure(2)
x = [float(percent[-1]),float(100-percent[-1])]
plt.pie(x, labels=["Succes","Echec"],colors=["green","red"],autopct ='%1.3f%%', shadow=True)
titre = "Pourcentage de succes et d echec "
plt.title(titre)

plt.figure(3)
plt.scatter(range(0,len(bar)),bar)
titre = "Solde en euros cumule"
plt.title(titre)
plt.xlabel("n (n ieme prediction)")
plt.ylabel("Solde (en euros)") 
#plt.axis([-5,len(bar)+3,min(bar)-3,max(bar)+5])
plt.autoscale()

plt.show()
plt.close()


