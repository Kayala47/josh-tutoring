import sys, pygame
pygame.init()

size = (width, height) = 800, 600

def increase_speed(ballSpeed):
    changingSpeed = 0.1

    #gives that variable a new value
    
    if (ballSpeed[0] > 0):
        #add
         ballSpeed[0] = ballSpeed[0] + changingSpeed
    else:
        #subtract
         ballSpeed[0] = ballSpeed[0] - changingSpeed
   
    if (ballSpeed[1] > 0):
        #add
        ballSpeed[1] = ballSpeed[1] + changingSpeed
    else:
        #subtract
        ballSpeed[1] = ballSpeed[1] - changingSpeed
    
        
ballSpeed = [2, 2]
paddleSpeed = [0,1]

black = (0, 0, 0)
white = (255,255,255)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
paddle = pygame.image.load("blue-paddle.png")

ballrect = ball.get_rect()
paddleRect = paddle.get_rect()

startPos = [width/2,height/2]
ballrect = ballrect.move(startPos)

#variable for score
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(ballSpeed)
    paddleRect = paddleRect.move(paddleSpeed)

    #JOSH - your hw is to figure out how to change it so that it only
    #goes the other direction when it ACTUALLY hits the paddle.Otherwise
    # it should keep going

    if ballrect.right > width:
        #if the ball hits the paddle or the wall, reverses
        ballSpeed[0] = -ballSpeed[0]
    #every time it hits the right side, scores a point
    
    if ballrect.left <= paddleRect.right:
        #if the ball hits the paddle
        ballSpeed[0] = -ballSpeed[0] #still flip speed
        increase_speed(ballSpeed)#increase speed
        print(ballSpeed)

    if (ballrect.top < 0 or ballrect.bottom > height):
        #if ball hits top or bottom, goes in reverse
        ballSpeed[1] = -ballSpeed[1]

    if (paddleRect.bottom >= height) or (paddleRect.top <= 0):
        #if paddle touches top or bottom, reverses
        paddleSpeed[1] = -paddleSpeed[1]
        
    
    #tell the user how many points they have - update the scoreboard

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle, paddleRect)
    pygame.display.flip()
