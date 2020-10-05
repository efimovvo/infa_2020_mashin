import pygame, sys
from pygame.draw import *
from numpy import pi
pygame.init()

white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_gray = ((200,200,200))
dark_gray = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))


FPS = 30

screen = pygame.display.set_mode((600, 600))
screen.fill(brown)
#Window
rect(screen, rust, (0, 300, 600, 300))
rect(screen, navy_blue, (390, 10, 200, 250))
rect(screen, sky_blue, (400, 20, 80, 80))
rect(screen, sky_blue, (500, 20, 80, 80))
rect(screen, sky_blue, (400, 120, 80, 130))
rect(screen, sky_blue, (500, 120, 80, 130))

ellipse(screen, orange, (110, 330, 300, 150))
ellipse(screen, black, (110, 330, 300, 150),1)

ellipse(screen, orange, (90, 400, 35, 50))
ellipse(screen, black, (90, 400, 35, 50),1)

ellipse(screen, orange, (65, 320, 125, 110))
ellipse(screen, black, (65, 320, 125, 110),1)

ellipse(screen, orange, (120, 435, 80, 46))
ellipse(screen, black, (120, 435, 80, 46),1)

ellipse(screen, orange, (330, 400, 100, 95))
ellipse(screen, black, (330, 400, 100, 95),1)

ellipse(screen, orange, (410, 460, 30, 70))
ellipse(screen, black, (410, 460, 30, 70),1)

#Eyes
ellipse(screen, green, (85, 365, 35, 37))
ellipse(screen, black, (85, 365, 35, 37),1)

ellipse(screen, green, (140, 365, 35, 37))
ellipse(screen, black, (140, 365, 35, 37),1)

ellipse(screen, black, (105, 370, 5, 25))
ellipse(screen, black, (160, 370, 5, 25))
#Ear
polygon(screen, pink, [(70,320), (100,335),
                               (80,355)])
polygon(screen, orange, [(70,320), (100,335),
                               (80,355)],6)                               
polygon(screen, black, [(70,320), (100,335),
                               (80,355)], 1)


polygon(screen, pink, [(180,320), (150,335),
                               (175,355)])
polygon(screen, orange, [(180,320), (150,335),
                               (175,355)], 6)                               
polygon(screen, black, [(180,320), (150,335),
                               (175,355)], 1)
#Nose
polygon(screen, black, [(125,400), (135,400),
                               (130,405)])
pygame.draw.line(screen, black, [130, 400], [130, 413], 1)
pygame.draw.arc(screen, black, (130, 405, 20, 10), pi, pi+pi, 1)
pygame.draw.arc(screen, black, (110, 405, 20, 10), pi, pi+pi, 1)

pygame.draw.arc(screen, black, (160, 405, 40, 10),0, ((pi+pi+pi+pi+pi)/6), 1)
pygame.draw.arc(screen, black, (156, 408, 40, 10),0, ((pi+pi+pi+pi+pi)/6), 1)
pygame.draw.arc(screen, black, (152, 411, 40, 10),0, ((pi+pi+pi+pi+pi)/6), 1)
pygame.draw.arc(screen, black, (65, 411, 40, 10), pi/6,pi, 1)
pygame.draw.arc(screen, black, (61, 408, 40, 10), pi/6,pi, 1)
pygame.draw.arc(screen, black, (57, 405, 40, 10), pi/6,pi, 1)

ellipse(screen, gray, (300, 490, 80, 80))
ellipse(screen, black, (300, 490, 80, 80), 2)
pygame.draw.arc(screen, black, (310, 510, 40, 30), pi/6,pi, 1)
pygame.draw.arc(screen, black, (310, 520, 40, 30), pi/6,pi, 1)
pygame.draw.arc(screen, black, (310, 530, 40, 30), pi/6,pi, 1)

pygame.draw.arc(screen, black, (320, 515, 40, 30), pi+pi/4,pi+pi, 1)
pygame.draw.arc(screen, black, (320, 525, 40, 30), pi+pi/4,pi+pi, 1)
pygame.draw.arc(screen, black, (320, 535, 40, 30), pi+pi/4,pi+pi, 1)

pygame.draw.arc(screen, black, (130, 550, 200, 40), pi/6,pi, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

