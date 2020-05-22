import pygame

WHITE = (255, 255, 255)

class Ball(pygame.sprite.Sprite):
    #this is going to be the class that represents a ball

    def __init__(self,x, y, direction):
        
        super().__init__()

        self.image = pygame.image.load("ball.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect(topleft = (x, y))
        
        #self.image = pygame.Surface([10,10])
        #self.image.fill(WHITE)
        self.image.set_colorkey((0,0,0))

        #pygame.draw.rect(self.image, WHITE, [10,10, 10, 10])

        #add top and bottom measurements
        self.top = self.rect.y
        self.bottom = self.rect.y + self.height

        #add left and right
        self.left = self.rect.x
        self.right = self.rect.x + self.width
 


    def get_rect(self):
        return self.rect

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        #add top and bottom measurements
        self.top = self.rect.y
        self.bottom = self.rect.y + self.height

        #add left and right
        self.left = self.rect.x
        self.right = self.rect.x + self.width
        
