import sys,pygame
from ball import Ball
from paddle import Paddle

pygame.init()

size = width, height =   800, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

all_sprites = pygame.sprite.Group()


def increase_speed(speed):
    changingSpeed = 0.1
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


    

    
speed = [2,2]
paddleSpeed = [0,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

paddle = pygame.image.load("blue-paddle.png").convert()

ball = Ball(0,0,0)

all_sprites.add(ball)

ballRect = ball.get_rect()
paddleRect = paddle.get_rect()

all_sprites.draw(screen)

startPos = [width/2,height/2]
ballRect = ballRect.move(startPos)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballRect = ballRect.move(speed)
    paddleRect = paddleRect.move(paddleSpeed)

    
    if (paddleRect.right >= ballRect.right) and (paddleRect.bottom >= ballRect.top or paddleRect.top <= ballRect.bottom ):
        #misses
        print("missed")
    

    elif ballRect.right > width:
        #if the ball hits the the wall, reverses
        speed[0] = -speed[0]
    #every time it hits the right side, scores a point
    
    elif ballRect.left <= paddleRect.right and ballRect.top >= paddleRect.top and ballRect.bottom <= paddleRect.bottom:
        #if the ball hits the paddle
        speed[0] = -speed[0] #still flip speed
        increase_speed(speed)#increase speed
        #print(speed)

    if (ballRect.top < 0 or ballRect.bottom > height):
        #if ball hits top or bottom, goes in reverse
        speed[1] = -speed[1]

    if (paddleRect.bottom >= height) or (paddleRect.top <= 0):
        #if paddle touches top or bottom, reverses
        paddleSpeed[1] = -paddleSpeed[1]

    if (paddleRect.left >= ballRect.right):
        #ball passed the paddle
        #del ball
        print("ball went past paddle")

#JOSH: your hw is to create a function (ball()) that:
        #create a new ball
        #give the new ball a starting position
        #start the ball moving
 
    
    #tell the user how many points they have - update the scoreboard

    screen.fill(black)
    #screen.blit(ball, ballRect)
    screen.blit(paddle, paddleRect)
    pygame.display.flip()

