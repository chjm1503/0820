#! python3
import random

class GuessingName:
    
    def __init__(self):
        self.__secret_number = random.randint(1, 101)

    def run(self):
        print("Guess the number!")

        guess = 0
        while True:
            guess = input("Please input your guess.")

            guess = int(guess)

            if guess == self.__secret_number:
                print('You win!')
                break
            elif guess < self.__secret_number:
                print('Too small!')
            else:
                print('Too big!')

GuessingName().run()