import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('Run_1.png'),
                                        util.cargar_imagen('Run_2.png'),
                                        util.cargar_imagen('Run_3.png'),
                                        util.cargar_imagen('Run_4.png'),
                                        util.cargar_imagen('Run_5.png'),
                                        util.cargar_imagen('Run_6.png'),
                                        util.cargar_imagen('Run_7.png'),
                                        util.cargar_imagen('Run_8.png'),
                                        util.cargar_imagen('Run_9.png'),
                                        util.cargar_imagen('Run_10.png'),
                                        util.cargar_imagen('Run_11.png'),
                                        util.cargar_imagen('Run_12.png'),
                                        util.cargar_imagen('Run_13.png'),
                                        util.cargar_imagen('Run_14.png'),
                                        util.cargar_imagen('Run_15.png'),
                                        util.cargar_imagen('Run_16.png'),
                                        util.cargar_imagen('Run_17.png'),
                                        util.cargar_imagen('Run_18.png'),
                                        util.cargar_imagen('Run_19.png'),
                                        util.cargar_imagen('Run_20.png')]
                                    
                
        self.cont = 1
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 200)
        self.vel = [2,3]
        self.estado = 1
        
		
        
    def update(self,size):
        if self.estado == 1:
           teclas = pygame.key.get_pressed()
           if teclas[K_RIGHT]:
                self.vel [0] +=1
           if teclas[K_LEFT] and self.vel[0]>1:
                self.vel[0] -= 1
           self.rect.x = (self.rect.x + self.vel[0]) % size[0]
           self.cont = (self.cont + 1) % 20
           self.image = self.imagenes[self.cont]
        else:
            self.image = util.cargar_imagen('Dead_30.png')
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect.size = (128,128)
        self.rect.y = size[1] - 128
            
