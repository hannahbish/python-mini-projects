import random

def roll_dice():
    dice = random.randint(1,6)
    print 'Rolling the dice... %d' % dice
    roll_again = raw_input('Would you like to roll again? Enter Y for Yes or any key for No. ')
    if roll_again == 'Y':
        roll_dice()
    else:
        print 'Goodbye!'

roll_dice()
