import pandas as pd
import random
countries=pd.read_csv('countries.csv')
countriesList=list(countries['COUNTRY'])
def playAtlas():
    global countriesList
    print("Starting Atlas Game ✨✨✨ \n\n")
    print("✨✨✨ TO EXIT THE GAME , ENTER 0  ✨✨✨")
    n=random.randint(0,213)
    cCountry=countriesList[n]
    print(cCountry)
    del(countriesList[n])
    turn=1
    pCountry=""
    while(True):
        if(turn==1):
            print("Player's Turn :")
            pCountry = playerTurn(cCountry[-1])
            if(pCountry=='0'):
                break
            turn=0
        if(turn==0):
            cCountry=compTurn(pCountry[-1])
            print(cCountry)
            turn=1

def compTurn(last):
    cCountry=""
    global countriesList
    for i in countriesList:
        if i[0]==last.upper():
            cCountry==i
            del(i)
            break

    return cCountry
def playerTurn(last):
    global countriesList
    status=1
    while(status):
        pCountry=input("Enter :")
        pCountry=pCountry.capitalize()
        if(pCountry=='0'):
            return pCountry
        if(pCountry[0]!=last.upper()):
            print("Wrong")
            continue
        elif(pCountry not in countriesList):
            print("No Country Found")
            continue
        else:
            ind=0
            for i in range(0,len(countriesList)):
                if(countriesList[i]==pCountry):
                    del(countriesList[i])
                    break
            status=0

    return pCountry
playAtlas()
