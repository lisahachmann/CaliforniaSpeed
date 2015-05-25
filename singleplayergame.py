import pygame
pygame.init()

#constants
WHITE = (255, 255 , 255)
GREEN = (0, 200, 100)
RED = (255, 0, 0)
BLACK = (0,0,0)

class Window():
	"""Creates the game screen, with caption"""
	size = (700, 500)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("California Speed")

class Card(object):
	"""Every card is an object of the Card class"""
	size = (70, 50) #constant size of card

	def __init__(self):
		pass
	def draw_card(self, x, y):
		pygame.draw.rect(Window.screen, RED, (x,y,50,70), 0) 
		pygame.display.flip()
	def new_position(self):
		"""Finds new spot, where the user wants the card to go"""
		new_spot = pygame.mouse.get_pos()
		x = new_spot[0]
		y = new_spot[1]
		Card.draw_card(self, x,y) #calls draw_card so it places the card there
		
	def back_of_card(self):
		#pile of player, visually
		pygame.draw.rect(Window.screen, RED, (20,20,50,70), 0) 
		#syntax goes:    screen, color, (x, y, width, height), thickness
	def move_card():
		pass

def deal_cards():
	"""beginning sequence that places 4 cards down from the pile"""
	pass
#initializes basic parts: screen, infinite loop and clock
Game = Window()
done = False
clock = pygame.time.Clock()

#infinite game loop unless you press the exit button
while not done:
	Window.screen.fill(GREEN)
	# First, clear the screen to green. Don't put other drawing commands
    # above this, or they will be erased with this command.
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
 		elif event.type == pygame.MOUSEBUTTONDOWN:
 			print pygame.mouse.get_pos()
 			First_Card.new_position()
    # --- Game logic should go here

	# --- Drawing code should go here
	First_Card = Card()
	First_Card.back_of_card() 
 	#pygame.display.update()
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	clock.tick(90)
	# --- Limit to 60 frames per second


"""Use in case I have sprites, for later:

	screen.blit(background, (0, 0))
	allsprites.draw(screen)
	pygame.display.flip() """