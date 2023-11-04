import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smash Down")

Testbg = pygame.image.load("test.jpeg")
# menu bg
# main game bg

font = pygame.font.SysFont("arial", 18)

# monster1 = ???






def drawstart():
    WIN.blit(Testbg, (0, 0))

    controls_text1 = font.render("Left mouse button     : SMASH!!! (destroy the monsters that run by)", True, (255, 255, 255))
    controls_text2 = font.render("Right mouse button   : parry (redirect incoming dangers)", True, (255, 255, 255))
    controls_text3 = font.render("Middle mouse button : rescue (save the innocent)", True, (255, 255, 255))

    WIN.blit(controls_text1, (10,10))
    WIN.blit(controls_text2, (10,30))
    WIN.blit(controls_text3, (10,50))


    pygame.display.update() 



def main():
    run = True
    drawstart()
    clock = pygame.time.Clock()
    while run :
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
    # if right click atk
    #    left        block/parry
    #    and midd    rescue

    pygame.quit()





if __name__ == "__main__":
    main()
