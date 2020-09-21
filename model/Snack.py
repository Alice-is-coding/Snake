import sys
import pygame
from random import randrange

sys.path.append("..\\controller\\")


class Snack:
    """
    Creates a snack and displays it.
    """

    def __init__(self, controller, color):
        """
        Constructor.

        Parameters
        ----------
        controller : controller.controller.Controller
            The controller used for the game.
        color : tuple of int
            The color of the snack.
        """
        self.controller = controller
        # Storing the color of a snack.
        self.color = color
        # Init the x pos & y pos to 0.
        self.x = 0
        self.y = 0

    def getPos_x(self):
        """
        Snack posX getter.

        Returns
        -------
        int
            The posX of the Snack object.
        """
        return self.x

    """
    Snack y pos getter. 
    """

    def getPos_y(self):
        """
        Snack posY getter.

        Returns
        -------
        int
            The posY of the Snack object.
        """
        return self.y

    def setPos(self):
        """
        Snack position setter.

        Returns
        -------
        None
        """
        self.randomSnack()

    def randomSnack(self):
        """
        Generates a random position x and y for the snack, then calls the controller to ask the view to show it
        on the surface.

        Returns
        -------
        None
        """
        # Declarations.
        width = self.controller.getWidth()
        bannerHeight = self.controller.getBannerHeight()
        height = self.controller.getHeight()
        blockSize = self.controller.getBlockSize()

        # Generating a random x and y (pos).
        self.x = randrange(0, width, blockSize)  # Note : param randrange(begin, max, step)
        self.y = randrange(bannerHeight, height, blockSize)

        # Creation of the container to be transferred to the view via the controller.
        rectObject = pygame.Rect(self.x + 1, self.y + 1, blockSize - 2, blockSize - 2)
        # Calls the controller to ask for the drawing of the rect visible on the interface given the pos and the color.
        self.controller.drawSnack(self.color, rectObject)
