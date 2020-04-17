# Hi Josh! #

As you can see, I've made some changes. This README file will now be used to host announcements, and your weekly homework. I've transferred all the definitons we created into the definitons.txt file, so you can always access those there. 

I'm sorry I've missed out last two sessions - things have been rather hectic here. To make sure you don't fall behind or forget what we were doing, I've made you a tutorial that you can follow to get some work done on Pong. 

A quick note: whenever you see a word highlighted `like this`, it means it has a special definiton that you should remember from our discussion. If you see one that you don't know, write it down. Look it up in that moment, but if you're still confused, make sure to tell me. If this does happen, do your best to continue with the lesson - I've made it so that you can just keep following the instructions even if there are parts you don't understand. 


## Finishing up Homework ##
Last time, I assigned you homework that would have you fix an issue with pong so that the ball would bounce correctly off the paddle, and mark a point whenever we missed it. In case you weren't able to finish, I'll teach you how to do that here. 

I'll start with the code we had last time we met. If you experience issues between the code you wrote and these instructions, you can always refer back to the main branch of github. Worst case, if you can't get it to work, clone the directory. 

In case you forgot how to clone it, do the following:

1. in file explorer, delete your "josh-tutoring" folder
2. in github, press the green button at the top of the repo that says "clone or download". It should let you copy a URL
3. in your terminal, navigate to the desktop and type:
```
git clone [THE URL THAT YOU JUST COPIED]

```

First Steps: Let's review what we've got:

Remember that the documentation page is your best friend. You can learn a lot about how this program can work if you read up on the parts you need to use. Check out the [Pygame Website](https://www.pygame.org/docs/) whenever you're stuck.

When we run the program, the ball bounces willy-nilly and eventually goes off the edge of the game map. Once it does, it gets stuck. We have to figure out some way to delete the ball and start over, otherwise our game can only handle one point being scored!

### Gameplan ###

Ok, the plan here is to re-make our ball so that it becomes a python object instead of just an image like we have it now. What that means is we'll be able to call a function like ball.update() and ball.delete() to stop and restart the game. 

Let's get started by creating the ball class. We'll need to pass it the proper `package` from pygame: pygame.sprite.Sprite). If you remember from our early lessons, a `sprite` is an object that moves in the game. So far, we've only been using an image, but that's not ideal, for reasons you've probably seen. 

### Creating a sprite ###

In order to create a sprite, we'll actually need a new file. This is just to make sure that we keep everything nice and tidy. 

In the same folder as everything else, create a new file and name it "ball.py". Copy and paste the following into it:

```python
import pygame
WHITE = (255, 255, 255)
class Ball(pygame.sprite.Sprite):
    def __init__(self,x, y, direction):
        super().__init__()
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

```

Let's go line by line and see what this does:

1. The first line imports pygame so we can use its built in functions
2. Here, I'm just setting up a color we can use later. You can search a color and then "RGB" to get this value
3. Here is where I'm defining a class for the sprite. "pygame.sprite.Sprite" inside the parenthesis means that I'm passing it a parent. So for this class, its parent would be a Sprite. That makes sense - a ball is a type of sprite in our game. 
4. Here, we define the init function. Remember, this is the one that it runs as soon as you create an object, so this one deals with setting up everything we'll need to use later.
5. This line is more complicated - basically, it calls the parent class (Sprite) to start. This sets up some important things in the background, but you don't need to know them for now
6. This line loads the image like we were doing before, except now its handled by the ball class
7. sets the width
8. sets the height
9. This line grabs the rectangle hitbox for the object. Now we're doing it here instead of in the main file
10. This line defines a new function that will help us move the ball

### Using the sprite ###

Now that we've created our ball object, we need to be able to use it! We've created our own `module`, and we can import it just as we would any other `package` that we get online. 

First things first: I want you to please go through your file and delete anything that mentions "ballRect" or "ball". We want to start fresh here. 

Now that you've done that, we can use the new file we created by `importing` it. At the top of the file, write a new line to import it, if you remember how.

...

If you don't remember how, there are two ways to import a package: 
 
- the bulky way: call `import ball`
- the efficient way: call `from ball import Ball`. This second way makes sure that we only take what we need from the module, instead of loading everything. 

...

Now we can use that class anywhere we want in our main file. To create a new ball object, call `ball = Ball(0,0,0)`. Then, you can set its x ad y coordinates like so:
```python
ball.rect.x = 200
ball.rect.y = 300
```

### Cleaning up the Code ###
Ok, remember how we deleted all mentions of ballRect and ball everywhere? You should already have a new ball variable since we just created it above, but its time to fix all the holes left by deleting ballRect. 

Here's a handy chart:

> When you see ____, replace it with ____
- ballRect ==> ball.rect
- ballRect.right ==> ball.rect.x + ball.rect.width
- ballRect.left ==> ball.rect.x
- ballRect.bottom ==> ball.rect.y + ball.rect.height
- ballRect.top ==> ball.rect.y

Think about why all these things changed, and what they mean now. None of the dimensions changed, but the way we have to represent them did. I'll give you a hint: the coordinates of any object start at the top left corner. So if you have a square of width 10 and start it at the very top left, it will have an x coordinate of 0. To get to its right side, you simply start at its x coordinate and add its width: 0 + 10 = square.right. See if you can figure out the formula for the rest. 

Lastly, you'll need to delete the line that says: `screen.blit(ball, ballRect)`, since we're no longer using those. Replace it with a simple call to ball.move(). Inside the parenthesis, put the speed dimensions:
```python
ball.move(speed[0], speed[1])
```

Now you should see it work!

## Your HW ##

Alrighty! Now that you've got the ball up and running, I want you to use these same instructions to make the paddle a sprite as well. It shouldn't take much modification, but here is where you're going to make sure that you actually understood all of this. 

Lastly, you'll notice there's a "branch" tab at the top of the github page. I've posted my answers in the "kvin-answers" branch. If you're really really stuck, the full answer is in "pong2.py". If you have any more questions, email me at ayala.kevin99@gmail.com. Happy coding, Josh!


