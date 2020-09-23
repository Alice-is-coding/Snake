from random import randrange

import pytest

from controller.controller import Controller
from view.gameOver import GameOver

blockSize = 20
width = 500
height = width


class TestGameOver:

    @pytest.fixture()
    def generatePosX(self):
        return randrange(0, width, 1)

    @pytest.fixture()
    def generatePosY(self):
        return randrange(0, height, 1)

    @pytest.fixture()
    def generateSnakeInterface(self):
        controller = Controller()
        return controller.interface

    def test__init__(self):
        controller = Controller()
        snakeInterface = controller.interface
        gameOver = GameOver(controller, snakeInterface)

        assert type(gameOver) == GameOver

    def test_isOnButton_playAgain(self, generatePosX, generatePosY, generateSnakeInterface):
        snakeInterface = generateSnakeInterface
        controller = snakeInterface.controller
        #width = snakeInterface.surface.get_width()
        #height = snakeInterface.surface.get_height()
        posX = generatePosX
        posY = generatePosY
        isOnPlayAgain = False
        snakeInterface.callGameOver(controller.snakeHead['head'], controller.snakeHead['eye1'],
                                    controller.snakeHead['eye2'], controller.score, controller.bestScore)
        gameOver = snakeInterface.gameOver

        if width // 11.4 <= posX <= width // 11.4 + width // 2.87 and height // 1.26 <= posY <= height // 1.26 + height // 11:
            isOnPlayAgain = True
        print("\n x : ", posX, "\n y : ", posY, "\n isOnPlayAgain : ", isOnPlayAgain)
        assert isOnPlayAgain == gameOver.isOnButton_playAgain(posX, posY)

    def test_isOnButton_quit(self, generatePosX, generatePosY, generateSnakeInterface):
        snakeInterface = generateSnakeInterface
        controller = snakeInterface.controller
        posX = generatePosX
        posY = generatePosY
        isOnQuit = False
        snakeInterface.callGameOver(controller.snakeHead['head'], controller.snakeHead['eye1'],
                                    controller.snakeHead['eye2'], controller.score, controller.bestScore)
        gameOver = snakeInterface.gameOver

        if width // 1.758 <= posX <= width // 1.758 + width // 2.87 and height // 1.26 <= posY <= height // 1.26 + height // 11:
            isOnQuit = True
        print('\n x : ', posX, '\n y : ', posY, '\n isOnQuit : ', isOnQuit)
        assert isOnQuit == gameOver.isOnButton_quit(posX, posY)



