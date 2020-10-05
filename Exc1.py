import pygame
from pygame.draw import *

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
screen.fill(white)

circle(screen, yellow , (300, 300), 150)
rect(screen, black, (240, 370, 120, 30))
circle(screen, red , (240, 270), 30)
circle(screen, red , (360, 270), 26)
circle(screen, black , (240, 270), 15)
circle(screen, black, (360, 270), 12)

polygon(screen, black, [(200,195), (280,245),
                               (270,260), (190,210),(200,195)])
polygon(screen, black, [(400,200), (320,250),
                               (330,260), (410,210),(400,200)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

