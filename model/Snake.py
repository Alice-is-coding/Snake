import pygame
import sys
import pdb
from random import randrange
sys.path.append("..\\controller\\")

#pdb.set_trace()


class Snake:
    """
    Constructor.

    :param Controller controller: The current controller.
    :param int speed: The speed of the snake.
    """
    def __init__(self, controller, speed, color):
        # Storing the controller.
        self.controller = controller
        # Storing the color.
        self.color = color
        # Creating the dictionary for the body.
        self.body = {}
        # Used as key to add new body parts to the dict body & used as a counter (score).
        self.countBody = 0
        # Adding the head to the body.
        self.createHead(self.color)
        self.speed = speed


    """
    Body getter.
    
    :return: The body property of the Snake object. 
    """
    def getBody(self):
        return self.body


    """
    Color getter.
    
    :return: The color property of the Snake object. 
    """
    def getColor(self):
        return self.color


    """
    Redirect to the createBody function with True given in parameter to say : we wannna create & store the head of the snake's body.
    
    param tuple(int, int, int) color: The color used to create the head of the snake. 
    """
    def createHead(self, color):
        self.createBody(color, True)


    """
    Create a new body part of the snake and add it to the dict containing all the body parts. 
    
    param tuple(int, int, int) color: The color used to create the body part. 
    param boolean isHead: (Optional) True if it's the head of the snake which is to be created, False otherwise. 
    param int x: (Optional) The pos x of the new body part (randomly generated inside the function if it's the head which is to be created).
    param int y: (Optional) The pos y of the new body part (randomly generated inside the function if it's the head which is to be created).
    """
    def createBody(self, color, isHead = False, x = None, y = None):
        # Saving the block size.
        blockSize = self.controller.getBlockSize()
        width = self.controller.getWidth()
        height = self.controller.getHeight()

        # print("x : ", x, " ; y : ", y)
        #print("isHead = ", isHead)

        # If it is the head to be created & stored :
        if isHead:
            # Generate random position.
            x = randrange(0, width, blockSize)  # to remember : param randrange(begin, max, step) (we go 20 by 20 so that the square will always be visible in a grid' square)
            y = randrange(0, height, blockSize)
            rectObject = pygame.Rect(x + 1, y + 1, blockSize - 2, blockSize - 2)
            # We add the rect for a key called "Head".
            self.body[self.countBody] = rectObject
            # print(self.body)
        else:
            # Else, it's a body part that is to be created.
            # Incrementation of the counter.
            self.countBody += 1
            x = self.body[self.countBody - 1].x - 1 - x
            y = self.body[self.countBody - 1].y - 1 - y
            # Creation of a rect object (the new body part).
            rectObject = pygame.Rect(x + 1, y + 1, blockSize - 2, blockSize - 2)
            # We add the rect to "body" (the key is the counter).
            self.body[self.countBody] = rectObject
            #print(self.body)

        # Call the controller to ask for the creation of a cube visible on the interface given the position, the color and if it's the head of the body or not.
        self.controller.drawRect(rectObject.x, rectObject.y, color, rectObject, isHead)


    """
    Move the snake.
    Each pos x and pos y of each body part of the snake is moved:
    The head of the snake is moved depending on the x and y offsets.
    For all the other body parts : the posx and posy of the body part become posx and posy of the previous body part. 
    
    param int x: The x offset (0, 20, or -20).
    param int y: The y offset (0, 20, or -20).
    param tuple(int, int, int) color: The color of the snake.
    param event.key direction: (Optional) The direction taken by the snake.
    """
    def move(self, x, y, color, direction=None):
        # Declarations.
        width = self.controller.getWidth()
        height = self.controller.getHeight()

        #print("x = ", x, " ; y = ", y)
        # We browse the dict from its end to its beginning.
        for key in range(len(self.body) - 1, -1, -1):
            # Storing the current Rect object in a variable.
            rect = self.body[key]
            # We fill the current rect container with a black color to show the movement of the snake.
            self.controller.fillSurface((0, 0, 0), rect)
            # If the rect is the head of the snake:
            if key == 0:
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
                #print("new head rect.x : ", rect.x)
                #print("new head rect.y : ", rect.y, "\n")
            else:
                # We store the previous Rect object.
                prevRect = self.body[key - 1]
                '''print("dict : ", self.body,"\n")
                print("rect[",key,"] : ", rect)
                print("rect.x : ", rect.x)
                print("rect.y : ", rect.y,"\n")
                print("prevRect[",key - 1,"] : ", prevRect)
                print("prevRect.x : ", prevRect.x)
                print("prevRect.y : ", prevRect.y,"\n")'''
                # The current x pos of the rect become the x pos of the previous rect.
                rect.x = prevRect.x
                # The current y pos of the rect become the y pos of the previous rect.
                rect.y = prevRect.y
                '''print("new rect.x : ", rect.x)
                print("new rect.y : ", rect.y,"\n")'''
        # We ask the controller to move all the rects.
        self.drawRects(self.body, color, direction)


    """
    Browse the dict passed as an arg and for each item (rect objects), the controller ask the view to draw the rect object according to its pos x and pos y.
    
    param Dictionary<Rect> dict: A dictionary containing all the rect objects of the snake.
    param tuple(int, int, int) color: The color of the snake. 
    param event.key direction: The direction taken by the snake. 
    """
    def drawRects(self, dict, color, direction):
        # Browsing the dictionary.
        for key, value in dict.items():
            # Storing the current item.
            rect = dict[key]
            # Calling the controller to draw the rect on the surface (by calling the view).
            self.controller.drawRect(rect.x, rect.y, color, rect, key == 0, direction)



