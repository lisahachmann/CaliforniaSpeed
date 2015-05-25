import pygame
pygame.init()

class Window():
	size = (700, 500)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("California Speed")

class Card(object):
	"""Every card is an object of the Card class"""
	def __init__(self):
		pass

	def make_hearts():
		pass
	def make_spades():
		pass
	def make_diamonds():
		pass
	def make_clubs():
		pass

def deal_cards():
	pass

Game = Window()
WHITE = (255, 255 , 255)
GREEN = (0, 200, 100)
RED = (255, 0, 0)
BLACK = (0,0,0)
done = False
clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("User asked to quit.")
		elif event.type == pygame.KEYDOWN:
			print("User pressed a key.")
		elif event.type == pygame.KEYUP:
			print("User let go of a key.")
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("User pressed a mouse button") 
    # --- Drawing code should go here
 
    # First, clear the screen to green. Don't put other drawing commands
    # above this, or they will be erased with this command.
	Window.screen.fill(GREEN)
 
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
"""Use in case I have sprites, for later:

	screen.blit(background, (0, 0))
	allsprites.draw(screen)
	pygame.display.flip() """
	
    # --- Limit to 60 frames per second
	clock.tick(60)
