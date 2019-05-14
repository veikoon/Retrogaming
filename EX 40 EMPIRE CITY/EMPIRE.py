import pygame
import os, inspect, random
from pygame.transform import scale

#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")


# Setup
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

police = pygame.font.SysFont("arial", 15)
 
 
print(scriptDIR)
 
 
# Set the width and height of the screen [width,height]
screeenWidth = 400
screenHeight = 300
screen = pygame.display.set_mode((screeenWidth,screenHeight))
 
pygame.display.set_caption("Empire City")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(True) 
 
fond = pygame.image.load(os.path.join(assets, "map.png"))
viseur =  pygame.image.load(os.path.join(assets, "viseur.png"))
bandit_rue2 = pygame.image.load(os.path.join(assets, "bandit_rue2.png"))
bandit_window4 = pygame.image.load(os.path.join(assets, "bandit_window4.png"))
fleche_droite = pygame.image.load(os.path.join(assets, "fleche_droite.png"))
fleche_gauche = pygame.image.load(os.path.join(assets, "fleche_gauche.png"))

temp = 0
T0 = 0
J_xdecor = 150
J_ydecor = 385
V_xecran = screeenWidth/2-45/2
V_yecran = screenHeight/2-52/2
bandit_rue2_x = random.randint(1,2000-62-60)
bandit_rue2_y = 686-157
spawn = True
zbeub = random.randint(1,4)
thug = random.randint(1,2)
if zbeub == 1:
   bandit_window_x = 790 
   bandit_window_y = 86
elif zbeub == 2:
   bandit_window_x = 1320 
   bandit_window_y = 259
elif zbeub == 3:
   bandit_window_x = 1910 
   bandit_window_y = 282
elif zbeub == 4:
   bandit_window_x = 330 
   bandit_window_y = 117
   
if thug == 1:
   mechant_x = bandit_rue2_x
   mechant_y = bandit_rue2_y
   mechantX = 62
   mechantY = 157
else:
   mechant_x = bandit_window_x
   mechant_y = bandit_window_y
   mechantX = 50
   mechantY = 74
 
# -------- Main Program Loop -----------
while not done:
   T0 = int(pygame.time.get_ticks()/1000)
   fleche_gauche_x = V_xecran-50
   fleche_gauche_y = V_yecran
   fleche_droite_x = V_xecran+45
   fleche_droite_y = V_yecran
   # récupère la liste des touches claviers appuyeées sous la forme liste bool
   pygame.event.pump()
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         done = True
         
   KeysPressed = pygame.key.get_pressed()
   
   if V_yecran >= 30:
      if KeysPressed[pygame.K_UP]:
         V_yecran -= 4
   else:
      if J_ydecor > 0:
         J_ydecor -= 4
      else: J_ydecor = 0
      
   if V_yecran <= 270-52:
      if KeysPressed[pygame.K_DOWN]:
         V_yecran += 4
   else:
      if J_ydecor < 685 - screenHeight :
         J_ydecor += 4
      else: J_ydecor = 685 - screenHeight
      
   if V_xecran >= 60:
      if KeysPressed[pygame.K_LEFT]:
         V_xecran -= 4
   else:
      if J_xdecor > 0:
         J_xdecor -= 4
      else: J_xdecor = 0
      
   if V_xecran <= 340-45:
      if KeysPressed[pygame.K_RIGHT]:
         V_xecran += 4
   else:
      if J_xdecor < 2000 - screeenWidth:
         J_xdecor += 4
      else: J_xdecor = 2000 - screeenWidth

   if KeysPressed[pygame.K_SPACE]:
      if V_xecran+J_xdecor >= mechant_x and V_xecran+J_xdecor <= mechant_x+mechantX and V_yecran+J_ydecor >= mechant_y and V_yecran+J_ydecor <= mechant_y+mechantY :
         spawn = False
         zbeub = random.randint(1,4)
         thug = random.randint(1,2)
         if zbeub == 1:
            bandit_window_x = 790 
            bandit_window_y = 86
         elif zbeub == 2:
            bandit_window_x = 1320 
            bandit_window_y = 259
         elif zbeub == 3:
            bandit_window_x = 1910 
            bandit_window_y = 282
         elif zbeub == 4:
            bandit_window_x = 330 
            bandit_window_y = 117
            
         if thug == 1:
            mechant_x = bandit_rue2_x
            mechant_y = bandit_rue2_y
            mechantX = 62
            mechantY = 157
         else:
            mechant_x = bandit_window_x
            mechant_y = bandit_window_y
            mechantX = 50
            mechantY = 74
         temp = T0
      V_yecran -= 10
   
   if T0 == temp+3:
      spawn = True
      
   print(spawn,"  ",T0,temp)
    # LOGIQUE
 
 
    # DESSIN
    
   # affiche la zone de rendu au dessus de fenetre de jeu
   zonejaune = pygame.Rect( J_xdecor, J_ydecor, screeenWidth, screenHeight )
   screen.blit(fond,(0,0),area = zonejaune)
   if spawn == True:
      if thug == 1:
         screen.blit(bandit_rue2,(bandit_rue2_x-J_xdecor,bandit_rue2_y-J_ydecor))
      else:
         screen.blit(bandit_window4,(bandit_window_x-J_xdecor,bandit_window_y-J_ydecor))
      
   screen.blit(viseur,(V_xecran,V_yecran))
   if (J_xdecor+V_xecran-mechant_x)**2 + (J_ydecor+V_yecran-mechant_y)**2 >= 300**2 and spawn == True:
      if J_xdecor+V_xecran > mechant_x:
         screen.blit(fleche_gauche,(fleche_gauche_x,fleche_gauche_y))
      else:
         screen.blit(fleche_droite,(fleche_droite_x,fleche_droite_y))

    # Go ahead and update the screen with what we've drawn.
   pygame.display.flip()
 
    # Limit frames per second
   clock.tick(30)
# Close the window and quit.
pygame.quit()