import pygame
import time
import random

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smash Down")

BG = pygame.image.load("test.jpeg")

def draw():
    WIN.blit(BG, (0, 0))
    pygame.display.update() 

def main():
    run = True

    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()





if __name__ == "__main__":
    main()
