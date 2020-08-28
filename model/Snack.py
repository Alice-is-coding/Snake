import sys
import pygame
import pdb
from random import randrange
sys.path.append("..\\controller\\")


class Snack:

    """
    Constructor.
    """
    def __init__(self, controller):
        # Storing the controller.
        self.controller = controller
        # Storing the color of a snack.
        self.color = (128,96,77)
        # Init the x pos to 0.
        self.x = 0
        # Init the y pos to 0.
        self.y = 0


    """
    Generate a random position x and y for the snack and call the controller to ask the view to show it on the surface. 
    """
    def randomSnack(self):
        # Declarations.
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        blockSize = self.controller.getBlockSize()

        # Generating a random x (pos).
        self.x = randrange(0, width, blockSize) # Note : param randrange(begin, max, step)
        # Generating a random y (pos).
        self.y = randrange(0, height, blockSize)

        # Creation of the container to be transfered to the view via the controller.
        rectObject = pygame.Rect(self.x + 1, self.y + 1, blockSize - 2, blockSize - 2)
        # Call to the controller to ask for the creation of a rectangle visible on the interface given the position and the color.
        self.controller.drawSnack(rectObject.x, rectObject.y, self.color, rectObject)


    """
    Snack position setter.
    """
    def setPos(self):
        self.randomSnack()


    """
    Snack x pos getter. 
    """
    def getPos_x(self):
        return self.x


    """
    Snack y pos getter. 
    """
    def getPos_y(self):
        return self.y

