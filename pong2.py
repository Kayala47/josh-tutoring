import pygame, random

from ball import Ball
from paddle import Paddle
pygame.init()
 
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0,0,0)
        
SCREENWIDTH=800
SCREENHEIGHT=800

speed = [4,4]
paddleSpeed = [0,4]

def increase_speed(speed):
    changingSpeed = 1
    speedLimit = 4

    #gives that variable a new value
    
    if (speed[0] > 0):
        #add
        speed[0] = min(speed[0] + changingSpeed, speedLimit)
    else:
        #subtract
        speed[0] = max(speed[0] - changingSpeed, -speedLimit)
   
    if (speed[1] > 0):
        #add
        speed[1] = min(speed[1] + changingSpeed, speedLimit)
    else:
        #subtract
        speed[1] = max(speed[1] - changingSpeed, -speedLimit)
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

#create the ball
ball = Ball(SCREENWIDTH/2, SCREENHEIGHT/2, 0)
ball.rect.x = 200
ball.rect.y = 300

#create the paddle
paddle = Paddle(WHITE)
 
# Add the ball to the list of objects
all_sprites_list.add(ball)
all_sprites_list.add(paddle)
 
#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
                
        #Game Logic
        all_sprites_list.update()
 
        #Drawing on Screen
        screen.fill(BLACK)
        
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)

        #paddle movement
        if paddle.rect.y > SCREENHEIGHT - paddle.height or paddle.rect.y < 0:
            paddleSpeed[1] = -paddleSpeed[1]

        paddle.move(paddleSpeed[0], paddleSpeed[1])
        
        
        #ball movement

        #hitting edges
        if ball.rect.x > SCREENWIDTH - ball.width:
            speed[0] = -speed[0]
        elif ball.rect.x < 0:
            #paddle missed
            print("missed")
            ball.kill()
            ball = Ball(SCREENWIDTH/2, SCREENHEIGHT/2, 0)
            ball.rect.x = 200
            ball.rect.y = 300
            

        if ball.rect.y > SCREENHEIGHT - ball.height or ball.rect.y < 0:
            speed[1] = -speed[1]

        #print("ball y = " + str(ball.rect.y))
        #print("paddle y = " + str(paddle.rect.y))
        if (ball.rect.x <= paddle.rect.x + paddle.width
            and (ball.rect.y + ball.height < paddle.rect.y + paddle.height
            or ball.rect.y > paddle.rect.y)):
            #ball hit paddle
            increase_speed(speed)
            speed[0] = -speed[0]


        ball.move(speed[0], speed[1])
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
