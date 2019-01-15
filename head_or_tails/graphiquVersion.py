#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import modesDeJeu as mdj


mdj.pygame.init()
width, height = mdj.pygame.display.Info().current_w, mdj.pygame.display.Info().current_h
width = width/2
height = height/2
fenetre = mdj.pygame.display.set_mode((width,height))
mdj.menuPrincipale(width,height,fenetre)
mdj.pygame.quit()


print("\nThose are benchmarks you have with a description. Please enter a name for your benchmark. If the name is present here it's the corresponding benchmark, else you will create a new benchmark with this name.\n ")
bch.os.chdir("./benchmarks")

bch_available = mdj.os.listdir("files")
print(bch_available)

bchName = str(raw_input("\nHere enter the name : "))

bch.get_bch(bch_L,bchName,bch_available)

mdj.os.chdir("../")
    
t0 = time.clock()

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
        
t1 = time.clock()

print("\nLe nombre total de 0 est : " + str(nb_0_and_1[0]))
print("\nLe nombre total de 1 est : " + str(nb_0_and_1[1]) + "\n")

print("\nLe temps d'execution est : "+str(t1-t0))


