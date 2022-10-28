import higher_lower_data
import random

data = higher_lower_data.data
logo = higher_lower_data.logo
vs = higher_lower_data.vs

current_score = 0
random.shuffle(data)

temp_data = data

A = random.choice(temp_data)
temp_data.remove(A)
B = random.choice(temp_data)
temp_data.remove(B)


def game(current_score, A, B):
    print(logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if A['follower_count'] > B['follower_count']:
        higher = 'A'
    else:
        higher = 'B'
    if answer == higher:
        current_score += 1
        print(f"You are right! Current score: {current_score}")
        A = B
        B = random.choice(temp_data)
        temp_data.remove(B)
        game(current_score, A, B)
        if current_score == len(data):
            return "You got all of them right! You are the highest scorer!"
    else:
        print(f"Sorry, you are wrong. Final score: {current_score}")


game(current_score, A, B)
