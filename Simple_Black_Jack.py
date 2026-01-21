import random

# Move a card from deck to hand

def draw_card(hand, deck):
    hand.append(deck.pop()) # take last card from deck

def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            aces += 1
        else:
            score += int (card)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def print_status(player_hand, dealer_hand, show_dealer_full=False):
    print ("\nPlayer hand:", player_hand, "Score:", calculate_score(player_hand))

    if show_dealer_full:
        print("Dealer hand:", dealer_hand, "Score:", calculate_score(dealer_hand))
    else: 
        print ("Dealer shows:", dealer_hand[0])


def main():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    player_hand = []
    dealer_hand = []

    # shuffle deck 
    random.shuffle(deck)

    # first deal 
    draw_card(dealer_hand, deck)
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)

    #player turn 
    while True:
        print_status(player_hand, dealer_hand)
        player_score = calculate_score(player_hand)
    
        if player_score > 21:
            print ("\nBust! Dealer wins.")
            return

        choice = input("\n(H)it or (S)tay?").lower()
        if choice == "h":
            draw_card(player_hand, deck)
        elif choice == "s":
            break
        else: 
            print ("Input not valid. Enter 'h' or 's'.")
    
    #dealer turn
    while calculate_score(dealer_hand) < 17:
        draw_card(dealer_hand, deck)
    
    print_status(player_hand, dealer_hand, show_dealer_full=True)

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    #winner
    if dealer_score > 21:
        print ("\nDealer busts! Player wins.")
    elif dealer_score > player_score:
        print ("\nDealer wins.")
    elif dealer_score < player_score:
        print ("\nPlayer wins!")
    else:
        print ("\nPush.")

if __name__ == "__main__":
    main()
