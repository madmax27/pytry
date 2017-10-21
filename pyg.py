#-IMPORTAZIONI-#

import pygame

#-COSTANTI-#

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#-INIZIALIZZAZIONE-#

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My pyg")

#-LOOP-#

done = False

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
	#-SCREEN-#

	screen.fill(WHITE)

	pygame.display.flip()
	
	clock.tick(60)
	
pygame.quit()