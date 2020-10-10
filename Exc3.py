import pygame, sys
from pygame.draw import *
from numpy import pi

def draw_window(x, y, width, height, frame_color, pane_color):
	''' Function draws a WINDOW
	
	Attrubutes:
	-----------------------------------------------
		x : float
			horizontal coordinate of window center point
		y : float
			vertical coordinate of window top point
		width : float
			horizontal size of the window
		height : float
			vertical size of the window
		frame_color : tuple of 3 int
			color of window frame
		pane_color : tuple of 3 int
			color of window pane
	'''
	frame_width_ratio = 0.1
	pane_width = (0.5 - 1.5 * frame_width_ratio) * width
	pane_height = (0.5 - 1.5 * frame_width_ratio) * height

	# Window frame
	rect(
		screen,
		frame_color,
		(
			x - 0.5 * width,
			y,
			width,
			height
		)
		)
	# Left top pane
	rect(
		screen,
		pane_color,
		(
			x + (-0.5 + frame_width_ratio) * width,
			y + frame_width_ratio * height,
			pane_width,
			pane_height,
		)
		)
	# Right top pane
	rect(
		screen,
		pane_color,
		(
			x + 0.5 * frame_width_ratio * width,
			y + frame_width_ratio * height,
			pane_width,
			pane_height
		)
		)
	# Left bottom pane
	rect(
		screen,
		pane_color,
		(
			x + (-0.5 + frame_width_ratio) * width,
			y + (0.5 + 0.5 * frame_width_ratio) * height,
			pane_width,
			pane_height
		)
		)
	# Right bottom pane
	rect(
		screen,
		pane_color,
		(
			x + 0.5 * frame_width_ratio * width,
			y + (0.5 + 0.5 * frame_width_ratio) * height,
			pane_width,
			pane_height
		)
		)

def draw_cat(x, y, width, height, hair_color, eyes_color):
	''' Function draws a CAT
	
	Attrubutes:
	-----------------------------------------------
		x : float
			cat horizontal position
		y : float
			cat vertical position
		width : float
			cat's size in horizontal
		height : float
			cat's size in vertical
		hair_color : tuple of 3 int
			color of cat's hair
		eyes_color : tuple of 3 int
			color of cat's eyes
	'''

# Cat's body
	ellipse(screen, hair_color, (x + width/3, y - height/6, width/1.5, height/2.5))
	ellipse(screen, black, (x + width/3, y - height/6, width/1.5, height/2.5), 1)

	ellipse(screen, hair_color, (x - width/2, y - height/2, width, height))
	ellipse(screen, black, (x - width/2, y - height/2, width, height), 1)

	ellipse(screen, hair_color, (x - width/1.75, y - height/8, width/8, height/2))
	ellipse(screen, black, (x - width/1.75, y - height/8, width/8, height/2), 1)

	ellipse(screen, hair_color, (x - 4*width/6, y - height/2.5, width/3, height/1.5))
	ellipse(screen, black, (x - 4*width/6, y - height/2.5, width/3, height/1.5), 1)

	ellipse(screen, hair_color, (x - width/2.3, y + height/4.2, width/4, height/3))
	ellipse(screen, black, (x - width/2.3, y + height/4.2, width/4, height/3), 1)

	ellipse(screen, hair_color, (x + width/6, y, width/3, height/1.7))
	ellipse(screen, black, (x + width/6, y, width/3, height/1.7), 1)

	ellipse(screen, hair_color, (x + width/2.5, y + height/3, width/7, height/1.7))
	ellipse(screen, black, (x + width/2.5, y + height/3, width/7, height/1.7), 1)

# Cat's eyes
	ellipse(screen, eyes_color, (x-12*width/24, y-height/4.9, width/10, height/5))
	ellipse(screen, black, (x-12*width/24, y-height/4.9, width/10, height/5), 1)

	ellipse(screen, eyes_color, (x-15*width/24, y-height/4.9, width/10, height/5))
	ellipse(screen, black, (x-15*width/24, y-height/4.9, width/10, height/5), 1)

	ellipse(screen, black, (x-11*width/24, y-height/5.3, width/30, height/8))
	ellipse(screen, black, (x-14*width/24, y-height/5.3, width/30, height/8))

# Cat's ear
	polygon(screen, pink, [(x-width/1.6, y-height/2.5), (x-width/1.8, y-height/2.9),
										(x-width/1.61, y-height/4)])
	polygon(screen, hair_color, [(x-width/1.6, y-height/2.5), (x-width/1.8, y-height/2.9),
										(x-width/1.61, y-height/4)], 3)                               
	polygon(screen, black, [(x-width/1.6, y-height/2.5), (x-width/1.8, y-height/2.9),
										(x-width/1.61, y-height/4)], 1)

	polygon(screen, pink, [(x-width/1.6+width/4, y-height/2.5), (x-width/1.75+width/8, y-height/2.9),
										(x-width/1.61+width/4, y-height/4)])
	polygon(screen, hair_color, [(x-width/1.6+width/4, y-height/2.5), (x-width/1.75+width/8, y-height/2.9),
										(x-width/1.61+width/4, y-height/4)],3)                               
	polygon(screen, black, [(x-width/1.6+width/4, y-height/2.5), (x-width/1.75+width/8, y-height/2.9),
										(x-width/1.61+width/4, y-height/4)], 1)

