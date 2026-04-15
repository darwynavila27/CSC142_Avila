import pygame
import pygwidgets
from Deck import Deck


def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        value = card.getValue()

        if value in ["Jack", "Queen", "King"]:
            score += 10
        elif value == "Ace":
            score += 11
            aces += 1
        else:
            score += int(value)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


class BlackjackGame:
    def __init__(self, window):
        self.window = window

        self.hitButton = pygwidgets.TextButton(window, (50, 500), "Hit")
        self.stayButton = pygwidgets.TextButton(window, (150, 500), "Stay")
        self.newGameButton = pygwidgets.TextButton(window, (250, 500), "New Game")

        self.font = pygame.font.SysFont(None, 36)

        self.resetGame()

    def resetGame(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.playerHand = []
        self.dealerHand = []

        self.gameOver = False
        self.playerTurn = True
        self.message = ""

        # initial deal
        self.playerHand.append(self.deck.dealCard())
        self.playerHand.append(self.deck.dealCard())

        self.dealerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())

    def handleEvent(self, event):
        if self.hitButton.handleEvent(event):
            if self.playerTurn and not self.gameOver:
                self.playerHand.append(self.deck.dealCard())

                if calculate_score(self.playerHand) > 21:
                    self.message = "Bust! Dealer wins."
                    self.gameOver = True

        elif self.stayButton.handleEvent(event):
            if self.playerTurn:
                self.playerTurn = False
                self.dealerTurn()

        elif self.newGameButton.handleEvent(event):
            self.resetGame()

    def dealerTurn(self):
        while calculate_score(self.dealerHand) < 17:
            self.dealerHand.append(self.deck.dealCard())

        self.evaluateWinner()

    def evaluateWinner(self):
        player = calculate_score(self.playerHand)
        dealer = calculate_score(self.dealerHand)

        if dealer > 21:
            self.message = "Dealer busts! You win!"
        elif dealer > player:
            self.message = "Dealer wins!"
        elif dealer < player:
            self.message = "You win!"
        else:
            self.message = "Push."

        self.gameOver = True

    def draw(self):
        self.window.fill((0, 120, 0))

        # buttons
        self.hitButton.draw()
        self.stayButton.draw()
        self.newGameButton.draw()

        # player cards
        x = 50
        y = 300
        for card in self.playerHand:
            card.draw(self.window, (x, y))
            x += 60

        # dealer cards
        x = 50
        y = 100

        for i, card in enumerate(self.dealerHand):
            if i == 1 and not self.gameOver:
                # draw hidden card manually (DO NOT overwrite image permanently)
                back_card = Deck().cards[-1] if False else None  # placeholder (ignored)
                # safer: just temporarily load correct back image via Card system is better

                # simplest safe approach:
                hidden = True
            else:
                hidden = False

            if hidden:
                # draw a rectangle placeholder OR reuse back image via Card system would be ideal
                pygame.draw.rect(self.window, (200, 200, 200), (x, y, 50, 70))
            else:
                card.draw(self.window, (x, y))

            x += 60

        # text
        player_text = self.font.render(
            f"Player: {calculate_score(self.playerHand)}",
            True,
            (255, 255, 255)
        )

        dealer_text = self.font.render(
            f"Dealer: {'?' if not self.gameOver else calculate_score(self.dealerHand)}",
            True,
            (255, 255, 255)
        )

        msg_text = self.font.render(self.message, True, (255, 255, 0))

        self.window.blit(player_text, (50, 250))
        self.window.blit(dealer_text, (50, 50))
        self.window.blit(msg_text, (50, 420))
        