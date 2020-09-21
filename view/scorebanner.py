import pygame

from view.tools import Tools


class ScoreBanner:
    """
    Draw the score banner on the main surface and update it when required.
    """

    def __init__(self, snakeInterface, controller, bannerColor, bannerFontColor, bannerWidth, bannerHeight):
        """
        Initialize the score banner.

        Parameters
        ----------
        snakeInterface : view.view.SnakeInterface
            The snake interface.
        controller : controller.controller.Controller
            The controller used for the game.
        bannerColor : tuple of int
            The color used to fill the banner.
        bannerFontColor : tuple of int
            The color used for the font.
        bannerWidth : int
            The width of the banner.
        bannerHeight : int
            The height of the banner.
        """
        self.snakeInterface = snakeInterface
        self.controller = controller
        self.bannerColor = bannerColor
        self.bannerFontColor = bannerFontColor
        self.bannerWidth = bannerWidth
        self.bannerHeight = bannerHeight
        self.scoreBannerRect = self.setScoreBannerRect(1, 0, self.bannerWidth, self.bannerHeight)

        self.createScoreBanner(self.scoreBannerRect)

    def getBannerHeight(self):
        """
        Banner height getter.

        Returns
        -------
        int
            The height of the banner.
        """
        return int(self.bannerHeight)

    def setScoreBannerRect(self, posX, posY, width, height):
        """
        Create and return the rectangle for the banner.

        Parameters
        ----------
        posX : int
            Position x (abscissa).
        posY : int
            Position y (ordinate).
        width : int
            The width of the future Rect.
        height : int
            The height of the future Rect.

        Returns
        -------
        pygame.Rect
            The banner rectangle.
        """
        return pygame.Rect(posX, posY, width, height)

    def createScoreBanner(self, bannerRect):
        """
        Draws the banner, and displays the scores (score & best score).

        Parameters
        ----------
        bannerRect : pygame.Rect
            The banner rectangle.

        Returns
        -------
        None
        """
        # Declarations.
        bestScore = self.controller.getBestScore()
        mainWidth = self.snakeInterface.width

        # Drawing the banner, and the 2 messages (Score and Best Score).
        self.snakeInterface.drawRect(self.bannerColor, bannerRect)
        Tools.createMessage(self.snakeInterface.getSurface(), 'Gameplay.ttf', mainWidth // 41, 'Score : 0',
                            self.bannerFontColor, self.bannerWidth // 9, self.bannerHeight // 2, None, True)
        Tools.createMessage(self.snakeInterface.getSurface(), 'Gameplay.ttf', mainWidth // 41,
                            'Best Score : ' + str(bestScore), self.bannerFontColor, self.bannerWidth // 1.18,
                            self.bannerHeight // 2, None, True)

    def updateScoreBanner(self, score):
        """
        Updates the score displayed on the banner.

        Parameters
        ----------
        score : int
            The current score.

        Returns
        -------
        None
        """
        # Declarations.
        mainWidth = self.controller.getWidth()
        blockSize = self.controller.getBlockSize()

        # We fill half of the banner (left side) with the banner color, and we draw the score back.
        self.snakeInterface.fillSurface(self.bannerColor, (1, 0, mainWidth // 2, blockSize * 2))
        Tools.createMessage(self.snakeInterface.getSurface(), 'Gameplay.ttf', mainWidth // 41,
                            'Score : ' + str(score), self.bannerFontColor, self.bannerWidth // 9,
                            self.bannerHeight // 2, None, True)
