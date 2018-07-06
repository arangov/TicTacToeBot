import random

#reset variables for future rounds, test multiple times to determine capabilities/bugs

#allows the user to determine what side they want to be on
def chooseSide():
    sides = ["O", "X"]
    #prompt user to choose their side
    userSide = input("Do you want to be O or X?")

    #user side is O, determines turn of orders
    if userSide.upper().strip() == "O":
        print("You have chosen " + userSide.upper().strip() + ".")
        sides.remove(userSide.upper().strip())
        print("That means I will be " + sides[0] + ".")
        print(
            "The way the game works is the top row goes from A1 on the left to A3, " 
            "the middle row is B with the same number convention, and the bottom row is C.")
        return userSide.upper().strip()
    #user side is X, determines turn of orders
    elif userSide.upper().strip() == "X":
        print("You have chosen " + userSide.upper().strip() + ".")
        sides.remove(userSide.upper().strip())
        print("That means I will be " + sides[0] + ".")
        print("The way the game works is the top row goes from 0 on the left to 2, "
              "the middle row is 3 to 5, and the bottom row is 6 to 8.")
        return userSide.upper().strip()
    #if the user chooses a side/input that isn't X or O
    else:
        print("You have chosen incorrectly, game over!!!")
        print("I will be waiting here until you consider the decision you made.")
        return ""

#allows whoever's side is X to make their move
def firstMoves():
    if userChoice == "O" and currentPlayer == 'X':
        #randomNum = random.randint(0,8)
        firstMove = 4
        print("Alright, so I'm going to choose " + str(firstMove) + ".")
        print("Your turn, let's see how you do.")
        return int(firstMove)
    elif currentPlayer == 'X' and userChoice == 'X':
        firstMove = input("What is your move?")
        print("Oh yeah, " + firstMove + " is a good one.")
        return firstMove
    elif currentPlayer == 'O' and userChoice == 'O':
        firstMove = input("What is your move?")
        print("Oh yeah, " + firstMove + " is a good one.")
        return firstMove

#determines the bots earlier moves because no one has the ability to win
def nextMoves(currentPlayer, move, lastMove, X, O):
    #keeps track of all options, besides center
    corners = [0, 2, 6, 8]
    middle = [1, 3, 5, 7]

    #off chance the last move ends up having this method called
    if tiles.__len__() is 1:
        return tiles[0]
    #first move for bot
    elif move is 1:
        #O chooses the corner if X's first move was the center
        if int(lastMove) is 4:
            return 0
        #O chooses center if X didn't choose center first
        elif int(lastMove) in corners or int(lastMove) in middle:
            if tiles.__contains__(4):
                return 4
            else:
                for item in corners:
                    if tiles.__contains__(item):
                        return item
                else:
                    if tiles.__contains__(4):
                        return 4
                    else:
                        for item in middle:
                            if tiles.__contains__(item):
                                return item
    #second move for bot
    elif move is 3:
        #keeps X's current choices organized
        X.sort()

        #handles top-left to bottom-right diagonal
        if (X[0] == 2 and X[1] == 4) or (X[0] == 4 and X[1] == 6):
            #handles both situations for this diagonal
            if X[0]== 2 and X[1] ==4:
                return X[1]+2
            else:
                return X[0]-2
        #handles X's first two moves being in the same row
        elif X[0] == X[1]-1 or X[0] == X[1]-2:
            #handles both situations for rows
            if X[0] == X[1]-1:
                if X[1] < 3:
                    if X[0] > 0:
                        return X[0]-1
                    else:
                        return X[1]+1
                elif X[1] < 6:
                    if X[0] > 3:
                        return X[0]-1
                    else:
                        return X[1]+1
                else:
                    if X[0] > 6:
                        return X[0]-1
                    else:
                        return X[1]+1
            elif X[0] == X[1]-2:
                return X[1]-1

        elif X[0] == X[1]-3 or X[0] == X[1]-6:
            if X[0] == X[1]-3:
                if X.__contains__(3):
                    if X[0] == 3:
                        return X[0]-3
                    else:
                        return X[1]+3
                elif X.__contains__(4):
                    if X[0] == 4:
                        return X[0]-3
                    else:
                        return X[1]+3
                elif X.__contains__(5):
                    if X[0] == 3:
                        return X[0]-3
                    else:
                        return X[1]+3
            elif X[0] == X[1]-6:
                return X[1]-3
        elif X[0] == X[1]-4:
            if X[0] == X[1]-4:
                if X[0] == 4:
                    return X[0]-4
                else:
                    return X[1]+4
        else:
            if 4 in tiles:
                return 4
            else:
                for item in corners:
                    if tiles.__contains__(item):
                        return item
    #third move for bot
    elif move is 5 or move is 7:
        for item in corners:
            if tiles.__contains__(item):
                return item
        else:
            if tiles.__contains__(4):
                return 4
            else:
                for item in middle:
                    if tiles.__contains__(item):
                        return item

