#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import os
import random

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

def compareLists(L1,L2):
        for i in range(0,len(L1)):
                if L1[i] != L2[i]:
                        return 0
        return 1

def makeBenchmarkFile(bch_L,bchName):
	bch_str=""
	for i in range(0,len(bch_L)-1):
		bch_str += str(bch_L[i]) + " "
  
	bch_str += str(bch_L[-1])
	os.chdir("files")
	bchFile = open(bchName,"w")
	bchFile.write(bch_str)
	bchFile.close()
	os.chdir("../")
 
def randomBenchmark(bch_L,bchName,size):
	bchName += ".txt"
	print("\nYou have chosen to make it randomly\n")
	for i in range(0,size):
		bch_L.append(random.randint(0,1))
 
	makeBenchmarkFile(bch_L,bchName)
      
def handMadeBenchmark(bch_L, bchName):
	print("\nYou have chosen to make it by hand\n")
	print("Please, you have to enter a succession of only 1 and 0 without spaces \n")
	bch_str = str(raw_input("Enter here : "))
	bch_str_new = ""
      
	for i in range(0,len(bch_str)):
		if (bch_str[i] =='1' or bch_str[i] == '0'):
			bch_L.append(int(bch_str[i]))
			bch_str_new += bch_str[i]+" "
      
	bchName += ".txt"
  
	os.chdir("files")
	bchFile = open(bchName,"w")
	bchFile.write(bch_str_new)
	bchFile.close()
	os.chdir("../")
  
def load_bch(bch_L,bchName):
	os.chdir("files")
	bchFile = open(bchName,"r")
	bch_str = bchFile.read()
	bchFile.close()
	os.chdir("..")

	for i in range(0,len(bch_str)):
		if (bch_str[i] == '0' or bch_str[i] =='1') :
			bch_L.append(int(bch_str[i]))


def benchmarks(bch_L,bchName,size):
        print("\n Commencons la personalisation de votre benchmark ! ")
        bchName+=".txt"
        motifs_L = []
        taille_motifs_L = []

        nb_pattern = int(raw_input("\nCombien de motifs differents voulez vous voir apparaitre dans le benchmark : "))

        condition = 1
        while(condition):
                total = 0
                nb_motifs = 0
                for i in range(0, nb_pattern):
                        print("\nInformations concernants le " + str(i+1) + " ieme motifs ! ")
                        motifs_L.append(raw_input("Veuillez entrer le motif : "))
                        taille_motifs_L.append(int(raw_input("Combien de fois au minimum voulez vous que ce motif apparaissent dans le benchmark : ")))
                        total += len(motifs_L[i]) * taille_motifs_L[i]
                        nb_motifs += taille_motifs_L[i]
                        
                if total > size:
                        print("\nAttention ! Le nombre total de 0 et 1 qui composent votre demande depasse la taille saisie ! Veuillez resaisir svp")
                        print("RAPPEL : Le motif ne doit etre compose que de 0 et 1, pas d espace")
                else:
                        condition = 0

        n = (size-total)/(nb_motifs-1)
        rep = raw_input("\nVoulez vous un espacement regulier entre l apparition des motifs ? [Y/n] ")
        repOrdre = raw_input("\nVoulez vous respecter l ordre d apparition des motifs (ils apparaissent tous dans l ordre rentre ) [Y/n] : ")
        if "Y" in repOrdre:
                if "Y" in rep:
                        space = int(raw_input("Saisissez la taille de cet espacement, il doit etre compris entre 0 et " +str(n) + " : "))
                cpt = -1
                for i in taille_motifs_L :
                        cpt+=1
                        for j in range(0,i):
                                for f in motifs_L[cpt]:
                                        bch_L.append(int(f))
                                if "Y" in rep:
                                        for k in range(0,space):
                                                bch_L.append(random.randint(0,1))
                                else:
                                        for k in range(0,random.randint(0,n)):
                                                bch_L.append(random.randint(0,1))

        else:
                if "Y" in rep:
                        space = int(raw_input("Saisissez la taille de cet espacement, il doit etre compris entre 0 et " +str(n) + " : "))
                print("\nLes motifs vont apparaitre dans n importe quel ordre et se melanger tout au long du benchmark !")
                cpt=[]
                #lesindices = cpt
                for ialea in range(0, len(taille_motifs_L)):
                        cpt.append(0)
                        #lesindices[ialea]= ialea
                while (len(bch_L) < size and len(motifs_L)>= 1 and cpt != taille_motifs_L):
                        ialea = random.randint(0,len(motifs_L)-1)
                        while(cpt[ialea]==taille_motifs_L[ialea]):
                                ialea = random.randint(0,len(motifs_L)-1)
                        for f in motifs_L[ialea]:
                                bch_L.append(int(f))
                        cpt[ialea]+=1
                        if "Y" in rep:
                                for k in range(0,space):
                                        bch_L.append(random.randint(0,1))
                        else:
                                for k in range(0,random.randint(0,n)):
                                        bch_L.append(random.randint(0,1))                                        
        while(len(bch_L) > size):
                bch_L.pop()

        print("\nLA TAILLE EFFECTIVE FINALE DU BENCHMARK COMPTE TENUE DE CE QUE VOUS EXIGE EST : " + str(len(bch_L)) + " !\n")

        makeBenchmarkFile(bch_L, bchName)
