import grid as gd
import pygame

# initialize pygame
pygame.init()
screen_size = (gd.WIDTH, gd.HEIGHT)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame Test")
 
# clock is used to set a max fps
clock = pygame.time.Clock()
 
running = True

grid = gd.Grid()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    screen.fill('black')
     
    # draw to the screen
    # YOUR CODE HERE

    grid.drawGrid(screen)
    
    grid.generation()

 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(1)
 
pygame.quit()