#determines if user/bot can win game in next move, bot uses that number to block path or win
def canIWin(list):
    for key, value in winningCombos.items():
        list.sort()
        value.sort()
        main_list = [item for item in value if item not in list]
        if main_list.__len__() == 1 and main_list[0] in tiles:
            return main_list[0]
    return -1

#prompts the user for the input for their next move
def userMakesDecision():
    print("What's your choice now?")
    print("The choices left are:")
    print(tiles)
    move = input()
    if tiles.__contains__(int(move)):
        if move in corners:
            corners.remove(int(move))
        elif move in middle:
            middle.remove(int(move))
        elif move == 4:
            center = -1
        print("Oh you chose " + move + ", well I guess we can't all be great.")
    else:
        print("Please choose a number within the list below.")
        move = userMakesDecision()
        return int(move)
    return int(move)


def removeTiles(nextMove):
    if int(nextMove) is 4:
        center = -1
    elif int(nextMove) in middle:
        middle.remove(int(nextMove))
    elif int(nextMove) in corners:
        corners.remove(int(nextMove))

    if currentPlayer == 'X':
        X.append(int(nextMove))
        tiles.remove(int(nextMove))
    else:
        O.append(int(nextMove))
        tiles.remove(int(nextMove))

#combinations that can win
winningCombos =  {0: [0, 1, 2], 1: [0, 3, 6], 2: [0, 4, 8], 3: [1, 4, 7], 4: [2, 5, 8], 5: [3, 4, 5], 6: [6, 7, 8], 7: [2, 4, 6]}

#shows the tiles that are left to be chosen
tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#choices for each part of a tic-tac-toe template
corners = [0, 2, 6, 8]
center = 4
middle = [1, 3, 5, 7]

#shows what side has chosen which tiles
X = []
O = []

#round counter
round = 1

#turn counter for each round
turn = 0

#keeps track of current player
currentPlayer = ""

#loops through until the game is complete
while (turn < 9):

#beginning of the game or when
    if turn == 0:
        userChoice = chooseSide()
        print("Round " + str(round))

#current Turn/player
    print("Turn " + str(turn+1))

#determines whether the current player is X or O for both userChoice situations
    if userChoice == 'X':
        if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
            currentPlayer = "O"
        else:
            currentPlayer = "X"
    else:
        if turn == 1 or turn == 3 or turn == 5 or turn == 7:
            currentPlayer = "O"
        else:
            currentPlayer = "X"

