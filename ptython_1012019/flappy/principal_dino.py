import sys, pygame, util
from pygame.locals import *
from heroe_dino import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def game():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Flappy" )
    background_image = util.cargar_imagen('fondo.jpg');
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH,SCREEN_HEIGHT) )
    bolso_image = util.cargar_imagen('bolso.jpg');
    bolso_image = pygame.transform.scale(bolso_image, (64,64) )
    bolso_rect = bolso_image.get_rect()
    bolso_rect.move_ip(SCREEN_WIDTH/2,SCREEN_HEIGHT-64)
    pygame.mouse.set_visible( False )
    heroe = Heroe()
    
    while True:       
        heroe.update((SCREEN_WIDTH,SCREEN_HEIGHT))      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(bolso_image, (SCREEN_WIDTH/2,SCREEN_HEIGHT-64))
        if heroe.rect.colliderect(bolso_rect):
            heroe.estado = 0

        
        pygame.display.update()
        pygame.time.delay(30)

      
if __name__ == '__main__':
      game()

