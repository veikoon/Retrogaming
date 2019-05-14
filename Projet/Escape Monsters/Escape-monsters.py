import pygame
import os,inspect,random
from math import *

pygame.init()

        ## Variables

# Taille de l'ecran
screenWidth = 800
screenHeight = 600

#Taille de la largeur et de longueur du personnage divisee par deux pour les ajustements
LargeurPerso = 27
HauteurPerso = 45

# Position initiale du personnage
persox = screenWidth/2-LargeurPerso
persoy = screenHeight/2-HauteurPerso

#Parametrage de la fenetre d'affichage
WINDOW_SIZE = [screenWidth, screenHeight]
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Escape monsters")

#Parametrage des polices utilisées
police1 = pygame.font.SysFont("arial", 10)
police2 = pygame.font.SysFont("arial", 20)

#Parametrage de l'emplacement des fichiers
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0))
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
clock = pygame.time.Clock()

#Afficher ou non la souris
pygame.mouse.set_visible(False)

    #Importation des images

#Map
fond = pygame.image.load(os.path.join(assets, "fond.png"))
carton = pygame.image.load(os.path.join(assets, "coffre.png"))
baril_sprite = pygame.image.load(os.path.join(assets, "baril.png"))
image_tir = pygame.image.load(os.path.join(assets, "tir.png"))
fond_pause = pygame.image.load(os.path.join(assets, "fond_pause.png"))
arme5_sprite = pygame.image.load(os.path.join(assets, "arme1.1.png"))
arme4_sprite = pygame.image.load(os.path.join(assets, "arme1.png"))  
arme3_sprite = pygame.image.load(os.path.join(assets, "arme2.png")) 
arme2_sprite = pygame.image.load(os.path.join(assets, "arme3.png")) 
arme1_sprite = pygame.image.load(os.path.join(assets, "arme4.png")) 
explosion1 = pygame.image.load(os.path.join(assets, "explosion1.png"))
explosion2 = pygame.image.load(os.path.join(assets, "explosion2.png"))
explosion3 = pygame.image.load(os.path.join(assets, "explosion3.png"))
Game_over = pygame.image.load(os.path.join(assets, "Game_Over_bon.png"))

#Perso
MCULeft = pygame.image.load(os.path.join(assets, "MCULeft.png"))
MCULeft_pas1 = pygame.image.load(os.path.join(assets, "MCULeft_Pas1.png"))
MCULeft_pas2 = pygame.image.load(os.path.join(assets, "MCULeft_Pas2.png"))

MCURight = pygame.image.load(os.path.join(assets, "MCURight.png"))
MCURight_pas1 = pygame.image.load(os.path.join(assets, "MCURight_Pas1.png"))
MCURight_pas2 = pygame.image.load(os.path.join(assets, "MCURight_Pas2.png"))

MCBack = pygame.image.load(os.path.join(assets, "MCBack_Milieu.png"))
MCBack_pas1 = pygame.image.load(os.path.join(assets, "MCBack_Pas1.png"))
MCBack_pas2 = pygame.image.load(os.path.join(assets, "MCBack_Pas2.png"))

MCDRight = pygame.image.load(os.path.join(assets, "MCDRight_Pas2.png"))
MCDRight_pas1 = pygame.image.load(os.path.join(assets, "MCDRight_Pas1.png"))
MCDRight_pas2 = pygame.image.load(os.path.join(assets, "MCDRight_Pas3.png"))

MCLeft = pygame.image.load(os.path.join(assets, "MCLeft2.png"))
MCLeft_pas1 = pygame.image.load(os.path.join(assets, "MCLeft_Pas1.png"))
MCLeft_pas2 = pygame.image.load(os.path.join(assets, "MCLeft_Pas2.png"))


MCDLeft = pygame.image.load(os.path.join(assets, "MCDLeft_Pas2.png"))
MCDLeft_pas1 = pygame.image.load(os.path.join(assets, "MCDLeft_Pas1.png"))
MCDLeft_pas2 = pygame.image.load(os.path.join(assets, "MCDLeft_Pas3.png"))

MCRight = pygame.image.load(os.path.join(assets, "MCRight.png"))
MCRight_pas1 = pygame.image.load(os.path.join(assets, "MCRight_Pas1.png"))
MCRight_pas2 = pygame.image.load(os.path.join(assets, "MCRight_Pas2.png"))

MCFront = pygame.image.load(os.path.join(assets, "MCFront_Milieu.png"))
MCFront_pas1 = pygame.image.load(os.path.join(assets, "MCFront_Pas1.png"))
MCFront_pas2 = pygame.image.load(os.path.join(assets, "MCFront_Pas2.png"))

# Boss

