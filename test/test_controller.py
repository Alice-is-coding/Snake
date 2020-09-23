from random import randrange
from controller import controller
from controller.controller import Controller
from view.gameOver import GameOver
import pygame
import pytest

controller = Controller()
blockSize = controller.getBlockSize()
width = controller.getWidth()
height = controller.getHeight()
snakeBody = controller.snakeBody
snakeHead = controller.snakeHead['head']


class TestController:

    def test__init__(self):
        controller1 = Controller()
        assert type(controller1) == Controller

    def test_getController(self):
        assert controller.getController() == controller

    def test_getBlockSize_type(self):
        assert type(blockSize) == int

    def test_getBlockSize_range(self):
        assert width > blockSize >= 0 and blockSize < height

    def test_getBlockSize_value(self):
        assert width % blockSize == height % blockSize == 0, 'width != 0 (mod blockSize) or height != 0 (mod blockSize)'

    def test_getWidth(self):
        assert type(width) == int and width >= 0, 'width is not type int or is < 0'

    def test_getHeight(self):
        assert type(height) == int and height >= 0, 'height is not type int or is < 0'

    def test_getScore(self):
        score = controller.getScore()
        assert type(score) == int and score >= 0, 'score is not type int or is < 0'

    def test_getBestScore(self):
        bestScore = controller.getBestScore()
        assert type(bestScore) == int and bestScore >= 0, 'bestScore is not type int or is < 0'

    def test_getNewDirection(self):
        controller.newDirection = pygame.K_DOWN
        assert controller.getNewDirection() == pygame.K_DOWN

    def test_getDirection(self):
        controller.direction = pygame.K_UP
        assert controller.getDirection() == pygame.K_UP

    def test_getBannerHeight(self):
        bannerHeight = controller.getBannerHeight()
        assert type(bannerHeight) == int and bannerHeight == 2 * blockSize, 'the bannerHeight isn\'t type int or '

    @pytest.fixture()
    def generateBestScore(self):
        return randrange(1, 500, 1)

    def test_setBestScore(self, generateBestScore):
        bestScore = generateBestScore
        controller.setBestScore(bestScore)
        assert controller.bestScore == bestScore

    @pytest.fixture()
    def generateSnack(self):
        controller.snack.setPos()

    @pytest.fixture()
    def generateSnake(self):
        x = 20
        y = 0
        snakeColor = controller.snake.getColor()

        for k in range(x, 51):
            controller.snake.createBody(snakeColor, False, x, y)

    def test_compareSnackAndSnakePos(self, generateSnake, generateSnack):

        # Declaration.
        snackPos_x = controller.snack.getPos_x()
        snackPos_y = controller.snack.getPos_y()
        isAtTheSamePos = False

        # Browsing all the items of the snakeBody.
        for key, value in snakeBody.items():
            # If an item is at the same place of the snack:
            if snakeBody[key].x - 1 == snackPos_x and snakeBody[key].y - 1 == snackPos_y:
                print('is on a body part')
                # We change the boolean var to true.
                isAtTheSamePos = True
        if snakeHead.x - 1 == snackPos_x and snakeHead.y - 1 == snackPos_y:
            print('the snake head a the same pos as the snack')
            isAtTheSamePos = True
        assert controller.compareSnackAndSnakePos() == isAtTheSamePos

    def test_compareSnakeHeadAndBodyPos(self, generateSnake):
        # Declarations.
        k = 1  # Body parts counter.
        biteHimself = False

        # While the snake didn't bite himself and we didn't reach the end of his body.
        while not biteHimself and k < len(snakeBody):
            # Storing the current body part.
            rect = snakeBody[k]
            # If the head is at the same position of the body part (rect)
            if rect.contains(snakeHead):
                biteHimself = True
            else:
                k += 1
        assert controller.compareSnakeHeadAndBodyPos() == biteHimself

    @pytest.fixture()
    def generateInt(self):
        return randrange(1, 500, 1)

    def test_isNewBestScore(self, generateInt):
        # Declarations.
        newScore = generateInt
        bestScore = controller.bestScore
        isNewBestScore = False

        print('\n newScore : ', newScore, '\n bestScore : ', bestScore)

        if newScore > bestScore:
            isNewBestScore = True
        print(' isNewBestScore : ', isNewBestScore)
        assert controller.isNewBestScore(newScore) == isNewBestScore

    def test_callGameOver(self, generateInt):
        controller.interface.callGameOver(controller.snakeHead['head'], controller.snakeHead['eye1'],
                                          controller.snakeHead['eye2'], controller.score, generateInt)

        assert type(controller.interface.gameOver) == GameOver
