import pygame
import numpy as np
import os, inspect, random
import pygame.surfarray as surfarray

pygame.init()
 
#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
  
fond = pygame.image.load(os.path.join(assets, "map.png"))
planche_sprites = pygame.image.load(os.path.join(assets, "planche.png"))
planche_sprites_inverse = pygame.image.load(os.path.join(assets, "plancheInverse.png"))
button = pygame.image.load(os.path.join(assets, "button.png"))
sortie = pygame.image.load(os.path.join(assets, "sortie.png"))
police = pygame.font.SysFont("arial", 50)
victoire = police.render( "WIN", 1, (255,255,0))


planche_sprites.set_colorkey((0,0,0))
planche_sprites_inverse.set_colorkey((0,0,0))

LARG = 30
def ChargeSerieSprites(id):
   sprite = []
   for i in range(18):
      spr = planche_sprites.subsurface((LARG * i, LARG * id, LARG,LARG))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite
   
def ChargeSerieSpritesInverse(id):
   sprite = []
   for i in range(18):
      spr = planche_sprites_inverse.subsurface((LARG * i, LARG * id, LARG,LARG))
      test = spr.get_at((10,10))
      if ( test != (255,0,0,255) ):
         sprite.append( spr )
   return sprite
   
def on_position(xmin,xmax,posx,posy):
   global button_x
   global button_y
   global ButtonState
   if posx >= xmin and posx <= xmax and posy >= 343 and posy <= 399:
       button_x = xmin + 4 
       button_y = 344
       return True
   else: 
      return False




###################################################################################
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("LEMMINGS")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# liste des etats
EtatMarche = 100
EtatChute  = 200
EtatStop   = 300
EtatDead   = 400
EtatCreuse = 500
EtatWin = 600

ButtonState = 0
ButtonStop = 300
ButtonCreuse = 500

# liste des lemmins en cours de jeu

lemmingsLIST = []
compteur_creation = 0

temp = 0
i = 0
buttonB = False
win = 0
# -------- Main Program Loop -----------

marche = ChargeSerieSprites(0)
marcheInverse = ChargeSerieSpritesInverse(0)
tombe  = ChargeSerieSprites(1)
meurt = ChargeSerieSprites(10)
stop = ChargeSerieSprites(4)
creuse = ChargeSerieSprites(9)

pygame.mouse.set_visible(1)

