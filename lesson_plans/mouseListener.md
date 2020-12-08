# Hi Josh #

Hope you've been well! Sorry for the long absence. I've got a lesson planned for you here that will show you the next component to making our computer game. 

## Mouse Listener ## 
The mouse listener class is used to get action events from the mouse, just like we did with the keyboard. It'll be able to capture clicks and respond to them, which is going to be really useful. That will mean our game will be able to point with the mouse and accept left and right clicks. 


Let's get started. 

## Tutorial ##

### Step 1 - Setup ###

Ok, so we've got lots of pieces set up already. You'll be using your existing code from when we were working with the buttons. Make sure that's still working well before starting off. 

However, I do want you to make some changes. Go ahead and comment our the buttons, so that we start with a blank slate. 

We're going to make 4 new buttons - top, right, bottom, left. The specific names will make sense later, but we need to start making these names more descriptive. Buttons 1-999 are going to get very confusing very soon. Arrange them according to their name, like this:

![](mouseButtons.drawio.png)

### Step 2 - MouseListener ###

Alrighty, now we're going to get into it!

Here's how to start implementing it:

1. In the main class, add the following code to the end of the name:
> implements MouseListener

2. For each button, you're going to add a MouseListener so that it can accept clicks.
Ex:
> topButton.addMouseListenerListener(this)

3. Now we're going to implement the actual feature that handles movement. This will be mostly up to you, but I'll give you the directions and some tips.

    - add a new method with the following name (the exact name is important!):
        > public void MouseReleased(MouseEvent e)
    - inside that method, we're going to write code to move the buttons when you click on them. Remember how we checked what the position of a button was before? 
    here are some tips:
        - For each action e, make sure that the click happened inside the button. That means we have to check the x and y locations to make sure the x and y of the click is inside the x and y of the button. 
        - if it is inside a button, that button should move. You know how to do this already. Set an "activatedButton" variable and move that button with the move method we defined before. 
        - the right button should move to the right, the top button should move up, bottom should move down, and left should move left. 

### Step 3 - Finished ###

Congrats! You got it!

Now you have some extra time if you want to do make it fancy. Here's some extra information about the MouseListener: https://docs.oracle.com/javase/tutorial/uiswing/examples/events/MouseEventDemoProject/src/events/MouseEventDemo.java

For extra credit, make something happens when the mouse hovers over the button. 

Have fun, and email me if you have any questions!