# Cat's nose
	polygon(screen, black, [(x-width/1.89, y+height/30), (x-width/2.04, y+height/30),
										(x-width/1.98, y+height/15)])
	line(screen, black, (x-width/1.98, y+height/15), (x-width/1.98, y+height/10), 1)
	arc(screen, black, (x-width/1.98, y+height/12, width/20, height/20), pi, 2*pi, 1)
	arc(screen, black, (x-width/1.98-width/20, y+height/12, width/20, height/20), pi, 2*pi, 1)

	arc(screen, black, (x-width/2.1, y+height/17, width/6, height/15),0, (pi * 5/6), 1)
	arc(screen, black, (x-width/2.1, y+height/11, width/6, height/15),0, (pi * 5/6), 1)
	arc(screen, black, (x-width/2.1, y+height/7, width/6, height/15),0, (pi * 5/6), 1)
	arc(screen, black, (x-width/1.4, y+height/17, width/6, height/15), pi/6,pi, 1)
	arc(screen, black, (x-width/1.4, y+height/11, width/6, height/15), pi/6,pi, 1)
	arc(screen, black, (x-width/1.4, y+height/7, width/6, height/15), pi/6,pi, 1)

# Ball
def draw_ball(x, y, diameter, ball_color, fiber_color):
	''' Function draws a BALL
	
	Attrubutes:
	-----------------------------------------------
		x : float
			ball horizontal position
		y : float
			ball vertical position
		diameter : float
			ball diameter
		ball_color : tuple of 3 int
			color of ball
		fiber_color : tuple of 3 int
			color of ball border and fiber lines
	'''
	ellipse(screen, ball_color, (x, y, diameter, diameter))
	ellipse(screen, fiber_color, (x, y, diameter, diameter), 2)

# Top 3 arcs of on the ball from the top to the bottom
	pygame.draw.arc(screen, fiber_color, (x + diameter/8, y + diameter/4, diameter/2, diameter/3), pi/6,pi, 1)
	pygame.draw.arc(screen, fiber_color, (x + diameter/8, y + diameter/2.5, diameter/2, diameter/3), pi/6,pi, 1)
	pygame.draw.arc(screen, fiber_color, (x + diameter/8, y + diameter/2, diameter/2, diameter/3), pi/6,pi, 1)

# Bottom 3 arcs of on the ball from the top to the bottom
	pygame.draw.arc(screen, fiber_color, (x + diameter/4, y + diameter/3, diameter/2, diameter/3), pi + pi/4, pi+pi, 1)
	pygame.draw.arc(screen, fiber_color, (x + diameter/4, y + diameter/2.5, diameter/2, diameter/3), pi + pi/4, pi+pi, 1)
	pygame.draw.arc(screen, fiber_color, (x + diameter/4, y + diameter/2, diameter/2, diameter/3), pi + pi/4, pi+pi, 1)

# One external fiber
	pygame.draw.arc(screen, fiber_color, (x - 1.5*diameter, y + 0.84*diameter, 2*diameter, diameter/2), pi/6, pi, 1)

pygame.init()

''' Color set '''
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
orange = (255,100,10)
yellow = (255,255,0)
blue_green = (0,255,170)
marroon = (115,0,0)
lime = (180,255,100)
pink = (255,100,180)
purple = (240,0,255)
gray = (127,127,127)
magenta = (255,0,230)
brown = (100,40,0)
forest_green = (0,50,0)
navy_blue = (0,0,100)
rust = (210,150,75)
dandilion_yellow = (255,200,0)
highlighter = (255,255,100)
sky_blue = (0,255,255)
light_gray = (200,200,200)
dark_gray = (50,50,50)
tan = (230,220,170)
coffee_brown = (200,190,140)

# Screen constants
FPS = 30
screen_width = 400
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

# Drawing background = the wall
screen.fill(brown)

# Drawing the floor 
rect(screen, rust, (0, 250, 600, 450))

# Drawing the windows
window_width = screen_width / 3
window_height = screen_height / 4
draw_window(screen_width / 12, 20, window_width, window_height, navy_blue, sky_blue)
draw_window(screen_width / 2, 20, window_width, window_height, navy_blue, sky_blue)
draw_window(screen_width * 11/12, 20, window_width, window_height, navy_blue, sky_blue)

# Drawing the cats
draw_cat(screen_width/4, 300, screen_width/3, 60, orange, green)
draw_cat(screen_width * 7/8, 300, screen_width * 2/5, 75, gray, sky_blue)
draw_cat(screen_width * 3/4, 460, screen_width/2, 100, brown, green)

# Drawing the balls
basic_ball_radius = screen_width / 40

draw_ball(screen_width / 3, screen_height * 5/6, 8*basic_ball_radius, gray, black)	
draw_ball(screen_width / 8, screen_height * 7/12, 7*basic_ball_radius, gray, white)
draw_ball(screen_width * 2/3, screen_height * 4/7, 6*basic_ball_radius, gray, black)
draw_ball(screen_width * 11/12, screen_height * 5/6, 9*basic_ball_radius, gray, black)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()