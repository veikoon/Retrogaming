import pygame

import numpy as np
import pygame.surfarray as surfarray
 
pygame.init()

# crée une palette de couleurs
palette = {} # initialise un dictionnaire
palette['B'] =  [  0,   0, 255]   # BLUE
palette[' '] =  [  0,   0,   0]   # BLACK
palette['W'] =  [255, 255, 255]   # WHITE
palette['G'] =  [  0, 255,   0]   # GREEN
palette['R'] =  [255,   0,   0]   # RED
palette['Y'] =  [255, 255,   0]   # YELLOW
palette['C'] =  [  0, 225, 255]   # CYAN
palette['M'] =  [  184, 115, 51]   # BROWN

win = 0
score = 0
police = pygame.font.SysFont("arial", 50)
font = pygame.font.SysFont("arial", 10)
gagne = police.render( "WIN", 1, (255,255,0))

# dimensions
WIDTH = 20  # largeur d'une case en pixels
NBcases = 20

# grille du jeu

plan = [ 'BBBBBBBBBBBBBBBBBBBB', 
         'B                  B',
         'B BB BBBBBBBBB  BBBB',
         'B B  B   B   B B   B',
         'B BB BB  B B B   B B',
         'B B   BB B B BBBBB B',
         'B  B  B  B B       B',
         'BB BB BB B BBBBBBBBB',
         'B   B    B         B',
         'BBB BBB  BBBBBBBB  B',
         'B     B            B', 
         'B BBB BBBBB   BBBBBB',
         'B BBB B            B',
         'B B B B BBBBBBBBBB B',
         'B B        B       B',
         'BB  BBBBB    BBBBBBB',
         'BBBBB     BB B     B',
         'B  BB     BB BBBBB B',
         'B         BB       B',
         'BBBBBBBBBBBBBBBBBBBB' ]

#verification du plan

if ( len(plan) != NBcases ): print("erreur, nombre de lignes dans le plan")
for ligne in plan:
    if ( len(ligne) != NBcases ): print("erreur, ligne pas à la bonne dimension")

# remplissage du tableau du labyrinthe
LABY  = np.zeros((NBcases,NBcases,3))
for y in range(NBcases):
    ligne = plan[y]
    for x in range(NBcases):
        c = ligne[x]
        LABY[x,y] = palette[c]
        
###################################################################################

def ToSprite(ascii):
   _larg = len(max(pers1, key=len)) # on prend la ligne la plus grande
   _haut = len(pers1)
   TBL = np.zeros((_larg,_haut,3)) # tableau 3 dimensions

   for y in range(_haut):
      ligne = ascii[y]
      for x in range(len(ligne)):
         c = ligne[x]  # on recupere la lettre
         TBL[x,y] = palette[c]  #on stocke le code couleur RVB
    
   # conversion du tableau de RVB en sprite pygame
   sprite = surfarray.make_surface(TBL)
   return sprite


pers1= [ '   RRR    ', 
         '  RRWWR   ',
         '   RRR    ',
         '   YY     ',
         '   YYY     ',
         '   YY YG   ',
         '   GG      ',
         '   CC      ',
         '  C  C     ',
         ' C    C    ',
         'C      C   ' ]
         
pers2 = [ '   RRR    ', 
         '  RRWWR   ',
         '   RRR   ',
         '   YY   ',
         '   YYY   ',
         '   YY YG  ',
         '   GG    ',
         '   CC     ',
         '   C C    ',
         '  C   C   ',
         '  C   C    ' ]
         
pers3 = [ '   RRR    ', 
         '  RRWWR   ',
         '   RRR    ',
         '   YY     ',
         '   YYY     ',
         '   YY YG   ',
         '   GG      ',
         '   CC      ',
         '   CC      ',
         '   CC     ',
         '   CC    ' ]
         
cle = [ '   YYYY   ', 
         '   Y  Y   ',
         '   Y  Y   ',
         '   Y  Y   ',
         '   YYYY    ',
         '     Y     ',
         '    YY     ',
         '     Y     ',
         '    YY    ',
         '     Y    ',
         '         ' ]
    
coffre = [ '           ', 
         '           ',
         'YMMMMYMMMMY',
         'YMMMMYMMMMY',
         'YMMMYYYMMMY',
         'YYYYYBYYYYY',
         'YMMMYYYMMMY',
         'YMMMMYMMMMY',
         'YYYYYYYYYYY',
         '          ',
         '         ' ]
         
