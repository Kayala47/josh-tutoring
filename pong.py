import sys, pygame
pygame.init()

size = (width, height) = 800, 600

def increase_speed(ballSpeed):
    addingSpeed = 0.01
        
    ballSpeed[0] = addingSpeed + ballSpeed[0]
    #gives that variable a new value
    ballSpeed[1] = ballSpeed[1] + addingSpeed
        
    

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

    if ballrect.right > width:
        #if the ball hits the paddle or the wall, reverses
        ballSpeed[0] = -ballSpeed[0]
    #every time it hits the right side, scores a point
    
    if ballrect.left <= paddleRect.right:
        #if the ball hits the paddle
        ballSpeed[0] = -ballSpeed[0] #still flip speed
        increase_speed(ballSpeed)#increase speed

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
