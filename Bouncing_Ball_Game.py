# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
WINNING_SCORE = 5

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Click The Ball Game")
 
# 4 - Load assets: image(s).
ballImage = pygame.image.load('images/ball.png')
font = pygame.font.SysFont(None, 36)
bigFont = pygame.font.SysFont(None, 48)

# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height

ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)

xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
 
score = 0
gameOver = False

startTime = pygame.time.get_ticks()
elapsedTime = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program  
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            if ballRect.collidepoint(event.pos):
                score += 1

                if score >= WINNING_SCORE:
                    gameOver = True
                    endTime = pygame.time.get_ticks()
                    elapsedSeconds = (endTime - startTime) / 1000
                else:
                    # Reset ball position
                    ballRect.left = random.randrange(MAX_WIDTH)
                    ballRect.top = random.randrange(MAX_HEIGHT)

                    # Increase speed randomly
                    xSpeed = (abs(xSpeed) + random.randint(1, 5)) * (1 if xSpeed > 0 else -1)
                    ySpeed = (abs(ySpeed) + random.randint(1, 5)) * (1 if ySpeed > 0 else -1)
    # 8 - Do any "per frame" actions
    if not gameOver:
        if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
            xSpeed = -xSpeed  # reverse X direction

        if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
            ySpeed = -ySpeed  # reverse Y direction

    # Update the rectangle of the ball, based on the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    if not gameOver:
        window.blit(ballImage, ballRect)

        scoreText = font.render(f"Score: {score}", True, WHITE)
        window.blit(scoreText, (10, 10))
    else:
        timeText = bigFont.render(
            f"You won in {elapsedSeconds: .2f} seconds!",
            True,
            WHITE
        )
        textRect = timeText.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(timeText, textRect)
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

