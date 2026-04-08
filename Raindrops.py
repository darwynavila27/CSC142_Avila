import pygame
import random
import time

class Raindrop:
    __slots__ = ("x", "y", "radius")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1

    def update(self):
        self.radius += 1

    def draw(self, window):
        pygame.draw.circle(window, (0, 0, 255), (self.x, self.y), self.radius, 1)


class RaindropsManager:
    RAIN_RATE = 0.5
    MAX_RADIUS = 50

    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Raindrops")

        self.clock = pygame.time.Clock()
        self.running = True

        self.raindrops = []
        self.last_drop_time = time.time()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        current_time = time.time()

        if current_time - self.last_drop_time >= RaindropsManager.RAIN_RATE:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.raindrops.append(Raindrop(x, y))
            self.last_drop_time = current_time

        for drop in self.raindrops:
            drop.update()

        new_list = []
        for drop in self.raindrops:
            if drop.radius <= RaindropsManager.MAX_RADIUS:
                new_list.append(drop)

        self.raindrops = new_list

    def draw(self):
        self.window.fill((0, 0, 0))

        for drop in self.raindrops:
            drop.draw(self.window)

        pygame.display.flip()


if __name__ == "__main__":
    manager = RaindropsManager()
    manager.run()
