import pygame
import sys
from model.Snack import Snack
from model.Snake import Snake
from view.view import SnakeInterface

# Globals
WIDTH = 500  # Size of the width (but also height as we choose to generate a square interface).
BLOCKSIZE = 20  # Size of a block.


class Controller:
    """
    According to the MVC design pattern, this class allows to control data and managing data flow
    between the Model and the View.
    """

    def __init__(self):
        """
        Constructor.
        Initialize the view (SnakeInterface) and the model (Snake and Snack).
        """
        # Init the game.
        self.speed = 15
        self.score = 0
        self.bestScore = 0
        self.interface = SnakeInterface(WIDTH, WIDTH, BLOCKSIZE, self)
        self.snake = Snake(self, (48, 235, 106))
        self.snakeBody = self.snake.getBody()
        self.snakeHead = self.snake.getHead()
        self.snack = Snack(self, (157, 125, 94))
        self.direction = None
        self.newDirection = None

        self.snack.setPos()  # We ask a new position for the snack.

    def main(self):
        """
        The main function.
        Infinite loop allowing the game to work as long as the user doesn't ask for quiting the game.
        """
        # Initializing a flag to enter an infinite loop.
        Flag = True
        # Init a timer.
        clock = pygame.time.Clock()
        # Positions.
        x = 0
        y = 0
        # Will be used to store the new direction.
        newDirection = self.getNewDirection()
        # Will be used to store the previous direction in order for the snake to not be allowed to go back on himself.
        direction = self.getDirection()
        # Some useful snake attributes.
        speed = self.speed
        snakeColor = self.snake.getColor()

        while Flag:
            # Get all the events of pygame.
            for event in pygame.event.get():
                # Allowing the possibility to quit the game.
                if event.type == pygame.QUIT:
                    Flag = False
                # Targeting the keydown events.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and direction != pygame.K_LEFT:
                        # The snake moves by the block size to the right.
                        x = BLOCKSIZE
                        y = 0
                        newDirection = pygame.K_RIGHT
                    elif event.key == pygame.K_DOWN and direction != pygame.K_UP:
                        # The snakes moves by the block size to the bottom.
                        x = 0
                        y = BLOCKSIZE
                        newDirection = pygame.K_DOWN
                    elif event.key == pygame.K_UP and direction != pygame.K_DOWN:
                        # The snake moves by the block size to the top.
                        x = 0
                        y = - BLOCKSIZE
                        newDirection = pygame.K_UP
                    elif event.key == pygame.K_LEFT and direction != pygame.K_RIGHT:
                        # The snake moves by the block size to the left.
                        x = - BLOCKSIZE
                        y = 0
                        newDirection = pygame.K_LEFT
                    # NB : We didn't update the newDirection variable here (which could let think that it's redundant)
                    # but it was on purpose: if we did such thing, the snake could have been able to go back on himself
                    # after having pressed the same key twice.
                    # Storing the direction which will become the previous one at the next iteration of the loop.
                    direction = newDirection
                # Targeting the cursor movements.
                if event.type == pygame.MOUSEMOTION:
                    # Event management.
                    self.interface.mouse_onHover()
                # Targeting the cursor clicks.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Event management.
                    self.interface.mouse_onButtonDown()
            isgameOver = self.compareSnakeHeadAndBodyPos()
            # Moving the snake according to the direction chosen by the user if it's not game over.
            if not isgameOver:
                self.snake.move(x, y, snakeColor, newDirection)
                # Calculate if the snake ate the snack.
                ateSnack = self.compareSnackAndSnakePos()
                if ateSnack:
                    # Creating a new body part for the snake.
                    self.snake.createBody(snakeColor, False, x, y)
                    self.interface.updateScoreBanner(self.snake.getScore())
                    # Generating a new snack position.
                    self.snack.setPos()
            else:
                # [A solution (useful for the future)] keyValPair = self.snakeBody[0].collidedict(self.snakeBody, True)
                # self.interface.gameOver(self.snakeBody[keyValPair[0]], direction)
                self.setNewScore()
                # If the new score is the new bestScore:
                if self.isNewBestScore(self.score):
                    # The bestScore attribute takes the score value and we call gameOver view with the new bestScore.
                    self.setBestScore(self.score)
                    self.callGameOver(self.bestScore)
                else:
                    # Else, there's not a new bestScore, so we call the gameOver view without arg.
                    self.callGameOver()
            # Updating the interface of the game.
            pygame.display.update()
            clock.tick(speed)
        # We quit the forever loop -> we quit the game.
        self.quit()

    def getController(self):
        """
        Controller getter.

        Returns
        -------
        Controller
            The current controller object.
        """
        return self

    def getBlockSize(self):
        """
        Block size getter.

        Returns
        -------
        int
            The size of a block.
        """
        return BLOCKSIZE

    def getWidth(self):
        """
        Width getter.

        Returns
        -------
        int
            The width of the interface object.
        """
        return self.interface.getSurface().get_width()

    def getHeight(self):
        """
        Height getter.

        Returns
        -------
        int
            The height of the interface object.
        """
        return self.interface.getSurface().get_height()

    def getScore(self):
        """
        Score getter.

        Returns
        -------
        int
            The score of the user (calculated according to the number of body parts the snake got).
        """
        return self.score

    def getBestScore(self):
        return self.bestScore

    def getNewDirection(self):
        """
        New direction getter.

        Returns
        -------
        pygame.key
            The new direction taken.
        """
        return self.newDirection

    def getDirection(self):
        """
        Direction getter.

        Returns
        -------
        pygame.key
            The direction taken (current one or old one).
        """
        return self.direction

    def getBannerHeight(self):
        """
        Score banner height getter.

        Returns
        -------
        int
            The height of the score banner.
        """
        return self.interface.getBannerHeight()

    def setNewScore(self):
        """
        Score attribute setter.

        Returns
        -------
        None
        """
        newScore = self.snake.getScore()
        self.score = newScore

    def setBestScore(self, bestScore):
        """
        BestScore attribute setter.

        Parameters
        ----------
        bestScore : int
            The new bestScore.

        Returns
        -------
        None
        """
        self.bestScore = bestScore

    def compareSnackAndSnakePos(self):
        """
        Compare the position of the snake and the position of the snack.

        Returns
        -------
        bool
            True if they are at the same position, False otherwise.
        """
        # Declaration.
        snakeBody = self.snakeBody
        snakeHead = self.snakeHead['head']
        snackPos_x = self.snack.getPos_x()
        snackPos_y = self.snack.getPos_y()
        isAtTheSamePos = False

        # Browsing all the items of the snakeBody.
        for key, value in snakeBody.items():
            # If an item is at the same place of the snack:
            if snakeBody[key].x - 1 == snackPos_x and snakeBody[key].y - 1 == snackPos_y:
                # We change the boolean var to true.
                isAtTheSamePos = True
        if snakeHead.x - 1 == snackPos_x and snakeHead.y - 1 == snackPos_y:
            isAtTheSamePos = True
        return isAtTheSamePos

    def compareSnakeHeadAndBodyPos(self):
        """
        Compare the head's position of the snake and the rest of his body.

        Returns
        -------
        bool
            True if the head is at the same position as a body part, False otherwise.
        """
        # Declarations.
        snakeBody = self.snakeBody
        snakeHead = self.snakeHead['head']
        # Body parts counter.
        k = 1
        biteHimself = False

        # While the snake didn't bite himself and we didn't reach the end of his body.
        while not biteHimself and k < len(snakeBody):
            # Storing the current body part.
            rect = snakeBody[k]
            # If the head is at the same position of the body part (rect)
            if rect.contains(snakeHead):
                biteHimself = True
            else:
                k += 1
        return biteHimself

    def isNewBestScore(self, newScore):
        """
        Calculates if newScore passed in arg is the new bestScore or not.

        Parameters
        ----------
        newScore : int
            The new score.

        Returns
        -------
        bool
            True if newScore is the new bestScore, False otherwise.
        """
        # Declarations.
        bestScore = self.bestScore

        if newScore > bestScore:
            return True
        else:
            return False

    def fillSurface(self, color, rectObject=None):
        """
        Fill the surface with a color (by calling the view).

        Parameters
        ----------
        color : tuple of int
            The color used to fill the surface ((R,G,B) format).
        rectObject : pygame.Rect, optional
            If used, the Rect object will be filled with the color, the entire surface if not.

        Returns
        -------
        None
        """
        self.interface.fillSurface(color, rectObject)

    def drawRect(self, color, rectObject):
        """
        Calls the drawRect function of the SnakeInterface object to draw the rectangle.

        Parameters
        ----------
        color : tuple of int
            Color of the Rect object ((R,G,B) format).
        rectObject : pygame.Rect
            Rect object to be drawn.

        Returns
        -------
        None
        """
        self.interface.drawRect(color, rectObject)

    def drawCircle(self, x, y, color):
        """
        Draws a circle on the surface (by calling the view).

        Parameters
        ----------
        x : int
            Position x.
        y : int
            Position y.
        color : tuple of int
            The color of the circle.

        Returns
        -------
        None
        """
        self.interface.drawCircle(x, y, color)

    def drawSnack(self, color, rectObject):
        """
        Draws a snack on the interface (by calling the view):
        If the snack position is the same as the snake: the method asks for a new position.
        Otherwise, the drawRect function is called to actually draw it.

        Parameters
        ----------
        color : tuple of int
            Color of the Rect object ((R,G,B) format).
        rectObject : pygame.Rect
            Rect object to be drawn (the snack).

        Returns
        -------
        None
        """
        # Declaration.
        snackIsOnSnake = self.compareSnackAndSnakePos()

        if snackIsOnSnake:
            self.snack.setPos()
        else:
            self.drawRect(color, rectObject)

    def callGameOver(self, bestScore=None):
        """
        Calls the gameOver view (by calling the view).

        Parameters
        ----------
        bestScore : int, optional
            To be mentioned if there's a new best score. Not necessary otherwise.

        Returns
        -------
        None
        """
        self.interface.callGameOver(self.snakeHead['head'], self.snakeHead['eye1'], self.snakeHead['eye2'],
                                    self.score, bestScore)

    def resetGame(self):
        """
        Resets all the attributes of the Controller object, except the bestScore attribute.
        Then it calls the main function in order to actually reset the game.

        Returns
        -------
        None
        """
        # Reset attributes.
        self.interface = SnakeInterface(WIDTH, WIDTH, BLOCKSIZE, self)
        self.snake = Snake(self, (48, 235, 106))
        self.snakeBody = self.snake.getBody()
        self.snakeHead = self.snake.getHead()
        self.snack = Snack(self, (157, 125, 94))
        self.snack.setPos()
        self.score = 0
        self.direction = None
        self.newDirection = None

        self.main()

    def quit(self):
        """
        To quit the game.

        Returns
        -------
        None.
        """
        pygame.quit()
        sys.exit()
