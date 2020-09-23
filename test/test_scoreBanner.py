from random import randrange

import pygame
import pytest

from controller.controller import Controller
from view.scorebanner import ScoreBanner

controller = Controller()


class TestScoreBanner:

    @pytest.fixture()
    def generateDimensions(self):
        return randrange(20, 500, 20)

    def test__init__(self, generateDimensions):
        snakeInterface = controller.interface
        bannerColor = (0, 0, 0)
        bannerFontColor = (255, 255, 255)
        bannerWidth = generateDimensions
        bannerHeight = bannerWidth
        scoreBanner = ScoreBanner(snakeInterface, controller, bannerColor, bannerFontColor, bannerWidth, bannerHeight)

        assert type(scoreBanner) == ScoreBanner

    def test_getBannerHeight(self):
        bannerHeight = controller.interface.getBannerHeight()
        print(bannerHeight)
        assert type(bannerHeight) == int and bannerHeight == 2 * controller.getBlockSize()

    def test_setScoreBannerRect(self):
        bannerHeight = controller.interface.scoreBanner.getBannerHeight()
        bannerWidth = controller.interface.scoreBanner.bannerWidth
        scoreBannerRect = controller.interface.scoreBanner.setScoreBannerRect(1, 0, bannerWidth, bannerHeight)

        assert type(scoreBannerRect) == pygame.Rect
