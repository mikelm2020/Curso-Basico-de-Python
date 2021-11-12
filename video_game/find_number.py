import random


def run():
    score = 1000
    random_number = random.randint(1, 100)
    print('Welcome to the game, You start with 1000 points')
    print('Each shot is of 100 points')
    number= int(input('Choose a number from 1 to 100:  '))
    while number != random_number:
        if number < random_number:
            print('Look for a bigger number')
        else:
            print('Look for a small number')
        number= int(input('Choose another number: '))
        score -= 100
    print('You win! has: ', score , ' points')




if __name__ == '__main__':
    run()