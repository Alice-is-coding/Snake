import pygame
import pytest
from controller.controller import Controller
from model.Snake import Snake

controller = Controller()

controller = Controller()


class TestSnake:

    def test__init__(self):
        color = (0, 255, 0)
        snake = Snake(controller, color)

        assert type(snake) == Snake

    def test_addBodyPart(self):
        x = 20
        y = 0
        k = 0
        blockSize = 20
        snake = controller.snake
        rect = pygame.Rect(x + 1, y + 1, blockSize - 2, blockSize - 2)
        while k <= 15:
            snake.addBodyPart(k, rect)
            k += 1

        snakeBody = snake.getBody()
        assert len(snakeBody) == k and type(snakeBody) == dict and type(snakeBody[k - 1]) == pygame.Rect, \
            'Some rects haven\'t been added or snakeBody isn\'t a dict or an object of the dict isn\'t a Rect object'

    def test_addHead(self):
        snakeHead = controller.snake.getHead()

        print(snakeHead)
        print(len(snakeHead))

        assert len(snakeHead) == 3, 'Misses à head part (head, eye1, or eye2), or there\'s more than 1 head...'
        for key, value in snakeHead.items():
            assert type(key) == str and type(value) == pygame.Rect, 'The key isn\'t an str or the value isn\'t a Rect'

    def test_getSnake(self):
        snake = controller.snake.getSnake()

        assert type(snake) == Snake

    def test_getHead(self):
        snakeHead = controller.snake.getHead()

        assert type(snakeHead) == dict and len(snakeHead) == 3

    def test_getBody(self):
        snakeBody = controller.snake.getBody()

        assert type(snakeBody) == dict

    def test_getColor(self):
        snakeColor = controller.snake.getColor()

        assert type(snakeColor) == tuple

    def test_getScore(self):
        snakeBody = controller.snake.getBody()
        score = controller.snake.getScore()

        assert type(score) == int and score == len(snakeBody)

    @pytest.fixture()
    def getHead(self):
        return controller.snake.getHead()

    @pytest.fixture()
    def getSurface(self):
        return controller.interface.getSurface()

    @pytest.fixture()
    def getHeight(self, getSurface):
        return getSurface.get_height()

    @pytest.fixture()
    def getWidth(self, getSurface):
        return getSurface.get_width()

    @pytest.fixture()
    def getBannerHeight(self):
        return controller.interface.getBannerHeight()

    @pytest.fixture()
    def getBlockSize(self):
        return controller.getBlockSize()

    def test_moveHead_returnToLeft(self, getHead, getWidth):
        # Changing the pos of the head.
        snakeHead = getHead
        width = getWidth
        snakeHead['head'].x = width
        initialSnakeHeadX = snakeHead['head'].x
        print(snakeHead['head'].x)

        controller.snake.moveHead(20, 0, pygame.K_RIGHT)
        print(snakeHead['head'])

        assert snakeHead['head'].x == (initialSnakeHeadX + 20) - width, \
            'Thing to be understood : in the function tested, we test if the rect.x + x > mainWidth (which means that ' \
            'we actually add x to rect.x). So if it is the case (rect.x + x > width) -> we move back by (- width).'

    def test_moveHead_returnToRight(self, getHead, getWidth):
        # Changing the pos of the head.
        snakeHead = getHead
        width = getWidth
        snakeHead['head'].x = 0
        initialSnakeHeadX = snakeHead['head'].x
        print(snakeHead['head'].x)

        controller.snake.moveHead(-20, 0, pygame.K_LEFT)
        print(snakeHead['head'])

        assert snakeHead['head'].x == (initialSnakeHeadX - 20) + width, \
            'Thing to be understood : in the function tested, we test if the rect.x + x <= 0 ' \
            '(which means that we actually added x to rect.x (here -20). So if it is the case (rect.x + x <= 0) ' \
            '-> we move forward by width.'

    def test_moveHead_returnToTop(self, getHead, getHeight, getBannerHeight):
        # Changing the pos of the head.
        snakeHead = getHead
        height = getHeight
        bannerHeight = getBannerHeight
        snakeHead['head'].y = height
        initialSnakeHeadY = snakeHead['head'].y
        print('snakeheadY init = : ', initialSnakeHeadY)

        controller.snake.moveHead(0, 20, pygame.K_DOWN)
        print('new snakeHeadY = ', snakeHead['head'].y)
        assert snakeHead['head'].y == (initialSnakeHeadY + 20) - height + bannerHeight, \
            'Thing to be understood : in the function tested, we test if the rect.y + y > height ' \
            '(which means we actually added y to rect.y (here 20). So if it is the case -> we move back by (-height).'

    def test_moveHead_returnToBottom(self, getHead, getHeight, getBannerHeight):
        # Changing the pos of the head.
        snakeHead = getHead
        height = getHeight
        bannerHeight = getBannerHeight
        snakeHead['head'].y = bannerHeight
        initialSnakeHeadY = snakeHead['head'].y
        print('initialSnakeHeadY : ', initialSnakeHeadY)

        controller.snake.moveHead(0, -20, pygame.K_UP)
        print('new snakeHeadY : ', snakeHead['head'].y)

        assert snakeHead['head'].y == (initialSnakeHeadY - 20) + height - bannerHeight, \
            'Thing to be understood : in the function tested, we test if the rect.y + y <= bannerHeight ' \
            '(which means we actually added y to rect.y (here -20). So if it is the case -> we moveForward ' \
            'to the lower edge.'

    def test_moveHead_continueMoving_elseCase(self, getHead, getWidth, getHeight, getBlockSize):
        blockSize = getBlockSize
        snakeHead = getHead
        height = getHeight
        width = getWidth
        snakeHead['head'].x = width - (4 * blockSize)
        snakeHead['head'].y = height - (4 * blockSize)
        initSnakeHeadX = snakeHead['head'].x
        initSnakeHeadY = snakeHead['head'].y
        print('init head pos X : ', initSnakeHeadX)
        print('init head pos Y : ', initSnakeHeadY)

        controller.snake.moveHead(20, 0, pygame.K_RIGHT)
        assert snakeHead['head'].x == initSnakeHeadX + 20
        initSnakeHeadX = snakeHead['head'].x

        controller.snake.moveHead(-20, 0, pygame.K_LEFT)
        assert snakeHead['head'].x == initSnakeHeadX - 20

        controller.snake.moveHead(0, 20, pygame.K_DOWN)
        assert snakeHead['head'].y == initSnakeHeadY + 20
        initSnakeHeadY = snakeHead['head'].y

        controller.snake.moveHead(0, -20, pygame.K_UP)
        assert snakeHead['head'].y == initSnakeHeadY - 20
