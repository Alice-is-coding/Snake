import pygame
import sys
from .gameOver import GameOver
from .scorebanner import ScoreBanner

sys.path.append("..\\controller\\")


class SnakeInterface:
    """
    Manages the creation of the snake game interface.
    Manages all the graphical aspects of the game as long as the user doesn't quit it.
    """

    def __init__(self, width, height, blockSize, controller):
        """
        Constructor.
        Initialize the game interface.

        Parameters
        ----------
        width : int
            The width of the surface.
        height : int
            The height of the surface.
        blockSize : int
            The size of a block.
        controller : controller.controller.Controller
            The controller used for the game.
        """
        # Init pygame modules.
        pygame.init()
        self.controller = controller
        # Config of the interface with the dimensions of the screen.
        self.surface = pygame.display.set_mode((width, height))
        self.blockSize = blockSize
        # Save dimensions.
        self.width = width
        self.height = height

        # Setting the game's title.
        pygame.display.set_caption("Snake Game")
        self.generateGrid(self.surface, width, height)
        self.scoreBanner = ScoreBanner(self, controller, (0, 0, 0), (255, 255, 255), self.width - 2, self.blockSize * 2)
        # Useful when the user looses.
        self.gameOver = None

    def getSurface(self):
        """
        Surface getter.

        Returns
        -------
        pygame.Surface
            The surface of the game.
        """
        return self.surface

    def getBannerHeight(self):
        """
        Score banner height getter.

        Returns
        -------
        int
            The height of the score banner.
        """
        return self.scoreBanner.getBannerHeight()

    def setGameOver(self, gameOver):
        """
        GameOver attribute setter.

        Parameters
        ----------
        gameOver : GameOver
            The gameOver view.

        Returns
        -------
        None
        """
        self.gameOver = gameOver

    def isSetGameOver(self):
        """
        Calculates if the gameOver attribute is set or not.

        Returns
        -------
        bool
            True if the gameOver attribute is set, False otherwise.
        """
        return self.gameOver is not None

    def generateGrid(self, surface: pygame.Surface, width, height):
        """
        Generates the grid and displays it on the game's interface.

        Parameters
        ----------
        surface : pygame.Surface
            The current surface of the game.
        width : int
            The width of the surface.
        height : int
            The height of the surface.

        Returns
        -------
        None
        """
        for x in range(width):
            for y in range(height):
                # Creating a container for a rectangular object.
                rect = pygame.Rect(x * self.blockSize, y * self.blockSize, self.blockSize, self.blockSize)
                # Drawing the form on the interface.
                pygame.draw.rect(surface, (255, 255, 255), rect, 1)

    def drawRect(self, color, rectObject):
        """
        Creates a rectangle on the interface given x, y, and a color.

        Parameters
        ----------
        color : tuple of int
            The color used to draw the rectangle.
        rectObject : pygame.Rect
            The Rect object to be drawn on the surface.

        Returns
        -------
        None
        """
        pygame.draw.rect(self.surface, color, rectObject)

    def drawCircle(self, x, y, color=(0, 0, 0)):
        """
        Draws the eyes of the snake.

        Parameters
        ----------
        x : int
            Abscissa.
        y : int
            Ordinate.
        color : tuple of int, optional
            The color used to draw the rectangle.

        Returns
        -------
        None
        """
        pygame.draw.circle(self.surface, color, (x, y), self.blockSize // 10)

    def fillSurface(self, color, rectObject=None):
        """
        Fills the surface (or the Rect instead (if passed in param)) with a specific color.
        Parameters
        ----------
        color : tuple of int
            The color used to fill the surface.
        rectObject : pygame.Rect or tuple of int or tuple of float, optional
            If passed, the rectangle will be filled with the color instead of the entire surface.

        Returns
        -------
        None
        """
        self.surface.fill(color, rectObject)

    def blit(self, source: pygame.Surface, destination):
        """
        Draws one image onto another.
        Useful for other classes using the SnakeInterface class : other classes use this function to bring changes to
        the surface without having to store the surface attribute from the SnakeInterface class.

        Parameters
        ----------
        source : pygame.Surface
            The source to be drawn onto the destination.
        destination : pygame.Surface or tuple of int or tuple of float
            The destination on which the source is to be drawn.

        Returns
        -------
        None
        """
        self.surface.blit(source, destination)

    def updateScoreBanner(self, score):
        """
        Calls the Score view in order to update the score banner displayed on the main surfac.

        Parameters
        ----------
        score : int
            The current score.

        Returns
        -------
        None
        """
        self.scoreBanner.updateScoreBanner(score)

    def callGameOver(self, head, eye1, eye2, score, bestScore):
        """
        Calls the gameOver function of the gameOver object (also instantiate it if not the case yet).

        Parameters
        ----------
        head : pygame.Rect
            The snake's head.
        eye1 : pygame.Rect
            The first snake's eye.
        eye2 : pygame.Rect
            The second snake's eye.
        score : int
            The current score.
        bestScore : int
            The new best score.

        Returns
        -------

        """
        if self.gameOver is None:
            gameOver = GameOver(self.controller, self)
            self.setGameOver(gameOver)
            gameOver.showGameOver(head, eye1, eye2, score, bestScore)

    def mouse_onHover(self):
        """
        Event onHover.
        When the gameOver view is instantiated,
        aesthetic effect when the cursor passes above one of the two buttons (play again / quit).

        Returns
        -------
        None
        """
        if self.gameOver is not None:
            # Declarations.
            mouse = pygame.mouse.get_pos()  # Returns a (x, y) relative to the top-left corner of the display.
            self.gameOver.mouse_onHover(mouse)

    def mouse_onButtonDown(self):
        """
        Event onButtonDown.
        Allowed when the gameOver attribute is instantiated.
        Calls the function (same name) of the GameOver class in order to manage the behavior depending on what the user
        clicked on.

        Returns
        -------
        None
        """
        if self.isSetGameOver():
            mouse_pos = pygame.mouse.get_pos()  # (x, y) format.
            self.gameOver.mouse_onButtonDown(mouse_pos)
