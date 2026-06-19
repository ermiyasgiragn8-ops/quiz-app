from random import randint


def main():
    print(
        "welcome to the rock, paper,scissors game \n the rules are simple you pick one \n and then we play:)"
    )
    game_logic()


def num_management():
    while True:
        try:
            random_num = randint(0, 2)
            if random_num == 0:
                compare_num = "r"
                print(compare_num)
            elif random_num == 1:
                compare_num = "p"
                print(compare_num)
            else:
                compare_num = "s"
                print(compare_num)
            return compare_num
        except ValueError:
            print("you have entered an invalid input")


def invalid_input():
    while True:
        while True:
            print("you have entered an invalid valid please try again")
            exit_user = (
                input(
                    "If you wish to quit the game and exit please enter 'exit' if you want to go back and play enter 'play' "
                )
                .strip()
                .lower()
            )
            strategy = ["yes", "no", "invalid"]
            while True:
                try:
                    if exit_user == "exit":
                        print("thank you for your time")
                        exit_strategy = strategy[0]
                        print(exit_strategy)
                        break
                    elif exit_user == "play":
                        print("you will be redirected to the play page!!")
                        exit_strategy = strategy[1]
                        print(exit_strategy)
                        break
                    else:
                        print("please enter one of the two options again !!")
                        exit_strategy = strategy[2]
                except ValueError:
                    print("you have entered an invalid value try again ")
                    break
                if exit_strategy != strategy[2]:
                    return exit_strategy
                else:
                    print(exit_strategy)
                    break

            if exit_strategy != strategy[2]:
                return exit_strategy
            else:
                print(exit_strategy)
                break


def game_logic():

    while True:
        machine_pick = num_management()
        player_pick = user_management()
        if player_pick == machine_pick:
            print(f"It is a draw we both picked {player_pick}")

        elif (
            (player_pick == "p" and machine_pick == "r")
            or (player_pick == "r" and machine_pick == "s")
            or (player_pick == "s" and machine_pick == "p")
        ):
            print(f"you have won i picked {machine_pick} and you picked {player_pick}")

        elif (
            (machine_pick == "p" and player_pick == "r")
            or (machine_pick == "r" and player_pick == "s")
            or (machine_pick == "s" and player_pick == "p")
        ):
            print(f"I have won i picked {machine_pick} and you picked {player_pick}")

        else:
            print("this value is invalid")
            new_strategy = invalid_input()
            print(f"this is the returned {new_strategy}")
            if new_strategy == "yes":
                return print("thank you for your time :)")
            else:
                continue


def user_management():
    while True:
        try:
            user_pick = (
                input(
                    "please choose one of these to start playing \n [rock 'R' or r ] \n [paper 'P' or 'p' ] \n [scissors 'S' or 's']  \n if you want to exit write something else besides the three characters specified \n choose one and enter it here "
                )
                .strip()
                .lower()
            )
            return user_pick
        except ValueError:
            print("you have entered an invalid input")


main()
