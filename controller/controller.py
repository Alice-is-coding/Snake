import pygame
import sys
import pdb
sys.path.append("..\\view\\")
sys.path.append("..\\model\\")
from view import SnakeInterface
from Snake import Snake
from Snack import Snack

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
        self.snake = Snake(self, 10, (0,0,255))
        self.snakeBody = self.snake.getBody()
        self.snack = Snack(self)
        self.snack.setPos() # We ask a new position for the snack.
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
        # The speed of the snake.
        speed = self.snake.speed
        # The color of the snake.
        snakeColor = self.snake.getColor()
        
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
            self.snake.move(x, y, snakeColor, direction)
            ateSnack = self.compareSnackAndSnakePos()
            if ateSnack:
                #print("x = ", x, " ; y = ", y)
                # We create a new body part for the snake.
                self.snake.createBody(snakeColor, False, x, y)
                # We generate a new snack position.
                self.snack.setPos()
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


    """
    Call the drawRect function if the position of the snack is not the same as the snake. Otherwise, a new positin for the snack is asked. 
    
    :param int x: Abscissa.
    :param int y: Ordinate.
    :param tuple(int, int, int) color: Color of the rectObject ((R, G, B) format).
    :param Rect rectObject: Rect object to be drawn (the snack). 
    """
    def drawSnack(self, x, y, color, rectObject):
        # Declaration.
        snackOnSnake = self.compareSnackAndSnakePos()

        if snackOnSnake:
            self.snack.setPos()
        else:
            self.drawRect(x, y, color, rectObject)
    

    """
    Compare the position of the snake and the position of the snack. 
    
    :return: True if they are at the same position, else False.
    """
    def compareSnackAndSnakePos(self):
        # Declaration.
        snakeBody = self.snakeBody
        snackPos_x = self.snack.getPos_x()
        #print("snack pos x : ", snackPos_x)
        snackPos_y = self.snack.getPos_y()
        #print("snack pos y : ", snackPos_y)
        isAtTheSamePos = False # Init the boolean to false in order to test.

        # We browse all the items of the snake.
        for key, value in snakeBody.items():
            #print("snake pos x : ", snakeBody[key].x)
            #print("snake pos y : ", snakeBody[key].y, "\n")
            # If an item is placed at the same place of the snack:
            if snakeBody[key].x - 1 == snackPos_x and snakeBody[key].y - 1 == snackPos_y :
                # We change the boolean var to true.
                isAtTheSamePos = True
        return isAtTheSamePos


if __name__ == "__main__":
    # Execute only if run as a script.
    self = Controller()
    self.main()