# Dank Memer
# Utilities -
#     Random Joke
#     Guess the number - simple game
#     A random meme- Hindi / English
import random
import requests
from PIL import Image
import pandas as pd
import time
import os

def runDankMemer():
    print("Hello Welcome to this bot :)\n")
    status=1
    while(status):
        line()
        userInput=int(input("To play guess the number game, enter 1\n"
                            "To listen a random joke,       enter 2\n"
                            "To see a meme,                 enter 3\n"
                            "To get a riddle,               enter 4\n"
                            "To exit from Dank Memer,       enter 5\n"))
        line()
        if(userInput==1):
            guessNumber()
        elif(userInput==2):
            getJoke()
        elif(userInput==3):
            getMeme()
        elif(userInput==4):
            getRiddle()
        elif (userInput == 5):
            print("Thank You :)")
            status=0
        else:
            print("Invalid Input")
        line()

def guessNumber() :
    line()
    status = 1
    while (status):
        print("Guess a number between 1 to 100 \n")
        n = random.randint(1, 100)
        flag = 1
        while (flag):
            guess = int(input("Enter your guess :"))
            if (guess < n):
                print("oops !! Think of a greater one")
                continue
            if (guess > n):
                print("oops !! Think of a lesser one")
                continue
            if (guess == n):
                print("You Won !!!")
                break
            line()
        status = int(input("Do you want to play again ? Enter 1 to play or 0 to exit ."))
    print("Thank You .")
def getJoke():
    line()
    status = 1
    while (status):
        response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious,racist,sexist&type=single")
        print(response.json()['joke'])
        print()
        time.sleep(4)
        status = int(input("Do you want to listen a joke again ? Enter 1 to play or 0 to exit ."))
        print()
        line()
    print("Thank You .")
def getMeme():
    line()
    status = 1
    while (status):
        n = str(random.randint(1, 18))
        path=os.path.abspath('../DankMemer/memes/'+n+'.jpg')
        # image = Image.open("memes/" + n + ".jpg")
        image = Image.open(path)
        image.show()
        status = int(input("Do you want to see one more ? Enter 1 to play or 0 to exit ."))
        line()
    print("Thank You .")
def getRiddle():
    line()
    status=1
    while(status):
        n = random.randint(0, 19)
        print("You have 15 seconds to answer the riddle : Answer will be shown automatically, do not enter anything")
        time.sleep(3)
        path=os.path.abspath('../DankMemer/riddles.csv')
        data = pd.read_csv(path, index_col=False)
        print("Riddle : " + data['question'][n])
        time.sleep(15)
        print("Time Up !!! Answer is : " + data['answer'][n])
        status=int(input("Do you want to play again ? Enter 1 to play or 0 to exit ."))
        line()
    print("Thank You .")
def line():
    print()
    for i in range(10):
        print("*************",end="")
    print("")









