#Hangman bot for discord.py -
#create a “guess the word” game.

import random

def runHangman():
    print("                                          🐱‍👤Welcome to the Hangman Game🐱‍👤")
    line()
    easy=['goa','delhi','paris','patna','mumbai','iraq','kota','kerala','pakistan','nagpur','pune','bhopal','haryana','punjab']
    medium=['amsterdam','newyork','kashmir','srinagar','afghanistan','turkey','newzealand','bishkek','ahmedabad','jaisalmer','chandigarh']
    hard=['vishakapatnam','thiruvananthapuram','australia','melbourne','sanfrancisco','washington','aizawal','damascus','baghdad','hyderabad']

    print('''             To play EASY level (3 guesses limit)--> Enter 1
             To play MEDIUM level (4 guesses limit)--> Enter 2
             To play HARD level (5 guesses limit)--> Enter 3
             To exit the game -->Enter 4 ''')


    level = int(input(' '))                    #asking for level-EASY, MEDIUM or HARD
    right = ''                                                 
    guesses = 0
    flag = 1
    if level == 1:
        right = random.choice(easy)                         
        guesses = 3
    elif level == 2:
        right = random.choice(medium)
        guesses = 4
    elif level == 3:
        right = random.choice(hard)
        guesses = 5
    elif level == 4:
        flag = 0
        print('Thank you!🙂')
    else :
        print('INVALID INPUT!')
        runHangman()

    if (flag == 1):   
        right_list = list(right)
        print('There are {} letters in the word to be guessed !'.format(len(right)))   #displaying no. of letters in the word to be guessed!

    if flag == 1:
        guess = ''
        while right_list != []:                                         
            guessed_letter = input('Your guess please : ').lower()
            if guessed_letter in right_list :
                right_list.remove(guessed_letter)
                print('CORRECT!!👏')
            else:
                guesses -= 1
                print('Oops! Remaining guesses = {}'.format(guesses))
            if right_list == []:
                print('HURRAY!!🥳 YOU WON!!')
                line()
                break
            if guesses == 0:                                                #in case the guesses exhaust
                print('YOU LOST!🙁 The correct word was {}...Better luck next time!'.format(right))
                line()
                break

    if flag == 1:
        decision = int(input('Wanna play again?😎--> Enter 1 OR Enter 0 to EXIT: '))
        line()
        if (decision == 1):
            runHangman()
        elif (decision == 0):
            print("Thank you!🙂")
            line()
        else :
            print('INVALID INPUT!')
            line()
            runHangman()

def line():
    print()
    for i in range(10):
        print("*************",end="")
    print("")

