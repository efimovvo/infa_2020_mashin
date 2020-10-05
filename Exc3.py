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


FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill(brown)



rect(screen, rust, (0, 250, 600, 450))


#Window

def draw_window(x, y, width, height):
	rect(screen, navy_blue, (x, y, width, height))
	rect(screen, sky_blue, (x+0.1*width, y+0.1*height, 0.35*width, 0.35*height))
	rect(screen, sky_blue, (x+0.55*width, y+0.1*height, 0.35*width, 0.35*height))
	rect(screen, sky_blue, (x+0.1*width, y+0.55*height, 0.35*width, 0.35*height))
	rect(screen, sky_blue, (x+0.55*width, y+0.55*height, 0.35*width, 0.35*height))


draw_window(60, 20, 120, 150)
draw_window(230, 20, 120, 150)
draw_window(400, 20, 120, 150)

#Cat
def draw_cat(x, y, width, height):

	ellipse(screen, orange, (x+width/3, y-height/6, width/1.5, height/2.5))
	ellipse(screen, black, (x+width/3, y-height/6, width/1.5, height/2.5),1)

	ellipse(screen, orange, (x-width/2, y-height/2, width, height))
	ellipse(screen, black, (x-width/2, y-height/2, width, height),1)

	ellipse(screen, orange, (x-width/1.75, y-height/8, width/8, height/2))
	ellipse(screen, black, (x-width/1.75, y-height/8, width/8, height/2), 1)

	ellipse(screen, orange, (x-4*width/6, y-height/2.5, width/3, height/1.5))
	ellipse(screen, black, (x-4*width/6, y-height/2.5, width/3, height/1.5),1)

	ellipse(screen, orange, (x-width/2.3, y+height/4.2, width/4, height/3))
	ellipse(screen, black, (x-width/2.3, y+height/4.2, width/4, height/3),1)

	ellipse(screen, orange, (x+width/6, y, width/3, height/1.7))
	ellipse(screen, black, (x+width/6, y, width/3, height/1.7),1)

	ellipse(screen, orange, (x+width/2.5, y+height/3, width/7, height/1.7))
	ellipse(screen, black, (x+width/2.5, y+height/3, width/7, height/1.7),1)

#Eyes
	ellipse(screen, green, (x-12*width/24, y-height/4.9, width/10, height/5))
	ellipse(screen, black, (x-12*width/24, y-height/4.9, width/10, height/5), 1)

	ellipse(screen, green, (x-15*width/24, y-height/4.9, width/10, height/5))
	ellipse(screen, black, (x-15*width/24, y-height/4.9, width/10, height/5), 1)

	ellipse(screen, black, (x-11*width/24, y-height/5.3, width/30, height/8))
	ellipse(screen, black, (x-14*width/24, y-height/5.3, width/30, height/8))
#Ear
	polygon(screen, pink, [(x-width/1.6,y-height/2.5), (x-width/1.8,y-height/2.9),
		                               (x-width/1.61,y-height/4)])
	polygon(screen, orange, [(x-width/1.6,y-height/2.5), (x-width/1.8,y-height/2.9),
		                               (x-width/1.61,y-height/4)],3)                               
	polygon(screen, black, [(x-width/1.6,y-height/2.5), (x-width/1.8,y-height/2.9),
		                               (x-width/1.61,y-height/4)], 1)

	polygon(screen, pink, [(x-width/1.6+width/4,y-height/2.5), (x-width/1.75+width/8,y-height/2.9),
		                               (x-width/1.61+width/4,y-height/4)])
	polygon(screen, orange, [(x-width/1.6+width/4,y-height/2.5), (x-width/1.75+width/8,y-height/2.9),
		                               (x-width/1.61+width/4,y-height/4)],3)                               
	polygon(screen, black, [(x-width/1.6+width/4,y-height/2.5), (x-width/1.75+width/8,y-height/2.9),
		                               (x-width/1.61+width/4,y-height/4)], 1)
#Nose
	polygon(screen, black, [(x-width/1.89, y+height/30), (x-width/2.04, y+height/30),
	                               (x-width/1.98, y+height/15)])
	pygame.draw.line(screen, black, (x-width/1.98, y+height/15), (x-width/1.98, y+height/10), 1)
	pygame.draw.arc(screen, black, (x-width/1.98, y+height/12, width/20, height/20), pi, pi+pi, 1)
	pygame.draw.arc(screen, black, (x-width/1.98-width/20, y+height/12, width/20, height/20), pi, pi+pi, 1)

	pygame.draw.arc(screen, black, (x-width/2.1, y+height/17, width/6, height/15),0, ((pi+pi+pi+pi+pi)/6), 1)
	pygame.draw.arc(screen, black, (x-width/2.1, y+height/11, width/6, height/15),0, ((pi+pi+pi+pi+pi)/6), 1)
	pygame.draw.arc(screen, black, (x-width/2.1, y+height/7, width/6, height/15),0, ((pi+pi+pi+pi+pi)/6), 1)
	pygame.draw.arc(screen, black, (x-width/1.4, y+height/17, width/6, height/15), pi/6,pi, 1)
	pygame.draw.arc(screen, black, (x-width/1.4, y+height/11, width/6, height/15), pi/6,pi, 1)
	pygame.draw.arc(screen, black, (x-width/1.4, y+height/7, width/6, height/15), pi/6,pi, 1)




draw_cat(100, 300, 120, 60)
draw_cat(430, 300, 150, 75)
draw_cat(300, 460, 200, 100)

#klubok
def draw_klubok(x, y, width, height):
	ellipse(screen, gray, (x, y, width, width))
	ellipse(screen, black, (x, y, width, width), 2)
	pygame.draw.arc(screen, black, (x+width/8,y+ width/4, width/2, width/3), pi/6,pi, 1)
	pygame.draw.arc(screen, black, (x+width/8,y+ width/2.5, width/2, width/3), pi/6,pi, 1)
	pygame.draw.arc(screen, black, (x+width/8,y+ width/2, width/2, width/3), pi/6,pi, 1)

	pygame.draw.arc(screen, black, (x+width/4,y+ width/3, width/2, width/3), pi+pi/4,pi+pi, 1)
	pygame.draw.arc(screen, black, (x+width/4,y+ width/2.5, width/2, width/3), pi+pi/4,pi+pi, 1)
	pygame.draw.arc(screen, black, (x+width/4,y+ width/2, width/2, width/3), pi+pi/4,pi+pi, 1)

	pygame.draw.arc(screen, black, (x-1.5*width,y+ 0.84*width, 2*width, width/2), pi/6,pi, 1)


draw_klubok(120, 500, 80, 80)	
draw_klubok(50, 370, 70, 70)	
draw_klubok(240, 280, 65, 65)	
draw_klubok(500, 500, 90, 90)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()