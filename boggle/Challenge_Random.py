import random

NUMBER_OF_GUESSES = 15
RANGE_TOP = 20
RANGE_BOTTOM = 1

while True:
    # generate the random number
    random_number = random.randint(RANGE_BOTTOM, RANGE_TOP)

    # give the user a certain amount of guesses
    for i in range(NUMBER_OF_GUESSES):
        guess = int(raw_input('guess the number: '))
        if guess == random_number:
            print 'Got the Number'
            break
        elif guess > random_number:
            print "This Number Too High"
        else:
            print "This Number Too Low"


    print "let's try a new number!"
    print "RANGE TOP:"
    print RANGE_TOP
    print "RANGE BOTTOM:"
    print RANGE_BOTTOM
