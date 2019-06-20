###Random Number Guessing Game

import random;

def game(playerName):
    print('Hey ' + playerName + '! Let us play a game. I would be guessing a random number between 1 and 10 (both inclusive).');
    number=random.randint(1,10);
    print('Take a guess.');
    count = 7;
    i=1;
    while i<count:
        try:
            guess = int(input());
            if guess==number:
                print('Correct Guess! It took you ' + str(i) + 'chances to figure it out.');
                break;
            elif guess>number:
                print('Little lower. Number guessed is too high.');
            else:
                print('Bit higher. Number guessed is too low.');
        except:
            print('Did you enter a number or something else ???');
        print('Guess Again!');
        i+=1;
    print("Thanks " + playerName + " for playing!");


print("Please enter your name.");
name = input();
game(name);
