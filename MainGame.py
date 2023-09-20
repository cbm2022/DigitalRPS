import random

# Implemented data structures such as dictionaries to map a key to a list of values such as: Rock maps to a list of [scissors, rock, paper]. Each element in the list represents win, draw, lose in that order. 
#######    add a list to a dictionary    ##########
# my_dict = {'name': 'John', 'ages': [25, 30, 35]}
# print(my_dict['ages'])  # Output: [25, 30, 35]
###################################################

####   how to add multiple keys to dict   ####################
# my_dict = {'name': 'John', 'age': 25}
# new_data = {'city': 'New York', 'country': 'USA'}
# my_dict.update(new_data)  # Adding multiple key-value pairs
# print(my_dict)
##############################################################

## 8/21 i need to be able to create these dictionaries with user input names

#this is only true for the playerpick!
ROCK = 1
PAPER = 2
SCISSORS = 3

##### BREAK DOWN #####
# if I, the player choose rock/1 we look at the array of the dictionary entry
# Then if the computer picks 0, which is scissors I, the player lose
# the player will always lose if the computer picks 0
# the player will always win if the computer picks 2
# the 2 players will always tie if the computer picks 1
#######################

#computer pick has to have a range of 0-2 (3 options)
PlayableHands = {ROCK:['scissors','rock','paper'],   
                 PAPER:['rock','paper','scissors'],    
                 SCISSORS:['paper','scissors','rock']}

# this isnt used in the code its just a graphic
RockHand = {"strength": "scissors", "ineffective":' Rock', "Weakness": 3}

class ConsoleDialouge:
    def __init__(self):
        pass

    #will print title ONCE
    def Start(self):
        print("Welcome to Digital rock paper scissors")

    #WORK IN PROGRESS
    def GetLanguage(self):
        print("----------------------------------------------Language Select----------------------------------------------")
        print("1. English     2. Spanish       3. French")
        # language = int(input("your language selected is "))
        language = 1
        if(language == 1):
            return(language)
        elif(language == 2):
            #do this
            pass
        else:
            pass

    #WORK IN PROGRESS
    def SetLanguage(self):
        #do the thing, this is where ill use the library to change all the words
        pass

    # Ask for user input, has expection handling
    def PlayerTurn(self):
        print(" 1        2          3   ")
        print("ROCK    PAPER    SCISSORS")
        while True:
            pick = input("-->")
            try:
                pick = int(pick)
                if 1 <= pick <= 3:
                    break
                else:
                    print("[input is not valid ): ] type 1, 2, or 3")
            except ValueError:
                print("Not a number, please enter a number")
        return(pick)
    
    # the computer picks a random number between 0-2 and that becomes their handshape
    def ComputerTurn(self):
        pick = random.randint(0,2)
        # pick = 2
        return(pick)

#game result calcs who wins
    #this function displays the result of the turn and has some game logic
    def GameResult(self, playerpick, computerpick):
        pass
        #old way below
        # #tie between player and copmuter
        # if playerpick == computerpick:
        #     print("DRAW!")
        #     return(0)
        # #player wins
        # elif playerpick > computerpick:
        #     print("inconclusive a or player wins")
        #     return(2)
        # #computer wins
        # elif playerpick < computerpick:
        #     print("inconlusive b or computer wins")
        #     return(0)
        # else:
        #     print("Invalid Input")
        #     persist = persist + 0
        
    # Asks the player if they would like to play the game again this works with the gameplayloop later in the code
    def GameOver(self):
        print("play agian?")
        while True:
            answer = input("-->")
            try:
                answer = str(answer)
                if answer == "n":
                    return(0)
                if answer == "y":
                    return(1)
                else:
                    print("not valid my guy")
            except ValueError:
                print("value error bro")
        
    # Starts the gameplay but not in control of the loop
    def PlayGame(self,playerpick,computerpick):
         # if the shape the computer picks is indexed as position 1 in the chosen array than the I, the player lose
         if PlayableHands[playerpick][computerpick] == PlayableHands[playerpick][-1]:
            print("Player lost to", PlayableHands[playerpick][computerpick])
            return(1)
         
         elif PlayableHands[playerpick][computerpick] == PlayableHands[playerpick][0]:
            print("Player wins with", PlayableHands[playerpick][1])
            return(1)

         elif PlayableHands[playerpick][computerpick] == PlayableHands[playerpick][1]:
            print("Player ties with", PlayableHands[playerpick][-2])
            return(0)
    

def main():
    #making a new console, there should only be one console but you can make 2
    console1 = ConsoleDialouge()

    #gameplayloop will only start if persistance is == 1
    persist = 1

    #total amount of games counter, goes up by 1 in the gameplay loop
    totalgames = 0

    #tells the console to display startup
    console1.Start()

    #gets the input from the user as to which language to use
    console1.GetLanguage()

    #this tells the game to switch dialouge to that language
    console1.SetLanguage()
    
    print("\n \n \n \n \nNew Game Session Started")
    
    #gameplayloop!!!
    while persist == 1 and totalgames < 10:
        print("\n\n\n   Game #" + str(totalgames + 1) + " Started")
        computerpick = console1.ComputerTurn()
        playerpick = console1.PlayerTurn()
        gameresult = console1.PlayGame(playerpick, computerpick)
        persist = gameresult + persist
        totalgames = totalgames + 1
        if persist != 1: 
            breakcondition = console1.GameOver()
            if breakcondition == 0:
                print("see you later, [Dramatic Pause] spiderman")
                break
            elif breakcondition == 1:
                persist = 1
                totalgames = 0

if __name__ == "__main__":
    main()