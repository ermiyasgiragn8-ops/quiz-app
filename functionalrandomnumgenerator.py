from random import randint


def main():
    print("welcome to random number generator game!!")
    print("hello world")
    game_logic()


def exiting(num):
    if num > 5:
        quit()


def check_number(n):
    if n < 0:
        print("you can only enter a natural number ")
        return False
    else:
        return n


def counting(m):
    m += 1
    exiting(m)
    return m


def num_range():
    m = 0
    while True:
        try:
            rand_range = int(input("Enter a number to set the range for the game "))
            if check_number(rand_range) == False:
                m = counting(m)
                continue
            #     print("you can only enter natural numbers")
            #     continue
            else:
                print("okay we will start the game soon")
                return rand_range
        except:
            print("You have entered an invalid input the game is going to stop ")
            print("value error")
            print("Good bye :)")
            break
    counting(m)


def generate_random():
    rand_num = num_range()
    while True:
        my_guess = randint(0, rand_num)
        print(f"the range is going to be from 1 upto {rand_num}")
        return my_guess


def comparing(guess, target):
    if guess == target:
        print("wow you nailed it you guessed the correct number")
        quit()
    elif guess < target:
        print("your guess is too low try again ")
    elif guess > target:
        print("Your guess is too high try again ")


def game_logic():
    finalnum = generate_random()
    m = 0
    while True:
        while True:
            try:
                guess = int(input("please guess a number "))

                value = check_number(guess)
                if value == False:
                    print("you have entered a negative number ")
                    m = counting(m)
                    continue
                else:
                    comparing(value, finalnum)
            except:
                print("value error you have entered an invalid number")
                quit()


main()
