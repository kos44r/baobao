import pygame
import random

pygame.init()

note_positions = {
    "G5": 110,
    "F5" : 125,
    "E5" : 155
}

note_y = random.choice(list(note_positions.values())) 

note_x = random.randint(150, 450)
                       
info = pygame.display.Info()
width = 800
height = 600
background_colour = (130, 130, 255)

screen = pygame.display.set_mode((800,600), pygame.RESIZABLE)
pygame.display.set_caption("Music")



running = True

while running:
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            running = False
            
            
    screen.fill(background_colour)
    
    pygame.draw.circle(
        screen,
        (50, 50, 50),
        (note_x, 155),
        15
    )
        
    
    #staff itself
    for i in range (5):
        y = 125 + i * 60
        pygame.draw.line(
            screen,
            (50, 50, 50),
            (100, y), #start of line
            (700, y),
            5
        )
    
    pygame.display.flip()
pygame.quit()