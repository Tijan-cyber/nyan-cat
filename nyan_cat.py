import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1800,1126))
pygame.mouse.set_visible(0)
pygame.display.set_caption("Nyan cat")
background = pygame.image.load("./background.jpeg")  #!!!!!!!!!!!! Spremeni na svojo pot do slike
igra = True




while igra:
	clock.tick(60)
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False


	pygame.display.update()
