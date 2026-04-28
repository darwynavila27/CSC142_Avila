import pygame
import os

class Card:
    def __init__(self, value, suit, image):
        self.value = value
        self.suit = suit

        base_path = os.path.dirname(__file__)
        full_path = os.path.join(base_path, "images_BJG", image)

        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Missing image: {full_path}")

        self.image = pygame.image.load(full_path)
        self.rect = self.image.get_rect()

    def draw(self, window, pos):
        self.rect.topleft = pos
        window.blit(self.image, self.rect)

    def getValue(self):
        return self.value
