import pygame
import random

pygame.init()
clock = pygame.time.Clock()
X = 1800
Y = 1126
screen = pygame.display.set_mode((X,Y))
pygame.mouse.set_visible(0)
pygame.display.set_caption("Nyan cat")
background = pygame.image.load("./background.jpg")

igra = True

cat_image = pygame.image.load("./cat.png")

ice_cream_image = pygame.image.load("./ice_cream.png")
ice_cream_image = pygame.transform.scale(ice_cream_image, (100, 100))

ufo_image = pygame.image.load("./ufo.png")
ufo_image = pygame.transform.scale(ufo_image, (100, 100))

lollipop_image = pygame.image.load("./lollipop.png")
lollipop_image = pygame.transform.scale(lollipop_image, (100, 100))

krof_image = pygame.image.load("./krof.png")
krof_image = pygame.transform.scale(krof_image, (100, 100))

milk_image = pygame.image.load("./milk.jpeg")
milk_image = pygame.transform.scale(milk_image, (100, 100))


cat = pygame.Rect(0, Y//2, 158, 78)
ice_cream = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
ufo = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
lollipop = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
krof = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
milk = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
font = pygame.font.Font('freesansbold.ttf', 80)

start_screen = True



while igra:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			igra = False

	screen.blit(font.render(f"Za začetek pritisni SPACE", True, (88, 151, 252)),(X//2-500,Y//2-100))


	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #Začetek igre
			start_screen = False



	while not start_screen: #igranje
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
					#premikanje!!! - naslednic

		screen.blit(ufo_image, ufo)
		screen.blit(ice_cream_image, ice_cream)
		screen.blit(lollipop_image, lollipop)
		screen.blit(krof_image, krof)
		screen.blit(milk_image, milk)
		screen.blit(cat_image, cat)

		cat.x += 1
		ufo.x -= 1
		ice_cream.x -= 1
		lollipop.x -= 1
		krof.x -= 1
		milk.x -= 1


		pygame.display.flip()
		screen.blit(background, (0,0))







	pygame.display.flip()
	screen.blit(background, (0,0))

