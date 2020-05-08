import pygame
WHITE = (255, 255, 255)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Instead we could
        self.image = pygame.image.load("blue-paddle.png").convert_alpha()
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        #add top and bottom measurements
        self.top = self.rect.y
        self.bottom = self.rect.y + self.height

        #add left and right
        self.left = self.rect.x
        self.right = self.rect.x + self.width
 
        

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        #add top and bottom measurements
        self.top = self.rect.y
        self.bottom = self.rect.y + self.height

        #add left and right
        self.left = self.rect.x
        self.right = self.rect.x + self.width
 

