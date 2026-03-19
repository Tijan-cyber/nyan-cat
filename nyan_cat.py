import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1800,1126))
pygame.mouse.set_visible(0)
pygame.display.set_caption("Nyan cat")
<<<<<<< HEAD
background = pygame.image.load("background.jpeg")  #!!!!!!!!!!!! Spremeni na svojo pot do slike
=======
background = pygame.image.load("background.jpeg")  #!!!!!!!!!!!! pomoje ni treba ker ji itak v istem folderju
>>>>>>> 28e7aae0176142492617074e58b1c563fa81a715
igra = True




while igra:
<<<<<<< HEAD
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        igra = False

        pygame.display.update()
        


=======
	clock.tick(60)
	screen.blit(background, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False


	pygame.display.update()
>>>>>>> 28e7aae0176142492617074e58b1c563fa81a715
