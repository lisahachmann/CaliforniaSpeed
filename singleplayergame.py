import pygame
pygame.init()

#constants
WHITE = (255, 255 , 255)
GREEN = (0, 200, 100)
RED = (255, 0, 0)
BLACK = (0,0,0)

class Window():
	size = (700, 500)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("California Speed")

class Card(object):
	"""Every card is an object of the Card class"""
	size = (70, 50)
	def __init__(self):
		pass

	def make_hearts(self):
		pass
	def make_spades(self):
		pass
	def make_diamonds(self):
		pass
	def make_clubs(self):
		pass
	def back_of_card(self):
		pygame.draw.rect(Window.screen, RED, (20,20,50,70), 0) 
		#screen, color, (x, y, width, height), thickness

def deal_cards():
	pass


Game = Window()


done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
 		elif event.type == pygame.MOUSEBUTTONDOWN:
 			print "User pressed the mouse button"
    # --- Game logic should go here



    # First, clear the screen to green. Don't put other drawing commands
    # above this, or they will be erased with this command.
	Window.screen.fill(GREEN)
	# --- Drawing code should go here
	First_Card = Card()
	First_Card.back_of_card() 
 	pygame.display.update()
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	clock.tick(60)

"""Use in case I have sprites, for later:

	screen.blit(background, (0, 0))
	allsprites.draw(screen)
	pygame.display.flip() """

	# --- Limit to 60 frames per second
