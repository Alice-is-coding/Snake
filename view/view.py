import pygame
import sys
import pdb
from random import randint
sys.path.append("..\\controller\\")


class SnakeInterface:
    '''
    Constructor.
    Initialize the game interface.

    :param int width: The width of the surface.
    :param int height: The height of the surface.
    :param int blockSize: The size of a block.
    :param Controller controller: The controller used for the game.
    '''
    def __init__(self, width, height, blockSize, controller):
        # Init pygame modules.
        pygame.init()
        # Store the controller.
        self.controller = controller
        # Save the block size.
        self.blockSize = blockSize
        # Config of the interface with the dimensions of the screen.
        self.surface = pygame.display.set_mode((width, height))
        # Setting the game's title.
        pygame.display.set_caption("Snake Game")
        # Generate the grid.
        self.generateGrid(self.surface, width, height)


    '''
    Generate the grid and displays it on the game's interface. 
    
    :param Surface surface: The current surface of the game. 
    :param int width: The width of the surface. 
    :param int height: The height of the surface. 
    '''
    def generateGrid(self, surface, width, height):
        # Creating the grid thanks to a for loop.
        for x in range(width):
            for y in range(height):
                # Creating a container for a rectangular object.
                rect = pygame.Rect(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize)
                # Drawing the form on the interface.
                pygame.draw.rect(surface, (255,255,255), rect, 1)


    """
    Surface getter. 
    
    :return: The surface of the game.
    """
    def getSurface(self):
        return self.surface


    """
    Create a rectangle on the interface given x, y, and a color.
    
    :param int x: Abscissa. 
    :param int y: Ordinate. 
    :param tuple(int, int, int) color: The color used to draw the rectangle. 
    :param Rect rectObject: The Rect object to be drawn on the surface. 
    :param boolean isHead: (Optional) If used, the eyes will be drawn on this rectangle. 
    :param event.type direction: (Optional) The direction used. 
    """
    def drawRect(self, x, y, color, rectObject, isHead = False, direction = None):
        # Creating the rectangle.
        pygame.draw.rect(self.surface, color, rectObject)
        # If it is the head of the snake's body :
        if isHead:
            # In addition, we draw the eyes, so that the user knows where to go.
            self.drawEyes(x, y, direction)


    '''
    Draw the eyes of the snake depending on the direction. 
    
    :param int x: Abscissa.
    :param int y: Ordinate. 
    :param event.type direction: (Optional) The direction taken by the snake. 
    '''
    def drawEyes(self, x, y, direction = None):
        if direction == pygame.K_UP:
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 16)), int(y + (self.blockSize - 16))), 2, 0)
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 7)), int(y + (self.blockSize - 16))), 2, 0)
        elif direction == pygame.K_DOWN:
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 16)), int(y + (self.blockSize - 6))), 2, 0)
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 7)), int(y + (self.blockSize - 6))), 2, 0)
        elif direction == pygame.K_LEFT:
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 17)), int(y + (self.blockSize - 15))), 2, 0)
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 17)), int(y + (self.blockSize - 7))), 2, 0)
        elif direction == pygame.K_RIGHT:
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 6)), int(y + (self.blockSize - 15))), 2, 0)
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 6)), int(y + (self.blockSize - 7))), 2, 0)
        else:
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 7)), int(y + (self.blockSize // 2))), 2, 0)
            pygame.draw.circle(self.surface, (0,0,0), (int(x + (self.blockSize - 16)), int(y + (self.blockSize // 2))), 2, 0)
            

    """
    Fill the surface (optionally the rect passed in param) with a certain color (black by default).
    
    :param tuple(int, int, int) color: The color used to fill the surface. 
    :param Rect rectObject: (Oprional) If passed, the rectangle will be filled with the color instead of the entire surface. 
    """
    def fillSurface(self, color, rectObject = None):
        self.surface.fill(color, rectObject)
        



