import random

word_list = open("commonenglishwords.txt").read().split()
word_list_len = len(word_list)
dict = {
    'human_game_dict': ''
}

def generate_new_game():
    secret_word = word_list[random.randint(0, word_list_len - 1)]
    secret_word_len = len(secret_word)
    return {
        'guesses_left': 6,
        'letters_guessed': [],
        'hangman': ['-'] * secret_word_len,
        'secret_word': secret_word,
        'secret_word_len': secret_word_len
    }

def is_alpha_char(str):
    return str.isalpha() and len(str) == 1

def get_index_list(element, list):
    return [i for i, e in enumerate(list) if e.upper() == element.upper()]

def prompt_guess(prompt):
    guess = raw_input(prompt)
    validate_guess(guess)

def quit(goodbye_text):
    print goodbye_text

def prompt_play_again():
    play_again = raw_input('Would you like to play again? Enter Y to play again or any other key to quit: ')
    if play_again.lower() == 'y':
        start_game()
    else:
        quit('Goodbye!')

def game_won():
    print 'Congratulations! You completed the word ' + dict['hangman_game_dict']['secret_word'] + '!'
    prompt_play_again()

def game_lost():
    print 'Sorry! You ran out of guesses. The word was: ' + dict['hangman_game_dict']['secret_word'] + '.'
    prompt_play_again()

def handle_wrong_guess(uppercase_input):
    print uppercase_input + ' is not in the word!'
    dict['hangman_game_dict']['guesses_left'] -= 1
    if dict['hangman_game_dict']['guesses_left'] == 0:
        game_lost()
    else:
        start_new_play()

def handle_correct_guess(uppercase_input, indexes_in_secret_word):
    for index in indexes_in_secret_word:
        dict['hangman_game_dict']['hangman'][index] = uppercase_input
    letters_remaining = get_index_list('-', dict['hangman_game_dict']['hangman'])
    if len(letters_remaining) > 0:
        start_new_play()
    else:
        game_won()

def process_hangman_play(input):
    uppercase_input = input.upper()
    indexes_in_guessed_words = get_index_list(uppercase_input, dict['hangman_game_dict']['letters_guessed'])
    if len(indexes_in_guessed_words) > 0:
        print('You already guessed ' + uppercase_input + '.')
        start_new_play()
    else:
        dict['hangman_game_dict']['letters_guessed'].append(uppercase_input)
        indexes_in_secret_word = get_index_list(uppercase_input, dict['hangman_game_dict']['secret_word'])
        if len(indexes_in_secret_word) == 0:
            handle_wrong_guess(uppercase_input)
        else:
            handle_correct_guess(uppercase_input, indexes_in_secret_word)

def validate_guess(user_input):
    if user_input.lower() == 'quit':
        quit('Goodbye! The word was ' + dict['hangman_game_dict']['secret_word'])
    elif not is_alpha_char(user_input):
        prompt_guess('You did not guess an alphabet character. Try again or enter Quit to quit: ')
    else:
        process_hangman_play(user_input)

def start_new_play():
    print('Number of guesses left: ' + str(dict['hangman_game_dict']['guesses_left']))
    if len(dict['hangman_game_dict']['letters_guessed']) > 0:
        print('Letters already guessed: ' + ' '.join(dict['hangman_game_dict']['letters_guessed']))
    print(' '.join(dict['hangman_game_dict']['hangman']))
    guess = raw_input('Guess a letter: ')
    print ''
    validate_guess(guess)

def start_game():
    dict['hangman_game_dict'] = generate_new_game()
    print('Welcome to Hangman!')
    start_new_play()

start_game()
