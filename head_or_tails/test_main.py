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

print("\n WELCOME INTO OUR PROJECT HEAD OR TAILS\n")

direct = raw_input("\n Do you want to play online directly ? [Y/n] : ")
memory = 30
bch_L = []
percent = []
success = 0
bar = [0]
predictor = prd.Predictor(memory)
res_L = []
nb_0_and_1 = [0,0]

if "Y" in direct:
    print("\n To stop the game please enter \"end\" \n")
    buffert=""
    while buffert!="end":
        res_L.append(predictor.One_for_All(bch_L))
        buffert = raw_input("\n Your turn, enter 0 or 1 we will try to predict it : ")
        if buffert!="end" and len(buffert) == 1 and (buffert == "0" or buffert =="1"):
            bch_L.append(int(buffert))
            nb_0_and_1[bch_L[-1]] += 1
            print("\n Our prediction was :" +str(res_L[-1]))
            if res_L[-1] == bch_L[-1]:
                success+= 1
                bar.append(bar[-1]+1)
                percent.append(float(success)*100/(len(bch_L)))
            else:
                bar.append(bar[-1]-1)
                percent.append(float(success)*100/(len(bch_L)))
        elif buffert!="end" :
            print("Erreur, veuillez saisir uniquement 0 ou 1 svp sans espace ou end pour arreter")
            buffert=""
else:
    print("\nThose are benchmarks you have with a description. Please enter a name for your benchmark. If the name is present here it's the corresponding benchmark, else you will create a new benchmark with this name.\n ")
    os.chdir("./benchmarks")
    
    bch_available = os.listdir("files")
    print(bch_available)
    
    bchName = str(raw_input("\nHere enter the name : "))

    get_bch(bch_L,bchName,bch_available)
    
    os.chdir("../")

    t0 = time.clock()

    for turn in range(0,len(bch_L)):
        res_L.append(predictor.all_bits_pattern_Memory_optimised(bch_L[:turn],0))
        # res_L.append(predictor.predict(bch_L[:turn]))
        nb_0_and_1[bch_L[turn]]+=1
        if res_L[turn] == bch_L[turn]:
            success+= 1
            bar.append(bar[-1]+1)
            percent.append(float(success)*100/(turn+1))
        else:
            bar.append(bar[-1]-1)
            percent.append(float(success)*100/(turn+1))

    t1 = time.clock()

print("\nLe nombre total de 0 est : " + str(nb_0_and_1[0]))
print("\nLe nombre total de 1 est : " + str(nb_0_and_1[1]) + "\n")

print("\nLe temps d'execution est : "+str(t1-t0) + "\n")

print(predictor)

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


