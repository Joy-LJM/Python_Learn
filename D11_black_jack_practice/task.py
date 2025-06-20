import art
import random


def deal_card():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(card_list)
    # black jack
    if score == 21 and len(card_list) == 2:
        return 0
    if 11 in list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return score


def compare(user_score, computer_score):
    """Compares the user score u_score against the computer score c_score."""
    if user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score == 0:
        return "You win with a black jack."
    elif computer_score == 0:
        return "Lose, opponent win with a black jack."
    elif user_score == computer_score:
        return "Draw."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def play_game():
    print(art.logo)
    is_game_over = False
    computer_score = -1
    user_score = -1
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card},current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
            if another_card == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
    # deal card for computer
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card},final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()
