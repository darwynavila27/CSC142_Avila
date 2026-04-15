import pygame
from BlackjackGame import BlackjackGame

def main():
    pygame.init()

    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blackjack GUI")

    game = BlackjackGame(window)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handleEvent(event)

        game.draw()
        pygame.display.update()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
    