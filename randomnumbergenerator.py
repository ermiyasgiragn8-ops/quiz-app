from random import randint

print("welcome to random number generator game!!")
exit_all = False
while True:
    while True:
        try:
            rand_range = int(input("Enter a number to set the range for the game"))
            if rand_range <= 0:
                print("you can only enter natural numbers ")
                continue
            else:
                print("okay we will start the game soon ")
                break
        except:
            print("you have entered an invalid input the game is going to stop ")
            exit_all = True
            break
    if exit_all:
        break
    n = 0
    radomnum = randint(0, rand_range)
    print(f"the range is going to be from 0 upto {rand_range}")
    while True:

        while True:
            try:
                guess = int(input("please guess a number "))
                if guess <= 0:
                    print("you can not try to enter a negative number try again ")
                    n += 1
                    exit_all = True
                    continue
                elif guess > 0:
                    break

            except:
                print("please enter a valid number ")
                quiting = input(
                    "if you want to stop the game please enter [n or N or any character besides y or Y]"
                ).lower()
                if quiting == "n":
                    print("thanks for your time :)")
                    exit_all = True
                    break
                elif quiting == "y":
                    continue
        if exit_all:
            break
        n += 1
        if n > 5:
            exit_all = True
            break
        if guess == radomnum:
            print("wow you nailed it you guessed the correct number")
            break
        elif guess < radomnum:
            print("your guess is too low try again ")
        elif guess > radomnum:
            print("Your guess is too high try again ")
    if exit_all:
        print("thanks for your time")
        break
