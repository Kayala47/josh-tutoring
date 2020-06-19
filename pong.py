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

SCREENHEIGHT=650


speed = [4,4]
paddleSpeed = [0,4]

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

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



def removeBall(ball, spritesList):

    spritesList.remove(ball)

    ball.kill()
    ball = Ball(SCREENWIDTH/2, SCREENHEIGHT/2, 0)
    ball.rect.x = 200
    ball.rect.y = 300

    spritesList.add(ball)

    return ball
    
def updatePaddle(paddle, upDown):
    keyPressed = pygame.key.get_pressed()

    (up, down) = upDown

    #red uses arrow keys
    #blue should use wasd, really just w = up, s = down
    if keyPressed[up]:
        if (paddle.rect.top - 10 >= 0):
            paddle.move(0, -10)
    elif keyPressed[down]:
        if (paddle.rect.bottom + 10 <= SCREENHEIGHT):
            paddle.move(0, 10)

def updateScore(redPts, bluePts):
    #draw_text = def draw_text(surf, text, size, x, y):

    text = "Red has " + str(redPts) + " points. Blue has " + str(bluePts) + " points."
    size = 25
    x = SCREENWIDTH/4
    y = 10

    font_type = pygame.font.SysFont('arial', size)
    return font_type.render(text, True, WHITE)

    
    
    
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

paddle = Paddle("blue")
paddle.rect.x = 0
paddle.rect.y = 0

redPaddle = Paddle("red")
redPaddle.rect.x = SCREENWIDTH - redPaddle.width
redPaddle.left = SCREENWIDTH - redPaddle.width
paddle.rect.y = 0

paddle = Paddle(WHITE)

 
# Add the ball to the list of objects
all_sprites_list.add(ball)
all_sprites_list.add(paddle)

all_sprites_list.add(redPaddle)

# Tracking points
redPts = 0
bluePts = 0

#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:

            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False

        updatePaddle(paddle, (pygame.K_w, pygame.K_s))
        updatePaddle(redPaddle, (pygame.K_UP, pygame.K_DOWN))
        

        
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


        if paddle.rect.colliderect(ball.rect):
            #ball hit left paddle
            increase_speed(speed)
            speed[0] = -speed[0]

        elif redPaddle.rect.colliderect(ball.rect):
            #ball hit right paddle
            increase_speed(speed)
            speed[0] = -speed[0]
            
    

        if ((paddle.top > ball.bottom and ball.right <= paddle.right) or
        (paddle.bottom < ball.top and ball.right <= paddle.right)):
            #ball goes through left side

            print("I think it missed the left side")
            
            ball = removeBall(ball, all_sprites_list)
            speed = [4,4]
            redPts = redPts + 1
            print(redPts)
            

        elif ((redPaddle.top > ball.bottom and ball.left >= redPaddle.left) or
        (redPaddle.bottom < ball.top and ball.left >= redPaddle.left)):
            #ball goes through right side
            
            ball = removeBall(ball, all_sprites_list)
            speed = [4,4]
            bluePts = bluePts + 1
            print(bluePts)

            
            

            
            

        if ball.rect.y > SCREENHEIGHT - ball.height or ball.rect.y < 0:
            speed[1] = -speed[1]


        ball.move(speed[0], speed[1])
 
        #Refresh Screen
        renderedText = updateScore(redPts, bluePts)
        screen.blit(renderedText, (SCREENWIDTH/4, 10))
        pygame.display.flip()
        
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
