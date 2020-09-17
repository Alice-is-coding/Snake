import pygame
import sys
from random import randrange

sys.path.append("..\\controller\\")


class Snake:
    """
    Creates a snake (his head and each body part) and allows it to move.
    """

    def __init__(self, controller, speed, color):
        """
        Constructor.

        Parameters
        ----------
        controller : controller.controller.Controller
            The controller used for the game.
        speed : int
            The speed chosen.
        color : tuple of int
            The color of the snake.
        """
        self.controller = controller
        self.color = color
        self.speed = speed
        # Creating the dictionary for the body and head.
        self.body = {}
        self.head = {}
        # Used as key to add new body parts to the dict body and the head & used as a counter (score).
        self.countBody = 0
        # Adding the head to the body.
        self.createHead(self.color)

    def addBodyPart(self, key, value):
        """
        Add a new body part to the body dict attribute.

        Parameters
        ----------
        key : int
            The dict index.
        value : pygame.Rect
            The new body part to be added.

        Returns
        -------
        None
        """
        self.body[key] = value

    def addHead(self, head, eye1, eye2):
        """
        Add the head and the eyes to the head dict attribute.

        Parameters
        ----------
        head : pygame.Rect
            The snake's head.
        eye1 : pygame.Rect
            The snake's first eye.
        eye2 : pygame.Rect
            The snake' second eye.

        Returns
        -------
        None
        """
        self.head['head'] = head
        self.head['eye1'] = eye1
        self.head['eye2'] = eye2

    def getSnake(self):
        """
        Snake getter.

        Returns
        -------
        Snake
            The Snake object.
        """
        return self

    def getHead(self):
        """
        Head dict attribute getter.

        Returns
        -------
        dict
            The head dict attribute containing the head and the eyes of the Snake object.
        """
        return self.head

    def getBody(self):
        """
        Body getter.

        Returns
        -------
        dict
            The body parts (attribute) of the Snake.
        """
        return self.body

    def getColor(self):
        """
        Color getter.

        Returns
        -------
        tuple of int
            The color attribute of the Snake object.
        """
        return self.color

    def getSpeed(self):
        """
        Speed getter.

        Returns
        -------
        int
            The speed attribute of the Snake object.
        """
        return self.speed

    def getScore(self):
        """
        Score getter.

        Returns
        -------
        int
            The score of the user (calculated according to the number of body parts).
        """
        return len(self.body)

    def createHead(self, color):
        """
        Redirect to the createBody function with True passed in param to say :
        we want to create & store the snake's head.

        Parameters
        ----------
        color : tuple of int
            The color to be drawn.

        Returns
        -------
        None
        """
        self.createBody(color, True)

    def createBody(self, color, isHead=False, x=None, y=None):
        """
        Create a new body part for the snake and add it to the body attribute (dict) containing all the body parts.

        Parameters
        ----------
        color : int or tuple of int
            The color used to create the body part.
        isHead : bool, optional
            True if the head of the snake is to be created, False otherwise.
        x : int, optional
            The pos x of the new body part (randomly generated inside the function if it's the head which is
            to be created).
        y : int, optional
            The pos y of the new body part (randomly generated inside the function if it's the head which is
            tp be created).

        Returns
        -------
        None
        """
        # Saving the dimensions.
        blockSize = self.controller.getBlockSize()
        width = self.controller.getWidth()
        height = self.controller.getHeight()
        # rectObject = None

        # If it is the head to be created & stored :
        if isHead:
            # Generate random position.
            x = randrange(0, width,
                          blockSize)
            # NB: param randrange(begin, max, step)
            # (we go blockSize by blockSize so that the square will always be visible in a grid' square).
            y = randrange(0, height, blockSize)
            # Creating the head and the eyes, then add it to the head dict.
            rectObject = pygame.Rect(x + 1, y + 1, blockSize - 2, blockSize - 2)
            eye1 = pygame.Rect(int(x + (blockSize // 1.4)), int(y + (blockSize // 2)), blockSize // 10, blockSize // 10)
            eye2 = pygame.Rect(int(x + (blockSize // 3)), int(y + (blockSize // 2)), blockSize // 10, blockSize // 10)
            self.addHead(rectObject, eye1, eye2)
        else:
            if self.countBody == 0:
                # Calculating an x and a y so that the new body par (Rect) will be drawn behind the head.
                x = self.head['head'].x - 1 - x
                y = self.head['head'].y - 1 - y
            else:
                # Else, it's a body part that is to be created -> the new body part will be drawn behind the last one.
                x = self.body[self.countBody - 1].x - 1 - x
                y = self.body[self.countBody - 1].y - 1 - y
            rectObject = pygame.Rect(x + 1, y + 1, blockSize - 2, blockSize - 2)
            # We add the Rect to the body.
            self.addBodyPart(self.countBody, rectObject)
            self.countBody += 1

        # Call the controller to ask for the creation of a square visible on the interface given the position,
        # the color and if it's the head of the body or not.
        self.drawBody(color, rectObject, isHead)

    def drawBody(self, color, rect, isHead=False):
        """
        Draw the body part (or the head) passed in arg.

        Parameters
        ----------
        color : tuple of int
            Color to be drawn.
        rect : pygame.Rect
            The body part (or the head) which is to be drawn.
        isHead : bool, optional
            If True, the Rect object is the head, and the head is to be drawn.

        Returns
        -------
        None
        """
        if isHead:
            # Browsing the head dict attribute.
            for key, value in self.head.items():
                if key != 'head':
                    eye = self.head[key]
                    self.controller.drawCircle(eye.x, eye.y, (0, 0, 0))
        else:
            self.controller.drawRect(color, rect)

    def move(self, x, y, color, direction=None):
        """
        Moves the snake.
        Each posX and posY of each body part of the snake is moved:
        The head of the snake is moved depending on the x and y offsets.
        For all the other body parts: the posX and posY of the body part become posX and posY of the previous body part.

        Parameters
        ----------
        x : int
            The x offset (0, blockSize, or - blockSize).
        y : int
            The y offset (0, blockSize, or - blockSize).
        color : tuple of int
            The color of the snake.
        direction : pygame.key, optional
            The direction taken by the snake.

        Returns
        -------
        None
        """
        self.moveBody()
        self.moveHead(x, y, direction)
        # We ask the controller to move all the rects.
        self.drawRects(self.body, self.head, color)

    def moveHead(self, x, y, direction):
        """
        Moves the head of the snake according to the offsets x and y.
        Then calls the moveEyes to move the eyes.
        Parameters
        ----------
        x : int
            Offset x.
        y : int
            Offset y.
        direction : pygame.key
            The direction taken by the snake.

        Returns
        -------
        None
        """
        # Declarations.
        width = self.controller.getWidth()
        height = self.controller.getHeight()

        for key, value in self.head.items():
            if key == 'head':
                rect = self.head[key]
                self.controller.fillSurface((0, 0, 0), rect)
                # Testing the next position of the head to manage the edges of the surface.
                if rect.x + x > width:
                    # We're reaching the right edge (we return to the left)
                    rect.move_ip(- width, y)
                elif rect.x + x <= 0:
                    # We're reaching the left edge (we return to the right)
                    rect.move_ip(width, y)
                if rect.y + y > height:
                    # We're reaching the lower edge (we return to the top)
                    rect.move_ip(x, - height + y)
                elif rect.y + y <= 0:
                    # We're reaching the upper edge (we return to the lower edge)
                    rect.move_ip(x, height + y)
                else:
                    # We continue moving as expected
                    rect.move_ip(x, y)
        self.moveEyes(self.head['head'].x, self.head['head'].y, direction)

    def moveEyes(self, x, y, direction):
        """
        Moves the eyes given an x and y offsets, and a direction.

        Parameters
        ----------
        x : int
            Offset x.
        y : int
            Offset y.
        direction : pygame.key
            The direction taken by the snake.

        Returns
        -------

        """
        # Declarations.
        eye1 = self.head['eye1']
        eye2 = self.head['eye2']
        blockSize = self.controller.getBlockSize()

        if direction == pygame.K_UP:
            eye1.x = int(x + (blockSize // 5))
            eye1.y = int(y + (blockSize // 5))
            eye2.x = int(x + (blockSize // 1.5))
            eye2.y = int(y + (blockSize // 5))
        elif direction == pygame.K_DOWN:
            eye1.x = int(x + (blockSize // 5))
            eye1.y = int(y + (blockSize // 1.4))
            eye2.x = int(x + (blockSize // 1.5))
            eye2.y = int(y + (blockSize // 1.4))
        elif direction == pygame.K_LEFT:
            eye1.x = int(x + (blockSize // 6))
            eye1.y = int(y + (blockSize // 4))
            eye2.x = int(x + (blockSize // 6))
            eye2.y = int(y + (blockSize // 1.5))
        elif direction == pygame.K_RIGHT:
            eye1.x = int(x + (blockSize // 1.4))
            eye1.y = int(y + (blockSize // 4))
            eye2.x = int(x + (blockSize // 1.4))
            eye2.y = int(y + (blockSize // 1.5))

    def moveBody(self):
        """
        Moves the body of the snake.
        For all the body parts: the posX and posY of the body part become posX and posY of the previous body part.

        Returns
        -------
        None
        """
        # Browse the dict from its end to its beginning.
        for key in range(len(self.body) - 1, -1, -1):
            rect = self.body[key]
            # Fill the current rect container with a black color to show the movement of the snake.
            self.controller.fillSurface((0, 0, 0), rect)
            # If the rect is the head of the snake:
            if key == 0:
                head = self.head['head']
                rect.x = head.x
                rect.y = head.y
            else:
                # We store the previous body part.
                prevRect = self.body[key - 1]
                # The current x pos and y pos of the rect become the x pos and y pos of the previous rect.
                rect.x = prevRect.x
                rect.y = prevRect.y

    def drawRects(self, body, head, color):
        """
        Browse the dicts passed in param: for each item (Rect objects), the controller asks the view to draw
        the Rect object according to its posX and posY.

        Parameters
        ----------
        body : dict
            A dictionary containing all the body parts (Rect objects) of the snake.
        head : dict
            A dictionary containing the different parts of the snake's head (head, eyes).
        color : tuple of int
            The color of the snake.

        Returns
        -------
        None
        """
        # Browsing the dicts.
        for key, value in head.items():
            # Asking the controller to draw each part of the head (head, eyes).
            rect = head[key]
            if key == 'head':
                self.controller.drawRect(color, rect)
            else:
                self.controller.drawCircle(rect.x, rect.y, (0, 0, 0))
        for key, value in body.items():
            # Asking the controller to draw each body parts.
            rect = body[key]
            self.controller.drawRect(color, rect)
