import pygame
from view.tools import Tools


class TestTools:

    def test_createText(self):
        fontType = 'Gameplay.ttf'
        fontSize = 20
        text = 'test'
        color = (0, 0, 255)
        theText = Tools.createText(fontType, fontSize, text, color)

        assert type(theText) == pygame.Surface


