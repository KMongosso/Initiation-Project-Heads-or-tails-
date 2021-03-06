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

memory = 500
temps_all_bits_pattern_optimised = []
#temps_n_bits_memory = []
temps_5 = []
for aka in range(1,1501):
    print(aka)
    bch_L = []
    predictor = prd.Predictor(memory)
    res_L = []

    bchName = "cmpTimeBch"
    
    size = aka
    os.chdir("./benchmarks")
    bch.randomBenchmark(bch_L,bchName,size)
    os.chdir("../")

    t0 = time.clock()

    for turn in range(0,len(bch_L)):
        res_L.append(predictor.all_bits_pattern_Memory_optimised(bch_L[:turn]))

    t1 = time.clock()
    temps_all_bits_pattern_optimised.append(t1-t0)

######################################################################################################
    #bch_L = []
    #predictor = prd.Predictor(memory)
    #res_L = []

    #bchName = "cmpTimeBch.txt"

    #os.chdir("./benchmarks")
    #bch.load_bch(bch_L,bchName)
    #os.chdir("../")

    #t0 = time.clock()

    #for turn in range(0,len(bch_L)):
        #res_L.append(predictor.n_bits_pattern_Memory(bch_L[:turn],2))

    #t1 = time.clock()
    #temps_n_bits_memory.append(t1-t0)

########################################################################################################

    #bch_L = []
    predictor = prd.Predictor(memory)
    res_L = []

    #bchName = "cmpTimeBch.txt"

    #os.chdir("./benchmarks")
    #bch.load_bch(bch_L,bchName)
    #os.chdir("../")

    t0 = time.clock()

    for turn in range(0,len(bch_L)):
        res_L.append(predictor.n_bits_pattern_Memory(bch_L[:turn],5))

    t1 = time.clock()
    temps_5.append(t1-t0)

#######################################################################################################
plt.plot(range(1,len(temps_5)+1),temps_all_bits_pattern_optimised,linewidth=2,label ="all_bits_pattern_Memory_optimised" )
#plt.plot(range(1,len(temps_5)+1),temps_n_bits_memory,linewidth=2,label ="2_bits_pattern_Memory", color="m" )
plt.plot(range(1,len(temps_5)+1),temps_5,linewidth=2,label ="n_bits_pattern_Memory", color="m" )
titre = "Temps d execution en fonction de la taille du fichier"
plt.title(titre)
plt.xlabel("Taille du fichier (nombre de 0 et 1 au total)")
plt.ylabel("Temps (en secondes)")
#plt.axis([0,1005,0,0.25])
plt.autoscale()

plt.legend(loc = 0)
#plt.show()
plt.savefig("temps_fonction_taille.png")
plt.close()
