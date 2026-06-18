from random import randint

print(
    "welcome to the rock, paper,scissors game \n the rules are simple you pick one \n and then we play:)"
)
while True:
    try:
        random_num = randint(0, 2)
        if random_num == 0:
            compare_num = "r"
        elif random_num == 1:
            compare_num = "p"
        else:
            compare_num = "s"
        user_pick = (
            input(
                "please choose one of these to start playing \n [rock 'R' or r ] \n [paper 'P' or 'p' ] \n [scissors 'S' or 's']  \n if you want to exit write something else besides the three characters specified \n choose one and enter it here "
            )
            .strip()
            .lower()
        )

        if user_pick == compare_num:
            print(f"It is a draw we both picked {user_pick}")
        elif (
            (user_pick == "p" and compare_num == "r")
            or (user_pick == "r" and compare_num == "s")
            or (user_pick == "s" and compare_num == "p")
        ):
            print(f"you have won i picked {compare_num} and you picked {user_pick}")
        elif (
            (compare_num == "p" and user_pick == "r")
            or (compare_num == "r" and user_pick == "s")
            or (compare_num == "s" and user_pick == "p")
        ):
            print(f"I have won i picked {compare_num} and you picked {user_pick}")
        else:
            while True:
                print("you have entered an invalid valid please try again")
                exit_user = (
                    input(
                        "If you wish to quit the game and exit please enter 'exit' if you want to go back and play enter 'play' "
                    )
                    .strip()
                    .lower()
                )
                exit_strategy = False
                play_strategy = False
                while True:
                    try:
                        if exit_user == "exit":
                            print("thank you for your time")
                            exit_strategy = True
                            break
                        elif exit_user == "play":
                            print("you will be redirected to the play page!!")
                            play_strategy = True
                        else:
                            print("please enter one of the two options again !!")
                            break

                    except ValueError:
                        print("you have entered an invalid value try again ")
                    if play_strategy:
                        break
                    if exit_strategy:
                        break
                if play_strategy:
                    break
                if exit_strategy:
                    quit()

    except ValueError:
        print("you have entered an invalid input please try again!!")
