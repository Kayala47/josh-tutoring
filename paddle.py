import pygame
WHITE = (255, 255, 255)
 
class Paddle(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load("blue-paddle.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