while not done:
    times = int(pygame.time.get_ticks()/1000)
    time = int( pygame.time.get_ticks() / 100 )
    time2 = int( pygame.time.get_ticks() / 50 )

    # draw background
    screen.blit(fond,(0,0))
    
    # creation des lemmings : 1 lemming toutes les 1,5 secondes
    if (  (compteur_creation < 15 ) and ( (time+compteur_creation) % 15 == 0) ):
      compteur_creation += 1
      new_lemming = {}
      new_lemming['x']  = 250
      new_lemming['y']  = 100
      new_lemming['vx'] = -1
      new_lemming['etat'] = EtatChute  
      new_lemming['fallcount'] = 0
      new_lemming['Decal'] = random.randint(0,7)
      new_lemming['sprite'] = 0
      new_lemming['stop_x'] = 0
      new_lemming['stop_y'] = 0
      new_lemming['correct'] = 12
      new_lemming['timeCreuse'] = 0
      lemmingsLIST.append(new_lemming)

   # gestion des évènements
   
   
    for event in pygame.event.get():  # User did something
        
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            
    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            pygame.draw.line(screen, (255,255,255),(x-5,y),(x+5,y))
            pygame.draw.line(screen, (255,255,255),(x,y-5),(x,y+5))
            

            for onelemming in lemmingsLIST:
               if x >= onelemming['x'] and x <= onelemming['x']+10 and y >= onelemming['y']+12 and y <= onelemming['y']+30:
                  if ButtonState == ButtonStop :
                     onelemming['stop_x'] = onelemming['x']
                     onelemming['stop_y'] = onelemming['y']
                     onelemming['etat'] = ButtonState
                  if ButtonState == ButtonCreuse:
                     if onelemming['etat'] == EtatMarche:
                        onelemming['etat'] = ButtonState
                     
            if on_position(190,239,x,y):
               ButtonState = ButtonStop
            elif on_position(240,286,x,y):
               print("1")
            elif on_position(287,334,x,y):
               print("2")
            elif on_position(335,382,x,y):
               print("3")
            elif on_position(383,430,x,y):
               print("4")
            elif on_position(431,478,x,y):
               print("5")
            elif on_position(479,525,x,y):
               print("6")
            elif on_position(526,574,x,y):
               ButtonState = ButtonCreuse
            elif on_position(575,620,x,y):
               print("8")
            else:
               ButtonState = 0
            print(ButtonState)
               
            
   # ETAPE 1 : gestion des transitions
   
    for onelemming in lemmingsLIST:
       if (screen.get_at((onelemming['x']+10, onelemming['y']+31)) != (0,0,0,255)) and (screen.get_at((onelemming['x']+22, onelemming['y']+31)) != (0,0,0,255)):
         if onelemming['fallcount'] > 100: onelemming['etat'] = EtatDead
         else: 
            if onelemming['etat'] == EtatChute : onelemming['etat'] = EtatMarche
       else: onelemming['etat'] = EtatChute

   
   # ETAPE 2 : gestion des actions
   
             
    for onelemming in lemmingsLIST:
      if ( onelemming['etat'] == EtatChute ):
         onelemming['y'] += 3
         onelemming['fallcount'] += 3
      
      if ( onelemming['etat'] == EtatCreuse ):
         if onelemming['timeCreuse'] == 0:
            onelemming['timeCreuse'] = times
            print("zbeub")
         if onelemming['timeCreuse']+3 == times:
            pygame.draw.rect(fond,(0,0,0),(onelemming['x'],onelemming['y']+29,20,20))            
            onelemming['timeCreuse'] = 0
            
            
      if ( onelemming['etat'] == EtatMarche ):
         for unlemming in lemmingsLIST:
            if (onelemming['x']+10 == unlemming['stop_x'] and onelemming['y'] == unlemming['stop_y']) or (onelemming['x'] == unlemming['stop_x']+21 and onelemming['y'] == unlemming['stop_y']) or (screen.get_at((onelemming['x'], onelemming['y']+29)) != (0,0,0,255)) or (screen.get_at((onelemming['x']+12, onelemming['y']+29)) != (0,0,0,255)):
               onelemming['vx'] *= -1
               if onelemming['vx'] < 0:
                  onelemming['x'] -= 1
               else :
                  onelemming['x'] += 1
         onelemming['x'] += onelemming['vx']
         onelemming['fallcount'] = 0
         
      if ((onelemming['x']-682)**2+(onelemming['y']-287)**2) <= 20**2:
         onelemming['etat'] = EtatWin
         onelemming['x'] = onelemming['y'] = -20
         win += 1
         

    # ETAPE 3 : affichage des lemmings
    screen.blit(sortie,(650,250))
    for onelemming in lemmingsLIST:
      xx = onelemming['x']
      yy = onelemming['y']
      state = onelemming['etat']
            
      if ( state == EtatChute ):
         screen.blit(tombe[time%len(tombe)],(xx,yy))
         
      if ( state == EtatMarche ):
         if onelemming['vx'] < 0:
            screen.blit(marche[(time+onelemming['Decal'])%len(marche)],(xx,yy))
         else:
            screen.blit(marcheInverse[(time+onelemming['Decal'])%len(marche)],(xx,yy))
         SpriteMarche = (time+onelemming['Decal'])%len(marche)
         
      if ( state == EtatDead):
         if temp != time2 and onelemming['sprite']<16:
            screen.blit(meurt[onelemming['sprite']],(xx,yy))
            onelemming['sprite']+=1
            temp = time
            
      if ( state == EtatStop):
         screen.blit(stop[time%len(stop)],(xx,yy))
            
      if ( state == EtatCreuse):
         screen.blit(creuse[time%len(creuse)],(xx,yy))


      if ButtonState != 0:
         screen.blit(button,(button_x,button_y))
    if win >= 10:
       screen.blit(victoire,(300,150))
    clock.tick(20)
    print(win)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()