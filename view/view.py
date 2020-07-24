import pygame
import sys
import pdb
import controller 


'''
Initialize the game interface. 
'''
def _init_(width, height):
    # Init pygame modules.
    pygame.init()
    # Config of the interface with the dimensions of the screen.
    surface = pygame.display.set_mode((width, height))
    # Generate the grid.
    generateGrid(surface, width, height)


'''
Generate the grid and displays it on game's interface. 
'''
def generateGrid(surface, width, height):
    # Defining the size of a block.
    blockSize = 20
    # Creating the grid thanks to a for loop.
    for x in range(width):
        for y in range(height):
            # Creating a container for a rectangular object.
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            # Drawing the form on the interface.
            pygame.draw.rect(surface, (255,255,255), rect, 1)


'''
The main function.
'''
def main():
    # Defining the size of the width (but also height as we choose to generate a square interface.
    width = 500
    Flag = True
    # Entering an infinite loop (necessary in order to display the game continually as long as we don't ask to quit the game).
    while Flag:
        # Init of the game.
        _init_(width, width)
        # Allowing the possibility to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Updating the interface of the game.
        pygame.display.update()


main()
