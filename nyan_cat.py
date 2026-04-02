import pygame
import random

pygame.init()
clock = pygame.time.Clock()
X = 1800
Y = 1126
screen = pygame.display.set_mode((X,Y))
pygame.mouse.set_visible(0)
pygame.display.set_caption("Nyan cat")
#158x78
background = pygame.image.load("./background.jpg").convert()
bg_width = background.get_width()

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

milk_image = pygame.image.load("./milk.png")
milk_image = pygame.transform.scale(milk_image, (100, 100))

ufo_image = pygame.image.load("./ufo.png")
ufo_image = pygame.transform.scale(ufo_image, (100, 100))



hotdog_image = pygame.image.load("./hotdog.png")
#hotdog 

cat = pygame.Rect(0, Y//2, 158, 78)
ice_cream = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
ufo = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
lollipop = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
krof = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
milk = pygame.Rect(1900, random.randint(100, 1100), 20, 20)
font = pygame.font.Font('freesansbold.ttf', 80)


platforma1 = pygame.Rect(random.randint(0, 1100), random.randint(100, 500), 259, 72)
platforma2 = pygame.Rect(random.randint(0, 1100), random.randint(600, 1100), 259, 72)
#platforma3 =
#platforma4 = 

platforme = [platforma1, platforma2]
clock = pygame.time.Clock()

start_screen = True

scroll = 0

speed = 0.2

#TODO
"""
double jump implementacija (reset ko je na platformi)
hitrejse premikanje elementov
platforme naj so naključne ampak ne preveč skupaj
"""
# to pove koliko jumpov ima na rzpolago
JUMPcount = 5


while igra:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            igra = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  #Začetek igre
            start_screen = False

    screen.blit(font.render(f"Za začetek pritisni SPACE", True, (88, 151, 252)),(X//2-500,Y//2-100))

    #igranje
    while not start_screen:
        print(f"jump count{JUMPcount}")
        time = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    

            #skok
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    if JUMPcount > 0:
                        speed = -0.5
                        JUMPcount -= 1





        #Pove ce se cat dotika platform
        colliding = [podlaga for podlaga in platforme if cat.colliderect(podlaga)]
        if len(colliding) > 0:
            a = colliding[0].y - cat.y
            #Da ostane na platformi
            if (a < 78 and a > 0) and speed > 0:
                #reset jumpov
                JUMPcount = 10
                speed = 0
            #Da se odbije od spodaj od platforme
            elif (a < -60) and speed < 0:
                speed *= -1

        #premikanje elementov levo po zaslonu
        
        speed += 0.01
        cat.y += speed * time
        ufo.x -= 2
        ice_cream.x -= 2
        lollipop.x -= 2
        krof.x -= 2
        milk.x -= 2
        platforma1.x -= 4
        platforma2.x -= 4


        for i in range(3):
            screen.blit(background, (i * bg_width + scroll,0))

        #scroll background
        scroll -= 5

        #reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        screen.blit(ufo_image, ufo)
        screen.blit(ice_cream_image, ice_cream)
        screen.blit(lollipop_image, lollipop)
        screen.blit(krof_image, krof)
        screen.blit(milk_image, milk)
        screen.blit(cat_image, cat)
        screen.blit(hotdog_image, platforma1)
        screen.blit(hotdog_image, platforma2)




        pygame.display.flip()

    pygame.display.flip()
    screen.blit(background, (0,0))



