import pygame
import time
import random
from pygame.locals import *
pygame.font.init()
font = pygame.font.SysFont("arial", 18)
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cheap SCookie Clicker")
BG = pygame.transform.scale(pygame.image.load("CHBG.jpg"), (WIDTH, HEIGHT))
cookie_img = pygame.transform.scale(pygame.image.load("cookie.png"), (100, 100))
mula = 0
power = 1


class button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def drawbutton(self):
        act = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                act = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return act
    
clicking_cookie = button(20, 200, cookie_img)

def drawinitial():
    WIN.blit(BG, (0, 0))
    muns = font.render(f"{mula} Cookies", 1, "white")
    WIN.blit(muns, (10, 10))

def main():
    global mula
    run = True
    clock = pygame.time.Clock()

    while run :
        drawinitial()
        clock.tick(60)

        if clicking_cookie.drawbutton():
            mula += power

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        pygame.display.update()

    pygame.quit()





if __name__ == "__main__":
    main()
