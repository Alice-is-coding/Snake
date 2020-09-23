import pygame


class Tools:
    """
    Full of static methods useful for the game in different classes.
    """
    @staticmethod
    def createMessage(mainSurface, fontType, fontSize, message, color, posX, posY, background=None, center=False,
                      smoothEdges=False, destination=None):
        """
        Creates a message and displays it.

        Parameters
        ----------
        mainSurface : pygame.Surface
            The main surface used to create the message.
        fontType : str
            The font type (filename)(relative path).
        fontSize : int
            The font size.
        message : str
            The message to be created and displayed.
        color : tuple of int
            The color of the message.
        posX : int or float
            The position x of the message.
        posY : int or float
            The position y of the message.
        background : tuple of int, optional
            The background color of the message.
        center : bool
            If True: the Rect object should be drawn at the center of the surface given its posX and posY.
        smoothEdges : bool, optional
            If True, the edges of the message will be visually smooth.
        destination : pygame.Surface, optional
            The surface on which the message should be drawn.

        Returns
        -------
        None
        """
        message_text = Tools.createText(fontType, fontSize, message, color, smoothEdges, background)
        message_rect = message_text.get_rect()
        Tools.showTextOnInterface(mainSurface, message_text, message_rect, destination, posX, posY, center)

    @staticmethod
    def createText(fontType, fontSize, text, color, smoothEdges=False, background=None):
        """
        Creates a Surface with some text given in param.

        Parameters
        ----------
        fontType : str
            The filename of the font chosen.
        fontSize : int
            The font size.
        text : str
            The text to be rendered according to a font.
        color : tuple of int
            The text color.
        smoothEdges : bool
            (Optional) If True, the text will be displayed with smooth edges.
        background : tuple of int
            (Optional) Background color.

        Returns
        -------
        pygame.Surface
            The new Surface created with the specified text rendered on it.
        """
        font = pygame.font.Font(fontType, fontSize)
        theText = font.render(text, smoothEdges, color, background)

        return theText

    @staticmethod
    def showTextOnInterface(mainSurface, text, rect=None, destination=None, posX=None, posY=None, center=False):
        """
        Displays some text on the main interface.

        Parameters
        ----------
        mainSurface : pygame.Surface
            The main surface used to show the text on.
        text : pygame.Surface
            The text to be displayed on the main surface.
        rect : pygame.Surface, optional
            The surface containing the text.
        destination : pygame.Surface, optional
            The surface on which the text is to be drawn.
        posX : int, optional
            The pos x of the Rect object.
        posY : int, optional
            The pos y of the Rect object.
        center : bool, optional
            If True: the Rect object should be drawn at the center of the surface given its posX and posY.

        Returns
        -------
        None
        """
        if center is True and rect is not None and posX is not None and posY is not None:
            rect.center = (int(posX), int(posY))
        if destination is not None:
            mainSurface.blit(text, destination)
        else:
            mainSurface.blit(text, rect)
