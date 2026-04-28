import pygame
import pygwidgets
import sys
import random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Catch the Box Deluxe')

WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)

clock = pygame.time.Clock()
FPS = 60

GAME_DURATION = 30000

STATE_START = 'start'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game_over'

class MovingBox:
    def __init__(self, speed_multiplier=1):
        self.size = 50
        self.x = random.randint(0, WINDOW_WIDTH - self.size)
        self.y = random.randint(0, WINDOW_HEIGHT - self.size)
        base_speed = random.choice([3, 4, 5])
        self.speed_x = base_speed * random.choice([-1, 1]) * speed_multiplier
        self.speed_y = base_speed * random.choice([-1, 1]) * speed_multiplier

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= WINDOW_WIDTH - self.size:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= WINDOW_HEIGHT - self.size:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.rect(window, BLUE, (self.x, self.y, self.size, self.size))

    def is_clicked(self, pos):
        mouse_x, mouse_y = pos
        return self.x <= mouse_x <= self.x + self.size and self.y <= mouse_y <= self.y + self.size

def reset_game():
    return {
        'score': 0,
        'start_time': pygame.time.get_ticks(),
        'box': MovingBox(),
        'speed_multiplier': 1
    }

scoreDisplay = pygwidgets.DisplayText(window, (10, 10), 'Score: 0', fontSize=24, textColor=BLACK)
timeDisplay = pygwidgets.DisplayText(window, (450, 10), 'Time: 30', fontSize=24, textColor=BLACK)
centerMessage = pygwidgets.DisplayText(window, (120, 160), '', fontSize=36, textColor=RED)
instructionText = pygwidgets.DisplayText(window, (120, 220), 'Click to start', fontSize=24, textColor=BLACK)

game_state = STATE_START
game_data = reset_game()

# Main loop
while True:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == STATE_START:
                game_state = STATE_PLAYING
                game_data = reset_game()

            elif game_state == STATE_PLAYING:
                if game_data['box'].is_clicked(pygame.mouse.get_pos()):
                    game_data['score'] += 1
                    game_data['speed_multiplier'] += 0.2
                    game_data['box'] = MovingBox(game_data['speed_multiplier'])

            elif game_state == STATE_GAME_OVER:
                game_state = STATE_START

    if game_state == STATE_START:
        centerMessage.setValue('Catch the Box!')
        instructionText.setValue('Click to start')
        centerMessage.draw()
        instructionText.draw()

    elif game_state == STATE_PLAYING:
        current_time = pygame.time.get_ticks()
        elapsed = current_time - game_data['start_time']
        remaining = max(0, (GAME_DURATION - elapsed) // 1000)

        scoreDisplay.setValue(f"Score: {game_data['score']}")
        timeDisplay.setValue(f"Time: {remaining}")

        time_ratio = max(0, (GAME_DURATION - elapsed) / GAME_DURATION)
        pygame.draw.rect(window, GREEN, (0, WINDOW_HEIGHT - 10, WINDOW_WIDTH * time_ratio, 10))

        if elapsed < GAME_DURATION:
            game_data['box'].move()
            game_data['box'].draw()
        else:
            game_state = STATE_GAME_OVER

        scoreDisplay.draw()
        timeDisplay.draw()

    elif game_state == STATE_GAME_OVER:
        centerMessage.setValue(f"Final Score: {game_data['score']}")
        instructionText.setValue('Click to restart')
        centerMessage.draw()
        instructionText.draw()

    pygame.display.update()
    clock.tick(FPS)
