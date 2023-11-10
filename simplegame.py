import pygame
import time
import random
from pygame.locals import *
pygame.font.init()
font = pygame.font.SysFont("arial", 18)
money_type = pygame.font.SysFont("impact", 30)
win_font = pygame.font.SysFont("comic sans", 100)
WIDTH, HEIGHT = 790, 700
shop_width = 200
obj_w, obj_h = 60, 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker Not")
BG = pygame.transform.scale(pygame.image.load("CHBG.jpg"), (WIDTH, HEIGHT))
cookie_img = pygame.transform.scale(pygame.image.load("cookie.png"), (250, 250))
oven_img = pygame.transform.scale(pygame.image.load("microwave....png"), (obj_w, obj_h))
pin_img = pygame.transform.scale(pygame.image.load("pin.png"), (55, 55))
pan_img = pygame.transform.scale(pygame.image.load("pan.png"), (obj_w, obj_h))
tools_img = pygame.transform.scale(pygame.image.load("tools.png"), (obj_w, obj_h))
mixer_img = pygame.transform.scale(pygame.image.load("mixer.png"), (55, 55))
gran_img = pygame.transform.scale(pygame.image.load("the_ma.png"), (obj_w, obj_h))
bake_img = pygame.transform.scale(pygame.image.load("prof_bake.png"), (obj_w, obj_h))
web_img = pygame.transform.scale(pygame.image.load("web.png"), (50, 50))
baky_img = pygame.transform.scale(pygame.image.load("baky.png"), (55, 55))
francise_img = pygame.transform.scale(pygame.image.load("francise.png"), (200, 90))
mula = 0
power = 1
true_passive = 0

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
    
class shpbutton():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def drawbutton(self, cost, name, x, y):
        act = False
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.rect(WIN, (200, 200, 200), (x - 5, y, shop_width, 55))
        price = font.render(f"{cost}$", 1, (0, 0, 0))
        item = font.render(f"{name}", 1, (0, 0, 0))
        WIN.blit(price, (x + 40, y + 30))
        WIN.blit(item, (x + 40, y))

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                act = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return act
        
clicking_cookie = button(50, 225, cookie_img)
shp_oven = shpbutton(345, 380, oven_img)
shp_pin = shpbutton(350, 140, pin_img)
shp_pan = shpbutton(345, 200, pan_img)
shp_tools = shpbutton(345, 260, tools_img)
shp_mixer = shpbutton(350, 320, mixer_img)
shp_grandma = shpbutton(565, 140, gran_img)
shp_bake = shpbutton(565, 200, bake_img)
shp_web = shpbutton(572, 262, web_img)
shp_baky = shpbutton(570, 320, baky_img)
Francise = button(465, 600, francise_img)


def drawinitial():
    WIN.fill((10, 100, 175))
    pygame.draw.rect(WIN, (20, 60, 195), (40, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (120, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (200, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (280, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (360, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (440, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (520, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (600, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (680, 0, 40, HEIGHT))
    pygame.draw.rect(WIN, (20, 60, 195), (760, 0, 40, HEIGHT))
    muns = money_type.render(f"{mula}$", 1, (255, 255, 255))
    pygame.draw.rect(WIN, (155, 80, 40), (340, 0, 10, HEIGHT))
    pygame.draw.rect(WIN, (155, 80, 40), (780, 0, 10, HEIGHT))
    pygame.draw.rect(WIN, (155, 80, 40), (560, 80, 10, 460))
    pygame.draw.rect(WIN, (155, 80, 40), (340, 120, 460, 10))
    pygame.draw.rect(WIN, (155, 80, 40), (340, 540, 450, 10))
    pygame.draw.rect(WIN, (200, 200, 200), (390, 560, 350, 130))
    million = font.render(f"1000000$", 1, (0, 0, 0))
    open = font.render(f"Open Francise", 1, (0, 0, 0))
    store = money_type.render(f"Upgrades", 1, (255, 255, 255))
    active = money_type.render(f"Active", 1, (255, 255, 255))
    passve = money_type.render(f"Passive", 1, (255, 255, 255))
    WIN.blit(open, (520, 570))
    WIN.blit(million, (535, 590))
    WIN.blit(active, (420, 80))
    WIN.blit(passve, (630, 80))
    WIN.blit(store, (505, 30))
    WIN.blit(muns, (115, 70))

def main():
    global mula
    global power
    global true_passive
    run = True
    clock = pygame.time.Clock()
    win = False
    cost_oven = 12000
    cost_pin = 10
    cost_pan = 120
    cost_tools = 1500
    cost_mixer = 6000

    cost_gran = 30
    cost_bake = 240
    cost_web = 2000
    cost_baky = 10000

    passive = 0

    while run :
        drawinitial()
        clock.tick(60)
        
        passive += true_passive

        if passive >= 1:
            mula = mula + round(passive)
            passive = passive % 1

        if clicking_cookie.drawbutton():
            mula += power

        if shp_oven.drawbutton(cost_oven, 'Oven', 360, 380) and mula >= cost_oven:
            power += 1000
            mula -= cost_oven
            true_cost_oven = cost_oven * 1.6
            cost_oven = round(true_cost_oven)

        if shp_pin.drawbutton(cost_pin, 'Rolling pin', 360, 140) and mula >= cost_pin:
            power += 1
            mula -= 10
            cost_pin = cost_pin * 2

        if shp_pan.drawbutton(cost_pan, 'Baking pan', 360, 200) and mula >= cost_pan:
            power += 15
            mula -= cost_pan
            true_cost_pan = cost_pan * 1.9
            cost_pan = round(true_cost_pan)

        if shp_tools.drawbutton(cost_tools, 'Icing tools', 360, 260) and mula >= cost_tools:
            power += 140
            mula -= cost_tools
            true_cost_tools = cost_tools * 1.8
            cost_tools = round(true_cost_tools)

        if shp_mixer.drawbutton(cost_mixer, 'Mixer', 360, 320) and mula >= cost_mixer:
            power += 350
            mula -= cost_mixer
            true_cost_mixer = cost_mixer * 1.7
            cost_mixer = round(true_cost_mixer)

        if shp_grandma.drawbutton(cost_gran, 'Granny', 580, 140) and mula >= cost_gran:
            true_passive += 2 / 60
            mula -= cost_gran
            true_cost_gran = cost_gran * 1.9
            cost_gran = round(true_cost_gran) 

        if shp_bake.drawbutton(cost_bake, 'Profesional', 580, 200) and mula >= cost_bake:
            true_passive += 20 / 60
            mula -= cost_bake
            true_cost_bake = cost_bake * 1.9
            cost_bake = round(true_cost_bake) 

        if shp_baky.drawbutton(cost_baky, 'Bakery', 580, 320) and mula >= cost_baky:
            true_passive += 2000 / 60
            mula -= cost_baky
            true_cost_baky = cost_baky * 1.6
            cost_baky = round(true_cost_baky) 

        if shp_web.drawbutton(cost_web, 'Online shop', 580, 260) and mula >= cost_web:
            true_passive += 300 / 60
            mula -= cost_web
            true_cost_web = cost_web * 1.8
            cost_web = round(true_cost_web)

        if Francise.drawbutton() and mula >= 1000000:
            win = True
            WIN.fill((10, 100, 175))
            win_txt = win_font.render(f"You are now super duper rich", 1, (255, 255, 255))
            WIN.blit(win_txt, (200, 260))
            while win == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        win = False
                        run = False
                        break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