BossLeft = pygame.image.load(os.path.join(assets, "BossDLeft.png"))
BossRight = pygame.image.load(os.path.join(assets, "BossDRight.png"))
BossDown = pygame.image.load(os.path.join(assets, "BossFront.png"))
BossUp = pygame.image.load(os.path.join(assets, "BossBack.png"))
BossDLeft = pygame.image.load(os.path.join(assets, "BossDLeft.png"))
BossDRight = pygame.image.load(os.path.join(assets, "BossDRight.png"))
BossULeft = pygame.image.load(os.path.join(assets, "BossULeft.png"))
BossURight = pygame.image.load(os.path.join(assets, "BossURight.png"))
BossFront = pygame.image.load(os.path.join(assets, "BossFront.png"))

#bat

BatDLeft3 = pygame.image.load(os.path.join(assets, "BatDLeft3.png"))
BatDRight3 = pygame.image.load(os.path.join(assets, "BatDRight3.png"))
BatFront3 = pygame.image.load(os.path.join(assets, "BatFront3.png"))
BatULeft3 = pygame.image.load(os.path.join(assets, "BatULeft3.png"))
BatURight3 = pygame.image.load(os.path.join(assets, "BatURight3.png"))

#Pumpkin

PumpkinBack3 =  pygame.image.load(os.path.join(assets, "CitrouilleBack.png"))
PumpkinDLeft3 =  pygame.image.load(os.path.join(assets, "CitrouilleDleft.png"))
PumpkinDRight3 =  pygame.image.load(os.path.join(assets, "CitrouilleDRight.png"))
PumpkinFront3 =  pygame.image.load(os.path.join(assets, "CitrouilleFront.png"))
PumpkinLeft3 =  pygame.image.load(os.path.join(assets, "CitrouilleLeft.png"))
PumpkinRight3 =  pygame.image.load(os.path.join(assets, "CitrouilleRight.png"))

# Snape

SnapeBack3 =  pygame.image.load(os.path.join(assets, "SnapeBack.png"))
SnapeDLeft3 =  pygame.image.load(os.path.join(assets, "SnapeDLeft.png"))
SnapeDRight3 =  pygame.image.load(os.path.join(assets, "SnapeDRight.png"))
SnapeFront3 =  pygame.image.load(os.path.join(assets, "SnapeFront.png"))
SnapeULeft3 =  pygame.image.load(os.path.join(assets, "SnapeULeft.png"))
SnapeURight3 =  pygame.image.load(os.path.join(assets, "SnapeURight.png"))


#Importation des sons

sontir = pygame.mixer.Sound(os.path.join(assets, "tir.wav"))
sonmort = pygame.mixer.Sound(os.path.join(assets, "mort.wav"))
reload = pygame.mixer.Sound(os.path.join(assets, "reload.wav"))

    #Initialisation des variables :
    
#Du personnage

x = 0
y = 400
vie = 20

#De la zone d'affichage

zonex = 0
zoney = 400

# Taille du décor

decorx = 2000
decory = 2000

# distance entre le personnage et le baril/monstres

distance_perso_baril = 0
distance_monstre_perso = 0
    
 # differentes armes utilisees : nb de munitions disponibles/ degats infliges aux monstres/ distance minimale de tir/ l'arme peut tirer ou non
 
arme5 = {'munitions':15,'degats':5, 'distance': 250, 'peut_tirer': False } 
arme4 = {'munitions':20,'degats':4.5, 'distance': 200, 'peut_tirer': False } 
arme3 = {'munitions':25,'degats':3.5, 'distance': 150, 'peut_tirer': False } 
arme2 = {'munitions':500,'degats':3, 'distance': 100, 'peut_tirer': False } 
arme1 = {'munitions':500,'degats':2, 'distance': 70, 'peut_tirer': False } 


#initalise l'arme courante avec arme1

arme = arme1


#Compteurs pour les apparitions d'entites

compteur_creation = 0
compteur_caisse = 0

#Initialisation des listes

barilLIST = []
monsterLIST = []
caisseLIST = []

# Variables qui definissent l'etat de l'explosion des barils

ETAT_EXPLOSION_DETRUIT = 0
ETAT_EXPLOSION_DEBUT = 1
ETAT_EXPLOSION_INTERM = 2
ETAT_EXPLOSION_FINAL = 3

#Autres
tempx = tempy = 0
direction = 0
nb_morts = 0

pause = False
done = False
tir = False
        
        ## Fonctions

# Calcule la distance entre deux points
 
def Distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)
    
# Permet de mettre le jeu en pause

