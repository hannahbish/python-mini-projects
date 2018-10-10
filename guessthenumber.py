import random

secret_number = random.randint(1,100)

def is_int(str):
    try:
        res = int(str)
        return isinstance(res, (int, long))
    except:
        return False

def prompt_guess(prompt):
    guess = raw_input(prompt)
    process_guess(guess)

def quit(goodbye_text):
    print goodbye_text

def process_guess(user_input):
    if user_input == 'Q':
        quit('Goodbye! The number was %d' % secret_number)
    elif not is_int(user_input):
        prompt_guess('You did not guess an integer number. Try again or enter Q to quit: ')
    elif int(user_input) == secret_number:
        quit('You guessed the number! It was %d' % secret_number)
    elif int(user_input) > secret_number:
        prompt_guess('Your guess is too high! Try again or enter Q to quit: ')
    elif int(user_input) < secret_number:
        prompt_guess('Your guess is too low! Try again or enter Q to quit: ')

prompt_guess('Guess the number! Enter a number between 1 and 100: ')
