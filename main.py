import random
import objects


def guess_my_number():
    user_input = objects.user.input_number()
    computer_guess = objects.computer.random_number()
    if user_input == computer_guess:
        print(f'My guess is {computer_guess}. Your\'s is {user_input}. My guess was correct! P.S. Computer\'s are always right!')
    elif computer_guess > user_input:
        print(f'My number is {computer_guess}, Your\'s is {user_input}. My number is higher. I was wrong... HOW DID... THAT HAPPEN? ...COMPUTING....')
    elif computer_guess < user_input:
        print(f'My number is {computer_guess}, Your\'s is {user_input}. My number is lower. I was wrong... HOW DID... THAT HAPPEN? ...COMPUTING....')
    play_again = input("Wanna play again, humanoid?(Yes/No): ")
    if play_again == "Yes" or play_again == "yes":
        guess_my_number()
    elif play_again == "No" or play_again == "no":
        print('Oh, you are afraid you are going to lose against a machine. Exiting the program now!')
    else:
        print('Invalid choice. Let\'s play again, human!')
        return guess_my_number()



guess_my_number()




    




