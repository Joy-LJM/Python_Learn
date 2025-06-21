import art
import random
from game_data import data


# def random_data():
#   item=data[random.randint(0,len(data)-1)]
#   return item

def compare(data_a, data_b):
    if data_a > data_b:
        return 'A'
    else:
        return 'B'


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def game():
    data_b = random.choice(data)
    score = 0
    game_continue = True
    # print logo and compare
    print(art.logo)
    while game_continue:
        # make data at position b become the next data  at position A
        data_a = data_b
        data_b = random.choice(data)
        if data_a == data_b:
            data_b = random.choice(data)

        print(f"Compare A: {format_data(data_a)} ")
        print(art.vs)
        print(f"Against B: {format_data(data_b)}")
        guess = input("Who has more followers? Type 'A'or 'B': ").upper()
        print('\n' * 20)
        print(art.logo)
        if guess == compare(data_a['follower_count'], data_b['follower_count']):
            score += 1

            print(f"You're right! Current {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
# if correct print("You're right! Current score+1")
# compare new
# one wong guess, ending the game print("Sorry, that's wrong. Final score: 3")
