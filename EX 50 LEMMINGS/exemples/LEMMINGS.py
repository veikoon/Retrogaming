import pygame
import numpy as np
import pygame.surfarray as surfarray
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# dimensions
WIDTH = 20  # largeur d'une case en pixels
NBcases = 10

# grille du jeu

plan = [ 'RRRRRRRRRR', 
         'R        R',
         'R RR RRRRR',
         'R RR R   R',
         'R RR RRR R',
         'R RR  RR R',
         'R  RR RR R',
         'RR RR RR R',
         'R   R    R',
         'RRRRRRRRRR' ]

#verification du plan

if ( len(plan) != NBcases ): print("erreur, nombre de lignes dans le plan")
for ligne in plan:
    if ( len(ligne) != NBcases ): print("erreur, ligne pas à la bonne dimension")

# remplissage du tableau du labyrinthe
LABY  = {}
for i in range(10):
    ligne = plan[i]
    for j in range(10):
        c = ligne[j]
        if (c == 'R'): LABY[j,i] = RED
        if (c == ' '): LABY[j,i] = BLUE
        




 
striped = np.zeros((WIDTH,WIDTH,3))
striped[:] = RED
striped[:,::3] = WHITE
ss = surfarray.make_surface(striped)

 
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            x = pos[0] // (WIDTH + MARGIN)
            y = pos[1] // (WIDTH + MARGIN)
            # Set that location to one
            cases[x,y] = 1
            print("Click ", pos, "Grid coordinates: ", x, y)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for ix in range(NBcases):
        for iy in range(NBcases):
            xpix = (MARGIN + WIDTH) * ix + MARGIN
            ypix = (MARGIN + WIDTH) * iy + MARGIN

            if cases[ix,iy] == 1:
                screen.blit(ss,(xpix,ypix))
            else:
                pygame.draw.rect(screen,BLUE,[xpix,ypix,WIDTH,WIDTH],0)
             
 
    # Limit to 30 frames per second
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 

pygame.quit()