import random

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '
            }

print("Use numpad to play tic tac toe.")

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
'''
def checkxoForRandom(turn):
    if turn == 'X':
        move = input()
        return move
    else:
        move = random.randint(1,9)
        move = str(move)
        return move
        '''


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn " + turn + ". Move to which place?")

        #move = checkxoForRandom(turn)
        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Already filled!!!! put number again!!!!!")
            continue

        #check if X or O has won
        if count >= 5 and count < 9:
            #landscape
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break

            #vertical
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print('\nGAME OVER\n')
                print(turn + " WON!!")
                break
        #tie!!
        if count == 9:
            print("Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play again? (y/n): ")
    if restart == 'y':
        for re in theBoard:
            theBoard[re] = " "
        game()
    elif restart == 'n':
        exit()


game()

