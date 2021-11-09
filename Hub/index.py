import pandas as pd
import DankMemer.dankmemer as dm
import DankMemer
import Hangman as hm
from csv import writer
pd.options.mode.chained_assignment = None
users = open('users.csv', 'a')
uwriter = writer(users)
class user():
    tag=0
    def __init__(self,username,password):

        self.id=user.tag
        user.tag+=1
        self.username=username
        self.password=password
        self.loggedin=False
        data=[self.id,self.username,self.password,self.loggedin]
        uwriter.writerow(data)
        users.close()

def runIndex():

    print("                                    ✨✨✨ Welcome To Discord Server ✨✨✨ ")
    dm.line()
    userInput=int(input("For User Registration Enter 1 \n"+
                        "To Access Available Bots Enter 2\n"))
    if(userInput==1):
        username=input("Enter Username :")
        password=input("Enter Password :")
        newUser=user(username,password)
        dm.line()
        print("User has been registered successfully")
        runIndex()
    if(userInput==2):
        username=input("Enter Username :")
        df = pd.read_csv("users.csv")
        if(len(df.where(df['username'] == username))==0):
            print("User Is Not Registered With This Server, Please Register First :")
            runIndex()
        elif(df.where(df['username'] == username).iloc[0, 3]==True):
            status2=True
            while status2:
                print("Bots Available :")
                print("🐸 Dank Memer 🐸 --> Enter 1")
                print("🌏    Atlas   🌏 --> Enter 2")
                print("‍👤   Hangman  👤 --> Enter 3")
                print()
                print("  To Log Out     --> Enter 4")
                print()
                userInput2 = int(input(": "))
                if (userInput2 == 1):
                    dm.runDankMemer()
                    continue
                elif (userInput2 == 3):
                    hm.runHangman()
                    continue
                elif (userInput2 == 4):
                    id = df.where(df['username'] == username).iloc[0, 0]
                    try:
                        df['loggedin'][id] = False
                        raise Exception
                    except:
                        print("Logged Out Successfully !!")
                    df.to_csv('users.csv', index=False)
                    status2=False
            runIndex()
        elif(df.where(df['username'] == username).iloc[0, 3]==False):
            dm.line()
            status=True
            print("You Must Log In First :( \n\n")
            while(status):
                password = input('Enter Your Password :')

                if (password == str(df.where(df['username'] == username).iloc[0, 2])):
                    id=df.where(df['username'] == username).iloc[0, 0]
                    try:
                        df['loggedin'][id]=True
                        raise Exception
                    except :
                        print("Logged In Successfully !!")
                    df.to_csv('users.csv',index=False)
                    status=False
                    runIndex()
                elif (password != df.where(df['username'] == username).iloc[0, 2]):

                    print("Wrong Password")









users.close()
runIndex()











        







    




