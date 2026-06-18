def main():
    print("Welcome to my quiz game!!")
    playing()


def playing():
    attempts = 0
    while True:
        var_playing = (
            input("Do you want to play a game? yes [y or Y]No [N or n]").lower().strip()
        )
        attempts = checkinput(var_playing, attempts)


def checkinput(input, attempt):
    m = 0
    if input == "y":
        print("Okay let's play :)")
        gamelogic()
        quit()
    elif input == "n":
        print("Thank you for your time :)")
        quit()
    else:
        print("you have entered an invalid character \n try again!")

        new_attempts = exiting(attempt)
        return new_attempts


question_list = [
    {1: "what does CPU stands for? "},
    {2: "what does GPU stands for? "},
    {3: "what does ALU stands for? "},
]
answer_list = [
    {1: "central processing unit"},
    {2: "graphical processing unit"},
    {3: "arithmetic logic unit"},
]


def extract_list(list1, list2):
    # print(list1, list2)
    # n=0
    # print(len(list1))
    # print(len(list2))
    n = 0
    m = 0
    while n < min(len(list1), len(list2)):
        # print(type(list2[n]), type(list2[n]))
        if isinstance(list1[n] and list2[n], dict):
            for key, value in list1[n].items():
                # print(key, value)
                user_answer = input(value).lower().strip()
                for key, value in list2[n].items():
                    if user_answer == value:
                        print(f"correct {user_answer} = {value}")
                        m += 1
                    else:
                        print(f"your are incorrect the answer is {value}")
        n += 1

    print(f"you were able to answer {m} out of {n} questions ")

    # print(list1[n], list2[n])


def gamelogic():
    questions_answers = extract_list(question_list, answer_list)


def exiting(z):
    z = checkattemp(z)
    if z > 5:
        print(z)
        quit()
    else:
        print("you have more chances ")
        return z


def checkattemp(n):
    n += 1
    print(f"{n} is this ")
    return n


main()