def paused():
    global pause
    while pause:
        screen.blit(fond_pause,(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            pause = False
        
# Permet d'infliger des dégats au monstre et de lui appliquer du recul dans la direction opposé du tir
        
def gererTirSurMonstre( monstre, tir, distance_monstre_perso) : 
    
    if tir == True and distance_monstre_perso <= arme['distance'] and tirerDroit(monster) != False and arme['peut_tirer'] == True:
        if direction == 0:
            monstre['y']-=random.randint(10,20)
        elif direction == 1:
            monstre['x'] += random.randint(10,20)
            monstre['y'] -= random.randint(10,20)
        elif direction == 2:
            monstre['x']+=random.randint(10,20)
        elif direction == 3:
            monstre['x'] += random.randint(10,20)
            monstre['y'] += random.randint(10,20)
        elif direction == 4 :
            monstre['y'] += random.randint(10,20)
        elif direction == 5:
            monstre['x'] -= random.randint(10,20)
            monstre['y'] += random.randint(10,20)
        elif direction == 6:
            monstre['x']-=random.randint(10,20)
        elif direction == 7:
            monstre['x'] -= random.randint(10,20)
            monstre['y'] -= random.randint(10,20)
        monstre['vie'] -= arme['degats']
        monstre['touche'] = True
        return True

    else:
        monster['touche'] = False
        return False
    
# Permet l'affichage du coup de feu en fonction de la direction du hero
    
def afficheTir(dir):
    global image_tir
    if dir == 0:
        movex = LargeurPerso+12
        movey = HauteurPerso- 10
        tirx = movex
        tiry = HauteurPerso- 10-arme['distance']
        flammex = LargeurPerso+3
        flammey = 0
        image_tir = pygame.transform.rotate(image_tir,90)

    if dir == 1:
        movex = LargeurPerso*2
        movey = 0
        tirx = LargeurPerso*2+arme['distance']
        tiry = -arme['distance']
        flammex = LargeurPerso+3
        flammey = -10
        image_tir = pygame.transform.rotate(image_tir,45)

    if dir == 2:
        movex = LargeurPerso*2
        movey = HauteurPerso
        tirx = +arme['distance']+LargeurPerso*2+30
        tiry = HauteurPerso
        flammex = LargeurPerso+12
        flammey = HauteurPerso-9
        
    if dir == 3:
        movex = LargeurPerso*2
        movey = HauteurPerso*2
        tirx = LargeurPerso*2+arme['distance']
        tiry = HauteurPerso*2+arme['distance']
        flammex = LargeurPerso+7
        flammey = HauteurPerso*2-20
        image_tir = pygame.transform.rotate(image_tir,315)
        
    if dir == 4:
        movex = LargeurPerso-12
        movey = HauteurPerso+ 10
        tirx = LargeurPerso-12
        tiry = HauteurPerso+ 10 + arme['distance']
        flammex = LargeurPerso-20
        flammey = 30
        image_tir = pygame.transform.rotate(image_tir,270)
        
    if dir == 5:
        movex = 0
        movey = HauteurPerso*2
        tirx = -arme['distance']
        tiry = HauteurPerso*2+arme['distance']
        flammex = -10
        flammey =HauteurPerso*2-23
        image_tir = pygame.transform.rotate(image_tir,225)
       
    if dir == 6:
        movex = -30
        movey = HauteurPerso
        tirx = -arme['distance']
        tiry = HauteurPerso
        flammex = -32
        flammey = HauteurPerso-9
        image_tir = pygame.transform.rotate(image_tir,180)
        
    if dir == 7:
        movex = 0
        movey = 0
        tirx = -arme['distance']
        tiry = -arme['distance']
        flammex = -10
        flammey = -10
        image_tir = pygame.transform.rotate(image_tir,135)

        
    pygame.draw.line(screen,(255,255,255),(persox + movex,persoy + movey),(persox+tirx,persoy+tiry), 3)
    screen.blit(image_tir,(persox+flammex,persoy+flammey))
    image_tir = pygame.image.load(os.path.join(assets, "tir.png"))
    
# Permet de ne toucher les monstres que dans la direction dans laquelle on regarde
    
def tirerDroit(monster):
    global persox,persoy,decorx,decory
    if direction == 6 and ((persoy + HauteurPerso + y) >= monster['y']) and ((persoy + HauteurPerso + y) <= (monster['y'] + 90)) and (monster['x'] <= (persox + x)) : 
        return True
    elif direction == 2 and ((persoy + HauteurPerso + y) >= monster['y']) and ((persoy + HauteurPerso + y) <= (monster['y'] + 90)) and (monster['x'] >= (persox + x)):
        return True
    elif direction == 0 and ((persox + LargeurPerso + x) >= monster['x']) and ((persox + LargeurPerso + x) <= (monster['x'] + 70)) and (monster['y'] <= (persoy + HauteurPerso + y)):
        return True
    elif direction == 4 and ((persox + LargeurPerso + x) >= monster['x']) and ((persox + LargeurPerso + x) <= (monster['x'] + 70)) and (monster['y'] >= (persoy + HauteurPerso + y)):
        return True
    elif direction == 1:
        for i in range(0,240):
            if (LargeurPerso + persox + x + i) >= monster['x'] and (HauteurPerso + persoy + y - i) <= monster['y'] + 90 and (LargeurPerso + persox + x + i) <= monster['x']+56 and (HauteurPerso + persoy + y - i) >= monster['y']:
                return True
    elif direction == 7:
        for i in range(0,240):
            if (LargeurPerso + persox + x - i) >= monster['x'] and (HauteurPerso + persoy + y - i) <= monster['y'] + 90 and (LargeurPerso + persox + x - i) <= monster['x']+56 and (HauteurPerso + persoy + y - i) >= monster['y']:
                return True
    elif direction == 3:
        for i in range(0,240):
            if (LargeurPerso + persox + x + i) >= monster['x'] and (HauteurPerso + persoy + y + i) <= monster['y'] + 90 and (LargeurPerso + persox + x + i) <= monster['x']+56 and (HauteurPerso + persoy + y + i) >= monster['y']:
                return True
    elif direction == 5:
        for i in range(0,240):
            if (LargeurPerso + persox + x - i) >= monster['x'] and (HauteurPerso + persoy + y + i) <= monster['y'] + 90 and (LargeurPerso + persox + x - i) <= monster['x']+56 and (HauteurPerso + persoy + y + i) >= monster['y']:
                return True
    else:
        return False
        
#Permet de determiner le monstre le plus proche

def procheMonster():
    tempx = 2000
    tempy = 2000
    distance_monstre = 4000
    for monster in monsterLIST:
        if tirerDroit(monster):
            if Distance(monster['x'],monster['y'],persox + x,persoy + y) < distance_monstre:
                tempx = monster['x']
                tempy = monster['y']
                distance_monstre = Distance(monster['x'],monster['y'],persox + x,persoy + y)
    for monster in monsterLIST:
        if monster['x'] == tempx and monster['y'] == tempy:
            return monster

#Permet de tester si le pixel en x,y est de la meme couleure que les murs
    
def isPIxlGrayColor(x,y):
    if (fond.get_at((int(x),int(y))) != (217,218,218,255) and fond.get_at((int(x),int(y))) != (133,130,128,255)):
        return False
    else:return True
    
def collisionLeftWall(x,y,w,h):
    x1 = x + w + 8
    y1 = y
    x2 = x + w + 8
    y2 = y + h
    if isPIxlGrayColor(x1,y1):return True
    if isPIxlGrayColor(x2,y2):return True
    return False
    
def collisionRightWall(x,y,w,h):
    x1 = x - 8
    y1 = y
    x2 = x - 8
    y2 = y + h
    if isPIxlGrayColor(x1,y1):return True
    if isPIxlGrayColor(x2,y2):return True
    return False   
    
def collisionBottomWall(x,y,w,h):
    x1 = x 
    y1 = y -8
    x2 = x + w
    y2 = y - 8
    if isPIxlGrayColor(x1,y1):return True
    if isPIxlGrayColor(x2,y2):return True
    return False   
    
    
def collisionTopWall(x,y,w,h):
    x1 = x 
    y1 = y + h + 8
    x2 = x + w
    y2 = y + h + 8
    if isPIxlGrayColor(x1,y1):return True
    if isPIxlGrayColor(x2,y2):return True
    return False    

#Creation de 10 barils

for i in range(0,10):
    new_baril = {}
    new_baril['x']  = random.randint(0,decorx-100)
    new_baril['y']  = random.randint(0,decorx-100)
    new_baril['etat_explosion'] = 1
    new_baril['debut_etat_explosion'] =  0
    barilLIST.append(new_baril)

################################################################################
##                             Boucle principale                              ##
################################################################################

while not done:
    
    # Declaration de la variable de temps pour les invocations
    time = int( pygame.time.get_ticks() / 100 )
    
    # Zone de l'image qui est affichee
    zone = pygame.Rect(x,y, screenWidth, screenHeight)
   
    # Affichage du fond d'ecran
    screen.blit(fond,(0,0),area = zone)
  
    #Creation d'une liste avec tous les parametres de chaque monstres :
        #On fait apparaitre au total 100 monstres
    if ((compteur_creation < 100 ) and ( (time+compteur_creation) % 5 == 0) ):
      compteur_creation += 1
      new_monster = {}
      new_monster['x']  = random.choice((0,decorx/2,decorx))
      if new_monster['x'] == (decorx/2):
          new_monster['y']  = random.choice((0,decory))
      else: new_monster['y']  = (decory / 2)
      new_monster['x'] += random.randint(-100,100)
      new_monster['y'] += random.randint(-100,100)
      new_monster['vx'] = -1
      new_monster['vie'] = 10
      new_monster['Decal'] = random.randint(0,7)
      new_monster['DecalSprite'] = random.randint(0,7)
      new_monster['touche'] = False
      new_monster['type'] = random.randint(0,3)
      new_monster['d'] = False
      new_monster['u'] = False
      new_monster['r'] = False
      new_monster['l'] = False
      monsterLIST.append(new_monster)
      
    #Creation d'une liste avec tous les parametres de chaque caisses :
        #On fait apparaitre des caisses toutes les 15 secondes
    if (time % 150 == 0):
        new_caisse = {}
        while True:
            caissex = random.randint(0,decorx-100)
            caissey = random.randint(0,decory-100)
            if (not isPIxlGrayColor(caissex,caissey) and not isPIxlGrayColor(caissex+40,caissey+40) and not isPIxlGrayColor(caissex,caissey+40) and not isPIxlGrayColor(caissex+40,caissey)):
                break
        new_caisse['x']  = caissex
        new_caisse['y']  = caissey
        new_caisse['type'] = random.randint(0,1)
        new_caisse['arme'] = random.randint(0,2)
        caisseLIST.append(new_caisse)

    
    #Initialisation de la prise en compte des evenements
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if arme['munitions'] > 0 and arme['peut_tirer'] == True:
                  arme['munitions'] -= 1
                  tir = True
                  
                  if arme != arme1 and arme != arme2 and arme['peut_tirer'] == True :
                    sontir.play()
                    
    # Tant que le personnage est en vie on peut jouer
    if vie > 0:
       
        # Declaration de la variable de temps de jeu
        times = int( pygame.time.get_ticks() / 1000 )
       
        # On retient la derniere touche pressee
        KeysPressed = pygame.key.get_pressed()
    
        # Changements d'armes
        if KeysPressed[pygame.K_1]: arme = arme1
        if KeysPressed[pygame.K_2]: arme = arme2
        if KeysPressed[pygame.K_3]: arme = arme3
        if KeysPressed[pygame.K_4]: arme = arme4
        if KeysPressed[pygame.K_5]: arme = arme5

        # Déplacement de l'ecran ou du hero en fonction des coordonnees et declaration de la variable de direction:
        # Vers le haut
        if KeysPressed[pygame.K_UP] and not collisionBottomWall(persox + x,persoy + y,LargeurPerso*2,HauteurPerso*2) :
            if (y > 0 and persoy <= screenHeight/2-HauteurPerso ): y-=5
            if ( y <= decory - screenHeight and persoy > screenHeight/2-HauteurPerso) : persoy -= 5
            if (y == 0 and persoy > 0): persoy -=5
            direction = 0
    
       
        if KeysPressed[pygame.K_DOWN] and not collisionTopWall(persox + x,persoy + y,LargeurPerso*2,HauteurPerso*2) :  
            if (y  < decory - screenHeight and persoy == screenHeight/2-HauteurPerso ): y+=5
            if ( y == 0 and persoy < screenHeight - HauteurPerso*2 ): persoy += 5
            if (y == decory - screenHeight and persoy < screenHeight - HauteurPerso*2 ): persoy +=5
            direction = 4
            
                
       
        if KeysPressed[pygame.K_LEFT] and not collisionRightWall(persox + x,persoy + y,LargeurPerso*2,HauteurPerso*2):
            if (x > 0 and persox == screenWidth/2-LargeurPerso ): x-=5 
            if (x == decorx-screenWidth and persox > screenWidth/2-LargeurPerso ): persox -=5
            if (x == 0 and persox > 0): persox -=5
            direction = 6
            
      
        if KeysPressed[pygame.K_RIGHT] and not collisionLeftWall(persox + x,persoy + y,LargeurPerso*2,HauteurPerso*2):
            if (x < decorx-screenWidth and persox == screenWidth/2-LargeurPerso ): x+=5
            if (x < decorx-screenWidth and persox < screenWidth/2-LargeurPerso ): persox +=5
            if (x == decorx - screenWidth and persox < screenWidth - LargeurPerso*2 ): persox +=5
            direction = 2
            
        # Declaration des variables de directions diagonales
        if KeysPressed[pygame.K_RIGHT] and KeysPressed[pygame.K_UP]:direction = 1
        if KeysPressed[pygame.K_RIGHT] and KeysPressed[pygame.K_DOWN]:direction = 3
        if KeysPressed[pygame.K_LEFT] and KeysPressed[pygame.K_UP]:direction = 7
        if KeysPressed[pygame.K_LEFT] and KeysPressed[pygame.K_DOWN]:direction = 5
                        
        # Le jeu est mis en pause
        if KeysPressed[pygame.K_p]:
            pause = True
            paused()
            
        # Boucle qui permet de ramasser une caisse (de vie ou de munitions)
        for caisse in caisseLIST:
            if Distance(persox + x + LargeurPerso,persoy + y + HauteurPerso,caisse['x']+20,caisse['y']+20) <= 40:
                if caisse['type'] == 0:
                    vie = 20
                    print("caisse de vie")
                if caisse['type'] == 1:
                    if arme['degats'] == 2:
                        arme1['munitions'] = 35
                    if arme['degats'] == 3:
                        arme2['munitions'] = 30
                    if arme['degats'] == 3.5:
                        arme3['munitions'] = 25
                    if arme['degats'] == 4.5:
                        arme2['munitions'] = 20
                    if arme['degats'] == 5:
                        arme3['munitions'] = 20
                    print("caisse de munitions")
                caisse['x'] = caisse['y'] = -100
        
        for monster in monsterLIST:
            
            # Declaration et reinitialisation de la variable liste qui permet de supprimer les monstres
            deathMonsterList = []
           
            # Déplacement des monstres
            if monster['x'] < persox+x :
                monster['x'] += 1
                monster['r'] = True
                monster['l'] = False
            elif monster['x'] > persox+x :
                monster['x'] -= 1
                monster['l'] = True
                monster['r'] = False
            
            if monster['y'] < persoy+y : 
                monster['y'] += 1
                monster['d'] = True
                monster['u'] = False
            elif monster['y'] > persoy+y : 
                monster['y'] -= 1
                monster['u'] = True
                monster['d'] = False
            
            # Attaque des monstres lorsqu'ils sont au corps a corps
            if Distance(monster['x'],monster['y'],persox+x,persoy+y) <= 40 :
                vie-=1
                sonmort.play()
                
            # On tire sur les monstres :
            distance_monstre_perso = Distance(persox + x + LargeurPerso, persoy + y + HauteurPerso, monster['x']+LargeurPerso, monster['y']+HauteurPerso)
            gererTirSurMonstre ( monster, tir, distance_monstre_perso )
            
            # Declaration des dommages de l'arme en prevision de son affichage
            score_monstre = police1.render( str(- arme['degats']), 1 , (255,255,255))
            
            #On supprime le monstre si il est mort
            if monster['vie'] <= 0:
                nb_morts += 1
                deathMonsterList.append(monster)
            if gererTirSurMonstre ( monster, tir, distance_monstre_perso ):
                break
            for deathMonster in deathMonsterList:
                index_monster = monsterLIST.remove(deathMonster)
        
        ## Affichage
        
        #Affichage du hero
        if(direction == 1):
            if int(pygame.time.get_ticks()/200)%4==0: screen.blit(MCURight_pas1, (persox, persoy))
            elif int(pygame.time.get_ticks()/200)%2==0: screen.blit(MCURight_pas2, (persox, persoy))
            else: screen.blit(MCURight,(persox,persoy))
        
        elif(direction == 7):
            if int(pygame.time.get_ticks()/200)%4==0: screen.blit(MCULeft_pas1, (persox, persoy))
            elif int(pygame.time.get_ticks()/200)%2==0: screen.blit(MCULeft_pas2, (persox, persoy))
            else: screen.blit(MCULeft,(persox,persoy))
        
        elif(direction == 0):
            if int(pygame.time.get_ticks()/200)%4==0: screen.blit(MCBack_pas1, (persox, persoy))
            elif int(pygame.time.get_ticks()/200)%2==0: screen.blit(MCBack_pas2, (persox, persoy))
            else: screen.blit(MCBack,(persox,persoy))
        
        elif(direction == 5):
            if int(pygame.time.get_ticks()/200)%4==0: screen.blit(MCDLeft_pas1, (persox, persoy))
            elif int(pygame.time.get_ticks()/200)%2==0: screen.blit(MCDLeft_pas2, (persox, persoy))
            else: screen.blit(MCDLeft,(persox,persoy))
        
        elif(direction == 3):
            if (int(pygame.time.get_ticks()/200)%4==0): screen.blit(MCDRight_pas1,(persox,persoy))
            elif (int(pygame.time.get_ticks()/200)%2==0): screen.blit(MCDRight_pas2,(persox,persoy))
            else: screen.blit(MCDRight, (persox, persoy))
        
        elif(direction == 4):
            if(int(pygame.time.get_ticks()/200)%4==0): screen.blit(MCFront_pas1, (persox, persoy))
            elif(int(pygame.time.get_ticks()/200)%2==0): screen.blit(MCFront_pas2, (persox, persoy))
            else: screen.blit(MCFront,(persox,persoy))
        
        elif(direction == 6):
            if(int(pygame.time.get_ticks()/200)%4==0): screen.blit(MCLeft_pas1, (persox, persoy))
            elif(int(pygame.time.get_ticks()/200)%2==0): screen.blit(MCLeft_pas2, (persox, persoy))
            else: screen.blit(MCLeft,(persox,persoy))
        
        elif(direction == 2):
            if(int(pygame.time.get_ticks()/200)%4==0): screen.blit(MCRight_pas1, (persox, persoy))
            elif(int(pygame.time.get_ticks()/200)%2==0): screen.blit(MCRight_pas2, (persox, persoy))
            else: screen.blit(MCRight,(persox,persoy))
        
        else: screen.blit(MCFront,(persox,persoy))
        
        #Affichage des caisses
        for caisse in caisseLIST:
            screen.blit(carton,(caisse['x'] - x,caisse['y'] - y))
                
        #Affichage des barils
        for baril in barilLIST:
            if baril['etat_explosion'] != 0:
              screen.blit(baril_sprite,(baril['x'] - x,baril['y'] - y))
        
        # Affichage de l'explosion des barils 
        for baril in barilLIST :
            if baril['etat_explosion'] == ETAT_EXPLOSION_DETRUIT : continue
            
            etat_explosion = baril['etat_explosion']
            time_now = pygame.time.get_ticks()
           
            if time_now  -  baril['debut_etat_explosion'] > 150:
                
                if etat_explosion == ETAT_EXPLOSION_INTERM:
                    screen.blit(explosion2,(baril['x'] - x,baril['y'] - y))
                    baril['etat_explosion']= ETAT_EXPLOSION_FINAL
                    baril['debut_etat_explosion'] = pygame.time.get_ticks()
               
                elif etat_explosion == ETAT_EXPLOSION_FINAL:
                    screen.blit(explosion3,(baril['x'] - x,baril['y'] - y))
                    baril['etat_explosion'] = ETAT_EXPLOSION_DETRUIT
                else:pass
            
            if tir == True and Distance(persox+x,persoy+y, baril['x'], baril['y'] ) <= 150 and (arme != arme1 and arme != arme2 ) and tirerDroit(baril)==True:
                
              
                if baril['etat_explosion'] == ETAT_EXPLOSION_DEBUT:
                    screen.blit(explosion1,(baril['x'] - x,baril['y'] - y))
                    baril['etat_explosion']= ETAT_EXPLOSION_INTERM
                    baril['debut_etat_explosion'] = pygame.time.get_ticks()

        # Gestion des degats des barils sur le hero
        if Distance(persox + x,persoy + y , baril['x'], baril['y']) <= 100 :
            vie -= 5
       
        # Gestion des degats des barils sur les monstres
        for monster in monsterLIST :
            if Distance(monster['x'], monster['y'], baril['x'], baril['y']) <= 100 :
                monster['vie'] -= 5
                monster['touche']

        #affichage de tous les monstres selon leurs positions respectives
        for monster in monsterLIST :
            if monster['vie'] > 0:
                if(monster['u']==True and monster['r'] == True):
                    if monster['type'] == 0: screen.blit(BossURight,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatURight3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 2: screen.blit(PumpkinBack3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 3: screen.blit(SnapeURight3,(monster['x'] - x,monster['y'] - y))

                elif(monster['u']==True and monster['l'] == True):
                    if monster['type'] == 0: screen.blit(BossULeft,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatULeft3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 2: screen.blit(PumpkinBack3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 3: screen.blit(SnapeULeft3,(monster['x'] - x,monster['y'] - y))
         
                elif(monster['u']==True and not monster['l'] and not monster['r']):
                    if monster['type'] == 0: screen.blit(BossBack,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatULeft,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 2: screen.blit(PumpkinBack3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 3: screen.blit(SnapeULeft3,(monster['x'] - x,monster['y'] - y))    
                    
                elif(monster['d']==True and monster['l'] == True):
                    if monster['type'] == 0: screen.blit(BossDLeft,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatDLeft3,(monster['x'] - x,monster['y'] - y))    
                    if monster['type'] == 2: screen.blit(PumpkinFront3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 3: screen.blit(SnapeDLeft3,(monster['x'] - x,monster['y'] - y))      
                        
                elif(monster['d']==True and monster['r'] == True):
                    if monster['type'] == 0: screen.blit(BossDRight,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatDRight3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 2: screen.blit(PumpkinDRight3,(monster['x'] - x,monster['y'] - y))    
                    if monster['type'] == 3: screen.blit(SnapeDRight3,(monster['x'] - x,monster['y'] - y))
                        
                elif(monster['d']==True and not monster['r'] and not monster['l']):
                    if monster['type'] == 0: screen.blit(BossFront,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatFront3,(monster['x'] - x,monster['y'] - y))  
                    if monster['type'] == 2: screen.blit(PumpkinFront3,(monster['x'] - x,monster['y'] - y))    
                    if monster['type'] == 3: screen.blit(SnapeFront3,(monster['x'] - x,monster['y'] - y))
                
                elif(monster['l']==True and not monster['u'] and not monster['d']):
                    if monster['type'] == 0: screen.blit(BossLeft,(monster['x'] - x,monster['y'] - y))
                    elif monster['type'] == 1: screen.blit(BatDLeft3,(monster['x'] - x,monster['y'] - y))
                    elif monster['type'] == 2: screen.blit(PumpkinLeft3,(monster['x'] - x,monster['y'] - y))  
                    elif monster['type'] == 3: screen.blit(SnapeDLeft3,(monster['x'] - x,monster['y'] - y))      
                        
                elif(monster['r']==True and not monster['u'] and not monster['d']):
                    if monster['type'] == 0: screen.blit(BossRight,(monster['x'] - x,monster['y'] - y))
                    elif monster['type'] == 1 : screen.blit(BatDRight3,(monster['x'] - x,monster['y'] - y))
                    elif monster['type'] == 2 : screen.blit(PumpkinRight3,(monster['x'] - x,monster['y'] - y))
                    elif monster['type'] == 3: screen.blit(SnapeDRight3,(monster['x'] - x,monster['y'] - y))
                
                else: 
                    if monster['type'] == 0: screen.blit(BossFront,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 1: screen.blit(BatFront3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 2: screen.blit(PumpkinFront3,(monster['x'] - x,monster['y'] - y))
                    if monster['type'] == 3: screen.blit(SnapeFront3,(monster['x'] - x,monster['y'] - y))    
            
            # Affichage des dégats au dessus des monstres
            if monster['touche'] == True :
                screen.blit(score_monstre,(monster['x']-x + 5 , monster['y']-y - 15))

        #Affichage de la barre de point de vie
        pygame.draw.rect(screen,(0,255,0),(persox + 20 ,persoy - 10,vie,5))
       
        # Affichage du nombre de munitions disponibles
        if arme != arme1 and arme != arme2 and arme['peut_tirer'] == True :
            munitions = police1.render( "munitions: " + str(arme['munitions']), 1, (255, 255, 255) )
            screen.blit( munitions, (persox + 5 , persoy - 25))
            
        # Affichage de l'arme
        if arme == arme1:
            affichage_arme = police2.render( "weapon: ", 1, (255, 255, 255) )
            screen.blit(affichage_arme, (0,0))
            screen.blit(arme1_sprite,(85,0))
            arme1['peut_tirer'] = True
              
        if arme == arme2 and nb_morts >= 5 :
            affichage_arme = police2.render( "weapon: ", 1, (255, 255, 255) )
            screen.blit(affichage_arme, (0,0))
            screen.blit(arme2_sprite,(85,0))    
            arme2['peut_tirer'] = True
                
        if arme == arme3 and  nb_morts >= 20:
            affichage_arme = police2.render( "weapon: ", 1, (255, 255, 255) )
            screen.blit(affichage_arme, (0,0))
            screen.blit(arme3_sprite,(85,0))   
            arme3['peut_tirer'] = True 
                
        if arme == arme4 and nb_morts >= 30:
            affichage_arme = police2.render( "weapon: ", 1, (255, 255, 255) )
            screen.blit(affichage_arme, (0,0))
            screen.blit(arme4_sprite,(85,0))
            arme4['peut_tirer'] = True
                
        if arme == arme5 and  nb_morts >= 50:
            affichage_arme = police2.render( "weapon: ", 1, (255, 255, 255) )
            screen.blit(affichage_arme, (0,0))
            screen.blit(arme5_sprite,(85,0))
            arme5['peut_tirer'] = True
        
        # Affichage du tir
        if(tir) and arme != arme1 and arme != arme2 and arme['peut_tirer'] == True:
                    afficheTir(direction)

    # Si le hero meurt
    else : 
        sonmort.play()
        sonmort.stop()
        screen.blit(Game_over,(125,125))
        affichage_score = police2.render("Score : "+ str(nb_morts) ,1, (0,0,0))
        screen.blit(affichage_score, (700,0))
        
    # Affichage temps
    affichage_temps = police2.render( "Temps : "+ str(times) +"s", 1, (0,0,0))
    screen.blit(affichage_temps, (600,0))
    
    # Affichage score
    affichage_score = police2.render("Score : "+ str(nb_morts) ,1, (0,0,0))
    screen.blit(affichage_score, (700,0))
    
    tir = False
    for monster in monsterLIST:
        monster['touche'] = False
        
    # Actualisation de l'affichage
    pygame.display.flip()
    
    # On bloque a 60 fps
    clock.tick(60)
    
# On ferme la fenetre pour quitter
pygame.quit()