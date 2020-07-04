import pygame
import sys

def _init_(width, height):
    # init pygame modules
    pygame.init()
    # config of the interface with the dimensions of the screen
    pygame.display.set_mode((width, height))
    # generate the grid
    #generateGrid(width, height)

#def generateGrid(width, height):



def main():
    width = 500
    while True:
        _init_(width, width)
        # to allow the possibility to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
