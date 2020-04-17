import pygame

WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    #this is going to be the class that represents a ball

    def __init__(self,x, y, direction):
        
        super().__init__()

        print("ball created at" + str(x) + " " + str(y))

        self.image = pygame.image.load("ball.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
       # self.image = pygame.Surface([10,10])
        #self.image.fill(WHITE)
        self.image.set_colorkey((0,0,0))

        #pygame.draw.rect(self.image, WHITE, [10,10, 10, 10])

        self.rect = self.image.get_rect()

    def get_rect(self):
        return self.rect

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
