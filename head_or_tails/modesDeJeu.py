#!/usr/bin/env python
#-*- coding: utf-8 -*-

from benchmarks import newbch as bch
from predictors import class_Predictor as prd 
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *

def menuPrincipale(width, height, fenetre):
    fenetre = pygame.display.set_mode((width,height))
    fond = pygame.image.load("graphics/fondBunny.png").convert()
    fond = pygame.transform.smoothscale(fond, (width, height))
    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            #Quitter
            if event.type == QUIT :
                continuer=0
                break

            if event.type ==  MOUSEBUTTONDOWN and event.button == 1 :
                if event.pos[0] > width/3.0 and event.pos[0]< width/1.2 and event.pos[1]> height/3.0 and event.pos[1] < height/0.5:
                    interactiveGame(width,height,fenetre)
                    fenetre = pygame.display.set_mode((width,height))
                    fond = pygame.image.load("graphics/fondBunny.png").convert()
                    fond = pygame.transform.smoothscale(fond, (width, height))
                    fenetre.blit(fond, (0,0))
                    pygame.display.flip()
                    
                    if event.pos[0] > 0 and event.pos[0]< width/3.0 and event.pos[1]> height/3.0 and event.pos[1] < height/0.5:
                        print("\nRAS GAAAAAAAANG\n")
    return

def afficheRes(percent,bar):
    plt.plot(percent,linewidth=2)
    titre = "Pourcentage de reussite cumule"
    plt.title(titre)
    plt.xlabel("n (n ieme prediction)")
    plt.ylabel("Pourcentage de reussite") 
    #plt.axis([0,len(percent),0,100])
    plt.autoscale()
    #plt.savefig("Pourcent_cum.png") 
    
    plt.figure(2)
    x = [float(percent[-1]),float(100-percent[-1])]
    plt.pie(x, labels=["Succes","Echec"],colors=["green","red"],autopct ='%1.3f%%', shadow=True)
    titre = "Pourcentage de succes et d echec "
    plt.title(titre)
    #plt.savefig("Pie.png")
    
    plt.figure(3)
    plt.scatter(range(0,len(bar)),bar)
    titre = "Solde en euros cumule"
    plt.title(titre)
    plt.xlabel("n (n ieme prediction)")
    plt.ylabel("Solde (en euros)") 
    #plt.axis([-5,len(bar)+3,min(bar)-3,max(bar)+5])
    plt.autoscale()
    #plt.savefig("scat.png")
    
    plt.show()
    plt.close()
    
    return

def interactiveGame(width,height,fenetre):
    fenetre = pygame.display.set_mode((width,height))
    online = pygame.image.load("graphics/online.png").convert()
    online = pygame.transform.smoothscale(online, (width, height))
    fenetre.blit(online, (0,0))
    pygame.display.flip()
    
    memory = 6
    bch_L = []
    percent = []
    success = 0
    bar = [0]
    predictor = prd.Predictor(memory)
    nb_0_and_1 = [0,0]
    res_L = []

    continuer = 1
    while continuer:
        for event in pygame.event.get():
            #Quitter
            if event.type == QUIT:
                continuer = 0
                break

            if event.type ==  MOUSEBUTTONDOWN and event.button == 1 :
                if event.pos[0] > width/2.0 and event.pos[1]>height/2.0:
                    res_L.append(predictor.all_bits_pattern_Memory_optimised(bch_L,0))
                    bch_L.append(0)
                    nb_0_and_1[bch_L[-1]] += 1
                    if res_L[-1] == bch_L[-1]:
                        bar.append(bar[-1]-1)
                        percent.append(float(success)*100/(len(bch_L)))
                    else:
                        success+= 1
                        bar.append(bar[-1]+1)
                        percent.append(float(success)*100/(len(bch_L)))
                        
                    font=pygame.font.SysFont("broadway",60,bold=False,italic=False)
                    text=font.render(str(bar[-1]),1,(255,255,255))
                    fenetre.blit(online, (0,0))
                    fenetre.blit(text,(width/9,height/6))
                    pygame.display.flip()
                        
                elif event.pos[0] < width/2.0 and event.pos[1]>height/2.0:
                    res_L.append(predictor.all_bits_pattern_Memory_optimised(bch_L,0))
                    bch_L.append(1)
                    nb_0_and_1[bch_L[-1]] += 1
                    if res_L[-1] == bch_L[-1]:
                        bar.append(bar[-1]-1)
                        percent.append(float(success)*100/(len(bch_L)))
                    else:
                        success+= 1
                        bar.append(bar[-1]+1)
                        percent.append(float(success)*100/(len(bch_L)))
                        
                    font=pygame.font.SysFont("broadway",60,bold=False,italic=False)
                    text=font.render(str(bar[-1]),1,(255,255,255))
                    fenetre.blit(online, (0,0))
                    fenetre.blit(text,(width/9,height/6))
                    pygame.display.flip()

                elif event.pos[0] < width/3.0 and event.pos[1]< height/3.0:
                    print( nb_0_and_1)
                    afficheRes(percent,bar)
                    continuer = 0
                    break
    
    return