bombe = ['BBYBYBBYBBB',
         'BBBYBWBYBBB',
         'BBBBBWBBBBB',
         'BBBBBWBBBBB',
         'BBBBBWBBBBB',
         'BBBB   BBBB',   
         'BBB     BBB',
         'BB       BB',
         'BBB     BBB',
         'BBBB   BBBB',
         'BBBBBBBBBBB']


player_sprite = ToSprite(pers1)
cle_sprite = ToSprite(cle)
coffre_sprite = ToSprite(coffre)
bombe_sprite = ToSprite(bombe)
player_x = 25
player_y = 25
cle_x = 365
cle_y = 365
coffre_x = 65
coffre_y = 265
coffre2_x = 145
coffre2_y = 125
bombe_x = 65
bombe_y = 125
bombe2_x = 345
bombe2_y = 265
temp = 0
etat = 1
spawn = spawn2 = True
###################################################################################
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("LABYRINTHE")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    KeysPressed = pygame.key.get_pressed()
    
    if screen.get_at((player_x,player_y-1)) != (0,0,255,255) and screen.get_at((player_x+10,player_y-1)) != (0,0,255,255):
        if KeysPressed[pygame.K_UP]:
            player_y -= 1
    if screen.get_at((player_x,player_y+11)) != (0,0,255,255) and screen.get_at((player_x+10,player_y+11)) != (0,0,255,255):
        if KeysPressed[pygame.K_DOWN]:
            player_y += 1
    if screen.get_at((player_x-1,player_y)) != (0,0,255,255) and screen.get_at((player_x-1,player_y+10)) != (0,0,255,255):
        if KeysPressed[pygame.K_LEFT]:
            player_x -= 1
    if screen.get_at((player_x+11,player_y)) != (0,0,255,255) and screen.get_at((player_x+11,player_y+10)) != (0,0,255,255):
        if KeysPressed[pygame.K_RIGHT]:
            player_x += 1
            
    if int(pygame.time.get_ticks()/500) != temp :
        temp = int(pygame.time.get_ticks()/500)
        if etat == 4:
            player_sprite = ToSprite(pers1)
            etat = 1
        elif etat == 1:
            player_sprite = ToSprite(pers2)
            etat = 2
        elif etat == 2:
            player_sprite = ToSprite(pers3)
            etat = 3
        elif etat == 3:
            player_sprite = ToSprite(pers2)
            etat = 4

    if win == 0:
        # Draw background
        for ix in range(NBcases):
            for iy in range(NBcases):
                xpix = WIDTH * ix
                ypix = WIDTH * iy
                couleur = LABY[ix,iy]
                pygame.draw.rect(screen,couleur,[xpix,ypix,WIDTH,WIDTH])
                
        # draw player
        screen.blit(cle_sprite,(cle_x,cle_y))
        if spawn:
            screen.blit(coffre_sprite,(coffre_x,coffre_y))
        if spawn2:
            screen.blit(coffre_sprite,(coffre2_x,coffre2_y))
        screen.blit(player_sprite,(player_x,player_y))
        screen.blit(bombe_sprite,(bombe_x,bombe_y))
        screen.blit(bombe_sprite,(bombe2_x,bombe2_y))
        display = font.render(str(score), 1, (0,255,0))
        screen.blit(display,[200,5])
    else:
      screen.blit(gagne,[150,150])
    #print(player_sprite.get_width())
    
    if ((player_x-cle_x)**2 + (player_y-cle_y)**2) <= 5:
        win = 1
        
    if ((bombe_x-player_x)**2 + (bombe_y-player_y)**2) <= 1000:
        player_x = 25
        player_y = 25
    
    if ((bombe2_x-player_x)**2 + (bombe2_y-player_y)**2) <= 1000:
        player_x = 25
        player_y = 25
        
    if ((coffre_x-player_x)**2 + (coffre_y-player_y)**2) <= 10:
        if spawn:
            score += 100
        spawn = False
    if ((coffre2_x-player_x)**2 + (coffre2_y-player_y)**2) <= 10:
        if spawn2:
            score += 100
        spawn2 = False
    # 30 fps
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()