import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players(2-4): ").strip()
    if players.isdigit():
        players = int(players)
        if 1 < players <= 4:
            break
        else:
            print("the value you entered should be between two and four(2-4)")
            continue
    else:
        print("you have entered an invalid input please try again: ")
        continue
print(players)
max_score = 50
player_scores = [0 for _ in range(players)]
print(player_scores)
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"player number {player_idx +1} turn has started ")
        print(f"the total score is {player_scores[player_idx]}")

        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ").lower()
            if should_roll == "y":
                value = roll()
                if value == 1:
                    print("you rolled a 1! Turn done!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print("You rolled a: ", value)
                print("your score is: ", current_score)
            else:
                break
        player_scores[player_idx] += current_score
        print("your total score is : ", player_scores[player_idx])
max_scored = max(player_scores)
wining_idx = player_scores.index(max_scored)
print(f"player number, {wining_idx +1} is the winner with a score of {max_scored}")
