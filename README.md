# Snake Game

Hello everyone,
This is Khushbu Kathuria and this project is for building snake game using python.

The steps that we are going to take to build this game are :-

- 1. installing pygame into your pc
- 2. creating the screen
- 3. creating the snake
- 4. moving the snake
- 5. game over when snake hits the boundaries
- 6. adding the food
- 7. increasing the length of the snake
- 8. displaying the score

-----------------------------------------------------------------------
## Step 1 - Install pygame into pc
To do so just type 'pip install pygame' in your pc terminal.
(if after installation 'WARNING: You are using pip version 19.2.3, however version 20.0.2 is available.'
the above message is shown use 'python -m pip install --upgrade pip' command)

You must now have pygame installed.

## Step 2 - Creating the snake

## Step 3 - Moving the snake
To move the snake we will use the key events present in the KEYDOWN class of pygame.
The events that are used over here are, K_UP, K_DOWN, K_LEFT, and K_RIGHT to make the snake move up, down, left and right respectively.

## Step 4 - Game over when snake hits the boundaries:
In this snake game, if the player hits the boundaries of the screen, then he loses
NOW WE WILL use of an ‘if’ statement that defines the limits for the x and y coordinates of the snake to be less than or equal to that of the screen.

## Step 5: adding the food !
here we will add food for the snake and when the snake passes over that food the message 'YUMMY!!' will be shown
and quit and play again option will also be added.

## step 6: increasing the length of the snake
in this we increase the length of the snake whenever it eats food.
the length of the snake is basically a list with an initial value 1.
also we  show game over if the snake collides its own body

## step 7: Displaying the score
we will make a new function which will display the length of the snake subtracted by 1 because of the initial size of the Snake.

 
