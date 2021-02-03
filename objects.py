import random 


class User:
    def input_number(self):
        try:
            number = int(input('What is your number?(1-10): '))
            if number >= 1 and number <=10:
                return number
            else:
                print('Please enter a number between 1 and 10! x1')
                return user.input_number()
        except:
            print('Please enter a number between 1 and 10! x2')
            return user.input_number()


user = User()


class Computer:
    def random_number(self):
        random_guess = random.randint(1, 10)
        return random_guess


computer = Computer()

