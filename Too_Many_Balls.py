import pygame
import random
from Ball import Ball

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 60
GAME_LENGTH_SECONDS = 15

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Click the Balls Game")
clock = pygame.time.Clock()

# Font setup
pygame.font.init()
font = pygame.font.SysFont("arial", 24)

# Game variables
ballList = []
score = 0
startTicks = pygame.time.get_ticks()
lastSecond = 0
gameOver = False

def createBall():
        return Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# Main Loop
running = True
while running:
    clock.tick(FRAMES_PER_SECOND)

    currentTicks = pygame.time.get_ticks()
    elapsedSeconds = (currentTicks - startTicks) // 1000

    # Spawn new ball every second
    if elapsedSeconds > lastSecond and not gameOver:
        ballList.append(createBall())
        lastSecond = elapsedSeconds

    # End game after 15 seconds
    if elapsedSeconds >= GAME_LENGTH_SECONDS and not gameOver:
        gameOver = True
        ballList.clear()

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mousePos = event.pos
            for ball in ballList[:]:
                if ball.wasClicked(mousePos):
                    score += 1
                    ballList.remove(ball)

    # Update balls
    if not gameOver:
        for ball in ballList:
            ball.update()

    # Draw everything
    window.fill((0, 0, 0))

    for ball in ballList:
        ball.draw()

    # Draw score and time
    scoreText = font.render(f"Score: {score}", True, (255, 255, 255))
    timeText = font.render(f"Time: {elapsedSeconds}", True, (255, 255, 255))

    window.blit(scoreText, (10, 10))
    window.blit(timeText, (10, 40))

    # Game over display
    if gameOver:
        finalText = font.render(f"Game Over! Final Score: {score}", True, (255, 0, 0))
        textRect = finalText.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        window.blit(finalText, textRect)

    pygame.display.update()

pygame.quit()
