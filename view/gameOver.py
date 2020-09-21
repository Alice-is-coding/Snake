import pygame

from view.tools import Tools


class GameOver:
    """
    Allows the creation of a Snake's game over view displayed to the user.
    """

    def __init__(self, controller, snakeInterface):
        """
        Constructor.

        Parameters
        ----------
        controller : controller.controller.Controller
            The controller used for the game.
        snakeInterface : view.view.SnakeInterface
            The main interface of the game.
        """
        self.controller = controller
        self.snakeInterface = snakeInterface
        self.buttons = {}
        self.buttonCounter = 0
        self.texts = ['GAME OVER', 'Score : ', 'Play Again', 'Quit', 'Congrats !', 'New best score : ']
        self.fontType = 'Gameplay.ttf'

    def addButton(self, rect, color, text, lineRect):
        """
        Adds a new button to the buttons dictionary attribute of the class.
        It is necessary to communicate a rect, a color, a text, and a lineRect (aesthetic).

        Parameters
        ----------
        rect : pygame.Rect
            The button (main Rect).
        color : tuple of int
            The main color of the button.
        text : str
            The text of the button.
        lineRect : pygame.Rect
            The Rect used to draw a line around the main Rect of the button.

        Returns
        -------
        None
        """
        self.buttons[self.buttonCounter] = {'rect': rect, 'color': color, 'text': text, 'lineRect': lineRect}
        self.buttonCounter += 1

    def updateButton(self, color, text, textPos, rect):
        """
        Updates the buttons info into the dictionary attribute of the class
        And displays the changes to the user.

        Parameters
        ----------
        color : tuple of int
            The main color of the button.
        text : str
            The text of the button.
        textPos : int or float or tuple of int or tuple of float
            The position of the text (x, y).
        rect : pygame.Rect
            The rect concerned by the changes.

        Returns
        -------
        None
        """
        # Browsing the nested dict.
        for key0, info in self.buttons.items():
            for key1 in info:
                # If the rect corresponds to the current iteration (we are at the right place):
                if info[key1] == rect:
                    # Changing the info with the params.
                    info['color'] = color
                    info['text'] = text
                    # Display the button updated.
                    self.showButton(info['color'], info['rect'], info['lineRect'], info['text'], textPos)

    def isOnButton_playAgain(self, posX, posY):
        """
        Calculates if the cursor is on the button "Play Again" given a posX and posY.

        Parameters
        ----------
        posX : int
            X position of the cursor.
        posY : int
            Y position of the cursor.

        Returns
        -------
        bool
            True if the cursor is on the button "Play Again", False otherwise.
        """
        # Declarations.
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        isOnPlayAgain = False

        if width // 11.4 <= posX <= width // 11.4 + width // 2.87 and height // 1.26 <= posY <= height // 1.26 + height // 11:
            isOnPlayAgain = True
        return isOnPlayAgain

    def isOnButton_quit(self, posX, posY):
        """
        Calculates if the cursor is on the button "Quit" given a posX and posY.

        Parameters
        ----------
        posX : int
            X position of the cursor.
        posY : int
            Y position of the cursor.

        Returns
        -------
        bool
            True if the cursor is on the button "Quit", False otherwise.
        """
        # Declarations.
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        isOnQuit = False

        if width // 1.758 <= posX <= width // 1.758 + width // 2.87 and height // 1.26 <= posY <= height // 1.26 + height // 11:
            isOnQuit = True
        return isOnQuit

    def showGameOver(self, head, eye1, eye2, score, bestScore):
        """
        Displays where the user lost the game, by highlighting the snake's head with a different color, and displays the
        game over interface to the user:
        A message "Game Over" & "Score :" (or "Congrats ! New best score :") and 2 buttons ("Play Again" & "Quit").

        Parameters
        ----------
        head : pygame.Rect
            The snake's head.
        eye1 : pygame.Rect
            The snake's first eye.
        eye2 : pygame.Rect
            The snake' second eye.
        score : int
            The current score.
        bestScore : int, optional
            The new bestScore (if not None)

        Returns
        -------
        None
        """
        # Declarations.
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        isNotAlreadyShown = self.buttons == {}

        # If we didn't already create the "gameOver ihm" -> we do it.
        if isNotAlreadyShown:
            # Showing to the user where the snake actually bite himself by highlighting its head.
            self.snakeInterface.fillSurface((255, 0, 0), head)
            # By filling the head with a color, we need to recreate the eyes.
            self.snakeInterface.drawCircle(eye1.x, eye1.y)
            self.snakeInterface.drawCircle(eye2.x, eye2.y)

            # Showing some info : "Game Over" ; "Score" ; 2 buttons ("Play Again" ; "Quit").
            """*****GAME OVER*****"""
            Tools.createMessage(self.snakeInterface.getSurface(), self.fontType, width // 10, self.texts[0],
                                (251, 244, 5), width // 2, height // 3,
                                (0, 0, 0), True)
            """*****SCORE*****"""
            self.createScoreMessage(width, height, score, bestScore)
            """*****BUTTONS*****"""
            self.createGameOverButtons(width, height)

    def showButton(self, color, rect, lineRect, text, textPos):
        """
        Displays the button on the surface.

        Parameters
        ----------
        color : tuple of int
            The main color of the button.
        rect : pygame.Rect
            The main rect of the button.
        lineRect : pygame.Rect
            The line around the main button rectangle.
        text : pygame.Surface
            The text to be drawn.
        textPos : int or float or tuple of int or tuple of float
            The position of the text.

        Returns
        -------
        None
        """
        # Filling the rect with the color, then displaying the text on the surface at a certain pos.
        self.snakeInterface.fillSurface((255, 255, 255), lineRect)
        self.snakeInterface.fillSurface(color, rect)
        Tools.showTextOnInterface(self.snakeInterface.getSurface(), text, None, textPos)

    def createScoreMessage(self, width, height, score, bestScore=None):
        """
        Creates and displays a message depending on the score.

        Parameters
        ----------
        width : int
            Main surface width.
        height : int
            Main surface height.
        score : int
            The current score.
        bestScore : int, optional
            The new best score.

        Returns
        -------
        None
        """
        # Declarations.
        mainSurface = self.snakeInterface.getSurface()

        # If there's a new best score:
        if bestScore is not None:
            # We congratulate the user.
            Tools.createMessage(mainSurface, self.fontType, int(width // 16.6), self.texts[4], (252, 178, 5),
                                width // 2, height // 1.9, (0, 0, 0), True)
            Tools.createMessage(mainSurface, self.fontType, int(width // 16.6), self.texts[5] + str(score),
                                (252, 178, 5), width // 2, height // 1.7, (0, 0, 0), True)
        else:
            # Otherwise, we only show the current score.
            Tools.createMessage(mainSurface, self.fontType, int(width // 12.5), self.texts[1] + str(score),
                                (252, 178, 5), width // 2, height // 1.8, (0, 0, 0), True)

    def createGameOverButtons(self, width, height):
        """
        Creates the 2 buttons of the game over view : "Play Again" and "Quit".

        Parameters
        ----------
        width : int
            The width of the main surface.
        height : int
            The height of the main surface.

        Returns
        -------
        None
        """
        # Declaration.
        mainSurface = self.snakeInterface.getSurface()

        '''*****BUTTON1*****'''
        # Creating.
        button1_text = Tools.createText(self.fontType, width // 25, self.texts[2], (255, 255, 255))
        button1_rect = pygame.Rect(width // 11.4, height // 1.26, width // 2.87, height // 11)
        button1_lineRect = pygame.Rect(width // 12.5, height // 1.27, width // 2.77, height // 10)
        self.addButton(button1_rect, (0, 0, 0), button1_text, button1_lineRect)
        # Drawing.
        pygame.draw.rect(mainSurface, (255, 255, 255), self.buttons[0]['lineRect'], 6)  # 6
        pygame.draw.rect(mainSurface, self.buttons[0]['color'], self.buttons[0]['rect'])
        self.showButton(self.buttons[0]['color'], self.buttons[0]['rect'], self.buttons[0]['lineRect'], button1_text,
                        (width // 7.58, height // 1.23))
        '''*****BUTTON2*****'''
        # Creating.
        button2_text = Tools.createText(self.fontType, width // 25, self.texts[3], (255, 255, 255))
        button2_rect = pygame.Rect(width // 1.758, height // 1.26, width // 2.87, height // 11)
        button2_lineRect = pygame.Rect(width // 1.78, height // 1.27, width // 2.77, height // 10)
        self.addButton(button2_rect, (0, 0, 0), button2_text, button2_lineRect)
        # Drawing.
        pygame.draw.rect(mainSurface, self.buttons[1]['color'], self.buttons[1]['rect'])
        pygame.draw.rect(mainSurface, (255, 255, 255), self.buttons[1]['lineRect'], 6)
        self.showButton(self.buttons[1]['color'], self.buttons[1]['rect'], self.buttons[1]['lineRect'], button2_text,
                        (width // 1.44, height // 1.23))

    def changeButtonStyle(self, fontType, fontSize, text, textColor, buttonColor, buttonTextPos, rect,
                          smoothEdges=False, background=None):
        """
        Changes the style of the button depending on the args.

        Parameters
        ----------
        fontType : str
            The font type (name of the file (relative path)).
        fontSize : int or float
            The size of the font.
        text : str
            The text drawn on the button.
        textColor : tuple of int
            The color of the text.
        buttonColor : tuple of int
            The main color of the button.
        buttonTextPos : tuple of int or tuple of float
            The position of the text (x, y).
        rect : pygame.Rect
            The button.
        smoothEdges : bool, optional
            If True, the edges of the text will be smooth.
        background : tuple of int, optional
            The background color of the text.

        Returns
        -------
        None
        """
        buttonText = Tools.createText(fontType, fontSize, text, textColor, smoothEdges, background)
        self.updateButton(buttonColor, buttonText, buttonTextPos, rect)

    def mouse_onHover(self, mousePos):
        """
        Event: cursor on hover.
        Creates an aesthetic effect when the user passes the cursor above one of the two game over buttons.

        Parameters
        ----------
        mousePos : (int, int)
            The (x, y) position of the cursor.

        Returns
        -------
        None
        """
        # Declarations.
        # Dimensions.
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        # Colors.
        white = (255, 255, 255)
        black = (0, 0, 0)
        # Buttons redundant info.
        button1_rect = self.buttons[0]['rect']
        button2_rect = self.buttons[1]['rect']
        button1_textPos = (width // 7.58, height // 1.23)
        button2_textPos = (width // 1.44, height // 1.23)
        fontSize = width // 25
        fontType = self.fontType
        isAlreadyShown = self.buttons != {}
        # Cursor (x, y) pos.
        mouse_posX = mousePos[0]
        mouse_posY = mousePos[1]

        if isAlreadyShown:
            # If we are on the "Play Again" button (button0):
            if self.isOnButton_playAgain(mouse_posX, mouse_posY):
                # Changing its style.
                self.changeButtonStyle(fontType, fontSize, self.texts[2], black, white, button1_textPos, button1_rect)
            # If we are on the "Quit" button (button1):
            elif self.isOnButton_quit(mouse_posX, mouse_posY):
                # Changing its style.
                self.changeButtonStyle(fontType, fontSize, self.texts[3], black, white, button2_textPos, button2_rect)
            # If "Play Again" button has a white color background:
            elif self.buttons[0]['color'] == white:
                # Reset its style.
                self.changeButtonStyle(fontType, fontSize, self.texts[2], white, black, button1_textPos, button1_rect)
            # If "Quit" button has a white color background:
            elif self.buttons[1]['color'] == white:
                # Reset its style.
                self.changeButtonStyle(fontType, fontSize, self.texts[3], white, black, button2_textPos, button2_rect)

    def mouse_onButtonDown(self, mouse_pos):
        """
        Event : cursor on clicked.
        Manage the behavior of the game depending where the user clicked.

        Parameters
        ----------
        mouse_pos : (int, int)
            (x, y) position of the cursor.

        Returns
        -------
        None
        """
        # Declarations.
        posX = mouse_pos[0]
        posY = mouse_pos[1]
        isOnButton1 = self.isOnButton_playAgain(posX, posY)
        isOnButton2 = self.isOnButton_quit(posX, posY)

        # If the user clicked on "Play Again":
        if isOnButton1:
            self.controller.resetGame()
        # If the user clicked on "Quit":
        elif isOnButton2:
            self.controller.quit()
