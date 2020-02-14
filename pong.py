import sys,pygame
pygame.init()

size = width, height =   800, 600

def increase_speed(speed):
    changingSpeed = 0.5

    #gives that variable a new value
    
    if (speed[0] > 0):
        #add
         speed[0] = speed[0] + changingSpeed
    else:
        #subtract
         speed[0] = speed[0] - changingSpeed
   
    if (speed[1] > 0):
        #add
        speed[1] = speed[1] + changingSpeed
    else:
        #subtract
        speed[1] = speed[1] - changingSpeed


speed = [2,2]
paddleSpeed = [0,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
paddle = pygame.image.load("blue-paddle.png")

ballrect = ball.get_rect()
paddlerect = paddle.get_rect()


startPos = [width/2,height/2]
ballrect = ballrect.move(startPos)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    ballrect = ballrect.move(speed)
    paddlerect = paddlerect.move(paddleSpeed)

    
    if (paddleRect.bottom >= ballRect.top and paddle.right >= ball.right) or (paddleRect.top <= ball.bottom and paddle.right >= ball.right):
        #misses
    

    else if ballrect.right > width:
        #if the ball hits the paddle or the wall, reverses
        speed[0] = -speed[0]
    #every time it hits the right side, scores a point
    
    else if ballrect.left <= paddlerect.right:
        #if the ball hits the paddle
        speed[0] = -speed[0] #still flip speed
        increase_speed(speed)#increase speed
        print(speed)

    if (ballrect.top < 0 or ballrect.bottom > height):
        #if ball hits top or bottom, goes in reverse
        speed[1] = -speed[1]

    if (paddleRect.bottom >= height) or (paddlerect.top <= 0):
        #if paddle touches top or bottom, reverses
        paddleSpeed[1] = -paddleSpeed[1]

    if (paddle.left >= ball.right):
        #ball passed the paddle
        del ball

#JOSH: your hw is to create a function (ball()) that:
        #create a new ball
        #give the new ball a starting position
        #start the ball moving
    
    
    #tell the user how many points they have - update the scoreboard

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle, paddlerect)
    pygame.display.flip()

