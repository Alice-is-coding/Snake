import pygame
import sys
import pdb
from random import randrange
sys.path.append("..\\controller\\")


class Snake:
    """
    Constructor.

    :param Controller controller: The current controller.
    :param int speed: The speed of the snake.
    """
    def __init__(self, controller, speed):
        # Storing the controller.
        self.controller = controller
        # Creating the dictionary for the body.
        self.body = {}
        # Adding the head to the body.
        self.createHead((0,0,255))
        # Used as key to add new body parts to the dict body & used as a counter (score).
        self.countBody = 0
        self.speed = speed


    """
    Body getter.
    
    :return: The body property of the Snake object. 
    """
    def getBody(self):
        return self.body


    """
    Redirect to the createBody function with True given in parameter to say : we wannna create & store the head of the snake's body.
    
    param tuple(int, int, int) color: The color used to create the head of the snake. 
    """
    def createHead(self, color):
        self.createBody(color, True)


    """
    Create a rectangle -> actually call the controller which will call the view to create the rectangle. 
    
    :param tuple(int, int, int) color: The color used to create the body. 
    :param boolean isHead: (Optional) If passed, the head will be created and stored, otherwise a body part will be created. 
    """
    def createBody(self, color, isHead = False):
        # Saving the block size.
        blockSize = self.controller.getBlockSize()
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        # Generate random position.
        x = randrange(0, width, blockSize) # to remember : param randrange(begin, max, step) (we go 20 by 20 so that the square will always be visible in a grid' square)
        y = randrange(0, height, blockSize)
        # We only create the container to be transfered to the view via the controller, so that we store the container into the dictionary.
        rectObject = pygame.Rect(x + 1, y + 1, blockSize - 2, blockSize - 2)
        #print("x : ", x, " ; y : ", y)

        # If it is the head to be created & stored :
        if isHead:
            # We add the value x, y and rect for a key called "Head".
            self.body["Head"] = rectObject
            #print(self.body)
        # Call the controller to ask for the creation of a cube visible on the interface given the position, the color and if it's the head of the body or not.
        self.controller.drawRect(rectObject.x, rectObject.y, color, rectObject, isHead)


    '''
    To move the snake.
     
    :param event.type direction: (Optional) The direction the snake took. 
    '''
    def move(self, x, y, direction = None):
        # Declaration.
        width = self.controller.getWidth()
        height = self.controller.getHeight()

        for key, value in self.body.items():
            rect = self.body[key]
            # We fill the current rect container with a black color to show the movement of the snake.
            self.controller.fillSurface((0,0,0), rect)

            if rect.x + x > width:
                # We're moving to the right (we return to the left)
                rect.move_ip(- width, y)
            elif rect.x + x <= 0:
                # We're moving to the left (we return to the right)
                rect.move_ip(width, y)
            if rect.y + y > height:
                # We're moving down (we return to the top)
                rect.move_ip(x, - height + y)
            elif rect.y + y <= 0:
                # We're moving up (we return to the bottom)
                rect.move_ip(x, height + y)
            else:
                # We continue moving as expected
                rect.move_ip(x, y)

            # We ask the controller to ask the view to move the rect (drawing the rect moved thanks to "move_ip" actually).
            self.controller.drawRect(rect.x, rect.y, (0,0,255), rect, key == "Head", direction)


