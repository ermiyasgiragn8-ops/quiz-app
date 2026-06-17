print("Welcome to my quiz game!!")
playing = input("Do you want to play a game? Yes[Y or y], No[N or n]").lower().strip()
if playing != "y":
    print("Thanks for your time good bye:)")
    quit()
print("Okay so let's play:) ")
n = 0
answer = input("what does CPU stands for? ").lower().strip()
if answer != "central processing unit":
    confirm = (
        input(
            "sorry you have the wrong answer! Would you like to know the correct answer?  Yes[Y or y], No[Write anything besides Y or y] "
        )
        .lower()
        .strip()
    )
    if confirm == "y":
        print("the correct answer is Central Processing Unit")
    else:
        print("Okay let's move to the next question.")

else:
    n += 1
    print("that is a correct answer good job")
answer = input("what does ALU stands for? ").lower().strip()
if answer != "arithmetic logic unit":
    confirm = (
        input(
            "sorry you have the wrong answer! Would you like to know the correct answer? Yes[Y or y], No[Write anything besides y or Y] "
        )
        .lower()
        .strip()
    )
    if confirm == "y":
        print("the correct answer is Arthimetic Logic Unit")
    else:
        print("Okay let's move to the next question.")
else:
    n += 1
    print("that is a correct answer good job")
answer = input("what does OS stands for? ").lower().strip()
if answer != "operating system":
    confirm = (
        input(
            "sorry you have the wrong answer! Would you like to know the correct answer?  Yes[Y or y], No[Write anything besides y or Y]"
        )
        .lower()
        .strip()
    )
    if confirm == "y":
        print("the correct answer is Operating system")
    else:
        print("Okay let's move to the next question.")

else:
    n += 1
score = (n / 3) * 100
score = round(score, 2)
print(
    f"that is a correct answer good job. you were able to answer {n} questions out of 3"
)
print(f"You were able to score {score}%")
