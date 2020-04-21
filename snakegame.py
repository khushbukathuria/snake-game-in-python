import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake Game')
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)    #this command prints out all the events 
pygame.quit()
quit()
