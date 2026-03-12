import pygame

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Nyan cat")
background = pygame.image.load("./background")  #!!!!!!!!!!!! Spremeni na svojo pot do slike
igra = True

while igra:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False