board = {
    "A": [".",".","."],
    "B": [".",".","."],
    "C": [".",".","."]
}

def printBoard(board):
    print("\nCurrenct Board\n")
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])

def battleship(board):
    print("\nWelcome to Battleship!\n")
    shipCol = input("Player 1, select a column for your battleship: ")
    shipRow = int(input("Player 1, select a row for your battleship: ")) -1
    printBoard(board)
    count = 0;
    while(True):
        guessCol = input("\nPlayer 2, select a column to check: ")
        guessRow = int(input("Player 2, select a row to check: ")) -1
        count += 1
        if((guessCol == shipCol) and (guessRow == shipRow)):
            print("\nYou won!")
            board[guessCol][guessRow] = "!"
            printBoard(board)
            print("\nScore:", count, " Guesses\n")
            break
        else:
            print("\nSorry, nothing there")
            board[guessCol][guessRow] = "x"
            printBoard(board)




battleship(board)