import pygame
import sys
import pdb
sys.path.append("..\\view\\")
sys.path.append("..\\model\\")
from view import SnakeInterface
from Snake import Snake

#pdb.set_trace()

# Globals
width = 500 # Size of the width (but also height as we choose to generate a square interface).
blockSize = 20 # Size of a block.


class Controller:
    """
    Constructor.
    """
    def __init__(self):
        # Init the game.
        self.interface = SnakeInterface(width, width, blockSize, self)
        self.snake = Snake(self, 5)
        self.snakeBody = self.snake.getBody()
        #print(self.snakeBody)

    """
    Controller getter.
    
    :return : the current controller. 
    """
    def getController():
        return self


    '''
    The main function.
    '''
    def main(self):
        # Initializing a flag to enter an infinite loop.
        Flag = True
        # Init a timer.
        clock = pygame.time.Clock()
        # Positions.
        x = 0
        y = 0
        direction = None
        # speed
        speed = self.snake.speed

        # Entering an infinite loop (necessary in order to display the game continually as long as we don't ask to quit the game).
        while Flag:
            # Allowing the possibility to quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        x = blockSize
                        y = 0
                        direction = pygame.K_RIGHT
                    elif event.key == pygame.K_DOWN:
                        x = 0
                        y = blockSize
                        direction = pygame.K_DOWN
                    elif event.key == pygame.K_UP:
                        x = 0
                        y = - blockSize
                        direction = pygame.K_UP
                    elif event.key == pygame.K_LEFT:
                        x = - blockSize
                        y = 0
                        direction = pygame.K_LEFT

            # Moving the snake
            self.snake.move(x, y, direction)
            # Updating the interface of the game.
            pygame.display.update()
            clock.tick(speed)


    """
    Call the drawRect function of the interface object to draw the rectangle.
    
    :param int x: Abscissa.
    :param int y: Ordinate.
    :param tuple(int, int, int) color: Color of the Rect object ((R,G,B) format).
    :param Rect rectObject: Rect object to be drawn.
    :param boolean isHead: (Optional) To know if it's the head of the snake which is to be drawn. 
    :param event.key direction: (Optional) To know in which direction the snake goes. 
    """
    def drawRect(self, x, y, color, rectObject, isHead = False, direction = None):
        # Call the view to ask for the creation of a cube.
        self.interface.drawRect(x, y, color, rectObject, isHead, direction)


    """
    Block size getter.
    
    :return: The block size. 
    """
    def getBlockSize(self):
        return blockSize


    """
    Width getter.
    
    :return: The width of the interface object.
    """
    def getWidth(self):
        return self.interface.getSurface().get_width()


    """
    Height getter.
    
    :return: The height of the interface object. 
    """
    def getHeight(self):
        return self.interface.getSurface().get_height()


    """
    To fill the surface with a color. 
    
    :param tuple(int, int, int) color: The color used to fill the surface ((R, G, B) format).
    :param Rect rectObject: (Optional) If used, the Rect object will be filled with the color and not the entire surface.
    """
    def fillSurface(self, color, rectObject = None):
        self.interface.fillSurface(color, rectObject)


if __name__ == "__main__":
    # Execute only if run as a script.
    self = Controller()
    self.main()