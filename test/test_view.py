from random import randrange

import pygame
import pytest

from controller.controller import Controller
from view.view import SnakeInterface

blockSize = 20


class TestView:

    @pytest.fixture()
    def generateDimensions(self):
        return randrange(20, 500, 20)

    @pytest.fixture()
    def generateSnakeInterface(self, generateDimensions):
        controller = Controller()
        width = generateDimensions
        height = width
        snakeInterface = SnakeInterface(width, height, blockSize, controller)
        print('width : ', width)

        return snakeInterface

    def test__init__(self, generateDimensions):
        controller = Controller()
        width = generateDimensions
        height = width
        snakeInterface = SnakeInterface(width, height, blockSize, controller)

        assert type(snakeInterface) == SnakeInterface

    def test_getSurface(self, generateSnakeInterface):
        snakeInterface = generateSnakeInterface
        surface = snakeInterface.getSurface()
        assert type(surface) == pygame.Surface

    def test_getBannerHeight(self, generateSnakeInterface):
        snakeInterface = generateSnakeInterface
        bannerHeight = snakeInterface.scoreBanner.getBannerHeight()

        assert type(bannerHeight) == int and bannerHeight == 2 * blockSize

    def test_isNotSetGameOver(self, generateSnakeInterface):
        snakeInterface = generateSnakeInterface
        isSetGameOver = snakeInterface.isSetGameOver()

        assert isSetGameOver is False

    @pytest.fixture()
    def generateGameOver(self, generateSnakeInterface):
        snakeInterface = generateSnakeInterface
        controller = snakeInterface.controller
        snakeInterface.callGameOver(controller.snakeHead['head'], controller.snakeHead['eye1'], controller.snakeHead['eye2'], controller.score, controller.bestScore)

        return snakeInterface

    def test_isSetGameOver(self, generateGameOver):
        snakeInterface = generateGameOver
        print(snakeInterface.gameOver)
        isSetGameOver = snakeInterface.isSetGameOver()

        assert isSetGameOver is True
