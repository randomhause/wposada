from random import randrange

#using a list for the powers of two minus one instead of calculating each time, because there are so few
two_power = [3,7,15,31,63] 

def nim():
    """
    Plays the game of Nim with the user - the pile size, AI intelligence and starting user are randomly determined
    Returns True if the user wins, and False if the computer wins
    """
    #randomly generating the pile size
    pile_size = randrange(10, 101) 
    #decides who starts - 0 is computer's turn and 1 is human's
    turn = randrange(0,2) 
    #decides whether the computer is smart or dumb - 0 is dumb and 1 is smart
    ai_intel = randrange(0,2) 


    print('The pile is %s marbles to begin' %(pile_size))

    if ai_intel == 0:
        print('The computer is dumb... you\'re in luck')
    else:
        print('The computer is smart... play well')

    #creating a loop that only breaks when the pile is two and the game is decided
    while pile_size > 2: 
        #all of the computer's decisions will be here, when it is the computer's turn
        if turn == 0: 
            print('\n\n***Computer\'s Turn***')
            #the computer wll only take a random amount if it is dumb or if the pile size is a power of 2 minus 1
            if ai_intel == 0 or pile_size in two_power:
                comp_take = randrange(1, pile_size // 2 + 1)
            #if the computer is smart and making the pile a power of 2 minus 1 is a legal move, it will do so
            else: 
                for power in two_power:
                    #checks which power of 2 minus 1 can be created with a legal move
                    if (pile_size // 2 >= pile_size - power) and (pile_size - power > 0):
                        #the computer will take however many marbles it takes to make the pile the power of 2 minus one
                        comp_take = pile_size - power
                        break
            pile_size -= comp_take
            print('\nThe computer takes %d marble(s) from the pile. The pile now has %d marble(s)' %(comp_take, pile_size))
            #once the computer's turn is done, it changes the turn variable
            turn = 1
        #player's turn
        else:
            #preventing the human from having a turn if the pile is size 2, because the game is decided
            if pile_size == 2:
                break
            print('\n\n***Your Turn***')
            hum_take = 0
            #forcing the user to input a valid move
            while hum_take < 1 or hum_take > pile_size // 2:
                hum_take = int(input('Please input an integer between 1 and %d: ' %(pile_size // 2)))
            pile_size -= hum_take
            print('\nYou take %d marble(s) from the pile. The pile now has %d marble(s)' %(hum_take, pile_size))
            #changing the turn back to the computer
            turn = 0
    #uses the most recent turn value to determine the winner
    #whoever's turn it is when the pile is 2 wins the game by taking one marble
    if turn == 0:
        print('\n\nThe computer takes one marble and leaves you with the last one... YOU LOSE!')
        return False
    else:
        print('\n\nYou take one marble and leave the computer with the last one... YOU WIN!')
        return True

nim()