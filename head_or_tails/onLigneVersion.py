#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import serverModesdejeu as mdj


mdj.pygame.init()
width, height = mdj.pygame.display.Info().current_w, mdj.pygame.display.Info().current_h
width = width/2
height = height/2
#fenetre = mdj.pygame.display.set_mode((width,height))
mdj.menuPrincipale(width,height)
mdj.pygame.quit()



