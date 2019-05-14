import pygame
import os, inspect
from pygame.transform import scale

#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")


# Setup
pygame.init()

# Define some colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED   = [255, 0, 0]
BLUE  = [0 , 0 , 255]

police = pygame.font.SysFont("arial", 15)
 
 
print(scriptDIR)
 
 
# Set the width and height of the screen [width,height]
screeenWidth = 800
screenHeight = 400
screen = pygame.display.set_mode((screeenWidth,screenHeight))
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(True) 
 
fond = pygame.image.load(os.path.join(assets, "fond.png"))
poisson = pygame.image.load(os.path.join(assets, "fish1.png")).convert()
poisson2 = pygame.image.load(os.path.join(assets, "fish2.png")).convert()
poisson3 = pygame.image.load(os.path.join(assets, "fish3.png")).convert()
decor = pygame.image.load(os.path.join(assets, "decor.png")).convert()
decor1 = pygame.image.load(os.path.join(assets, "decor1.png")).convert()
decor1 = pygame.image.load(os.path.join(assets, "decor1.png")).convert()
plant1 = pygame.image.load(os.path.join(assets, "plant1.png")).convert()
plant2 = pygame.image.load(os.path.join(assets, "plant2.png")).convert()


poisson.set_colorkey((170, 238, 255))
poisson2.set_colorkey((170, 238, 255))
poisson3.set_colorkey((170, 255, 238))
decor.set_colorkey((255, 0, 0))
decor1.set_colorkey((255, 7, 0))
plant1.set_colorkey((255, 7, 0))
plant2.set_colorkey((255, 7, 0))


decor_x = 150
decor_y = 200
decor1_x = 400
decor1_y = 100
plant1_x = 700
plant1_y = 300
plant2_x = 300
plant2_y = 50
poisson1_x  = 100
poisson1_y  = 200
poisson1_vx = -2
poisson2_x  = 50
poisson2_y  = 150
poisson2_vx = -4
poisson3_x  = 0
poisson3_y  = 0
poisson3_vx = -1
sprite = 0
 
poisson2 = pygame.transform.flip(poisson2,True,False)
poisson3 = pygame.transform.flip(poisson3,True,False)
# -------- Main Program Loop -----------
while not done:
   
   # récupère la liste des touches claviers appuyeées sous la forme liste bool
   pygame.event.pump()
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
      
   
    # LOGIQUE
 
   poisson1_x += poisson1_vx
   if ( poisson1_x < 200 ):
      poisson1_x = 200
      poisson1_vx = -poisson1_vx
      poisson = pygame.transform.flip(poisson,True,False)
   if ( poisson1_x > 600-113 ):
      poisson1_x = 600-113
      poisson1_vx = -poisson1_vx
      poisson = pygame.transform.flip(poisson,True,False)
      
   poisson2_x += poisson2_vx
   if ( poisson2_x < 100 ):
      poisson2_x = 100
      poisson2_vx = -poisson2_vx
      poisson2 = pygame.transform.flip(poisson2,True,False)
   if ( poisson2_x > 500 ):
      poisson2_x = 500
      poisson2_vx = -poisson2_vx
      poisson2 = pygame.transform.flip(poisson2,True,False)

   poisson3_x += poisson3_vx
   if ( poisson3_x < 0 ):
      poisson3_x = 0
      poisson3_vx = -poisson3_vx
      poisson3 = pygame.transform.flip(poisson3,True,False)
   if ( poisson3_x > 600 ):
      poisson3_x = 600
      poisson3_vx = -poisson3_vx
      poisson3 = pygame.transform.flip(poisson3,True,False)

 
    # DESSIN
    
   # affiche la zone de rendu au dessus de fenetre de jeu
   screen.blit(fond,(0,0))
   
   #tt = pygame.rect(poisson1_x,poisson1_y,10,10)
   screen.blit(poisson, (poisson1_x,poisson1_y))   
   screen.blit(poisson2, (poisson2_x,poisson2_y))
   screen.blit( scale(plant1,(75,125)), (plant1_x,plant1_y))
   screen.blit( scale(plant2,(100,350)), (plant2_x,plant2_y)) 
   screen.blit( scale(poisson3,(200,200)), (poisson3_x,poisson3_y)) 
   screen.blit( scale(decor,(150,150)), (decor_x,decor_y))
   screen.blit( scale(decor1,(300,300)), (decor1_x,decor1_y))

    # Go ahead and update the screen with what we've drawn.
   pygame.display.flip()
 
    # Limit frames per second
   clock.tick(60)
 
# Close the window and quit.
pygame.quit()