#determines whether user has chosen a valid side
    if userChoice != "" and turn == 0:
        firstMove = firstMoves()
        removeTiles(firstMove)
    elif turn == 0:
        print("Type in either 'X' or 'Y'!!!")
        #det
        turn = -1

    #rest of turns for userChoice of X
    if userChoice == 'X':
        #first turn for bot side
        if turn == 1:
            nextMove = nextMoves(currentPlayer, turn, firstMove, X, O)
            removeTiles(nextMove)
            print("I think I caught you with this one, I choose: " + str(nextMove))
        #
        elif turn > 1 and turn < 8 and userChoice == 'X':
            if turn is 2 or turn is 4 or turn is 6:
                nextMove = userMakesDecision()
                removeTiles(nextMove)
            else:
                #determines whether bot side can win game and plays winning tile
                if turn >= 4 and canIWin(O) != -1:
                    nextMove = canIWin(O)
                    print("Hmmmmmm, guess what just happened when I chose " + str(nextMove))
                    print("I WIN AND YOU ARE A LOSER!!!")
                    print("Better luck next time!!!")
                    print("Would you like to play again? Y/N")
                    decision = input()
                    if decision.upper().strip() == 'Y':
                        print("Alright, sounds good. Let's get the ball rolling :D")
                        # shows the tiles that are left to be chosen
                        tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                        # choices for each part of a tic-tac-toe template
                        corners = [0, 2, 6, 8]
                        center = 4
                        middle = [1, 3, 5, 7]

                        # shows what side has chosen which tiles
                        X = []
                        O = []
                        turn = -1
                        round += 1
                    else:
                        print("Alright, well come play against me again soon.")
                        exit()
                else:
                    if turn >= 3 and canIWin(X) != -1:
                        possibleWinByX = canIWin(X)
                        nextMove = possibleWinByX
                        print("I'm going to surprise you with this one, I choose " + str(nextMove))
                        removeTiles(nextMove)
                    else:
                        nextMove = nextMoves(currentPlayer, turn, 9, X, O)
                        print("I'm going to surprise you with this one, I choose " + str(nextMove))
                        removeTiles(nextMove)
        elif turn == 8 and userChoice == 'X':
            nextMove = canIWin(X)
            if nextMove == -1:
                print("The only choice now is " + str(tiles[0]))
                print("I'll choose for you then haha, you choose " + str(tiles[0]))
                print("Looks like this game was a draw. Trying to play again? Y/N")
                choice = input()
                if choice.upper().strip() == "Y":
                    # shows the tiles that are left to be chosen
                    tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                    # choices for each part of a tic-tac-toe template
                    corners = [0, 2, 6, 8]
                    center = 4
                    middle = [1, 3, 5, 7]

                    # shows what side has chosen which tiles
                    X = []
                    O = []
                    turn = -1
                    round += 1
                else:
                    print("Alright, well come play against me again soon.")
                    exit()
    elif userChoice == 'O':
        if turn == 8 and canIWin(X) == -1:
            print("The only choice now is " + str(tiles[0]))
            print("Looks like this game was a draw. Trying to play again? Y/N")
            choice = input()
            if choice.upper().strip() == "Y":
                # shows the tiles that are left to be chosen
                tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                # choices for each part of a tic-tac-toe template
                corners = [0, 2, 6, 8]
                center = 4
                middle = [1, 3, 5, 7]
                # shows what side has chosen which tiles
                X = []
                O = []
                turn = -1
                round += 1
            else:
                print("Alright, well come play against me again soon.")
                exit()
        elif turn == 1 and currentPlayer == 'O':
            firstMove = firstMoves()
            removeTiles(firstMove)
        elif turn > 1:
            if turn == 2:
                nextMove = nextMoves(currentPlayer, turn-1, firstMove, O, X)
                removeTiles(nextMove)
                print("I think I caught you with this one, I choose: " + str(nextMove))
            elif turn is 3 or turn is 5 or turn is 7:
                nextMove = userMakesDecision()
                removeTiles(nextMove)
            elif turn >= 4 and canIWin(X) != -1:
                nextMove = canIWin(X)
                print("Hmmmmmm, guess what just happened when I chose " + str(nextMove))
                print("I WIN AND YOU ARE A LOSER!!!")
                print("Better luck next time!!!")
                print("Would you like to play again? Y/N")
                decision = input()
                if decision.upper().strip() == 'Y':
                    print("Alright, sounds good. Let's get the ball rolling :D")
                    # shows the tiles that are left to be chosen
                    tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                    # choices for each part of a tic-tac-toe template
                    corners = [0, 2, 6, 8]
                    center = 4
                    middle = [1, 3, 5, 7]
                    # shows what side has chosen which tiles
                    ticTacToe = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""}
                    X = []
                    O = []
                    turn = -1
                    round += 1
                else:
                    print("Alright, well come play against me again soon.")
                    exit()
            elif turn >= 4 and canIWin(O) != -1:
                possibleWinByO = canIWin(O)
                nextMove = possibleWinByO
                print("I'm going to surprise you with this one, I choose " + str(nextMove))
                removeTiles(nextMove)
            elif currentPlayer == 'X':
                nextMove = nextMoves(currentPlayer, 5, 9, O, X)
                print("I'm going to surprise you with this one, I choose " + str(nextMove))
                removeTiles(nextMove)
    #rest of turns for userChoice of O
    turn += 1
