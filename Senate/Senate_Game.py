import random as rand;


#make the board: 
def boardcreate():
    rows, cols = (3, 10)
    board = [['0' for i in range(cols)] for j in range (rows)]

    #Baord set up for pieces:
    for x in range (0 , 10):
        if x % 2== 0:
            #make the white pieces
            board[0][x] = (str)((int)(x/2)+1) +'W'
        else:
            #make the black pieces
            board[0][x] = (str)((int)((x-1)/2)+1)+'B'
    return board


# prints the board line by line
def printboard(board):
    rows= len(board)
    #print ("rows: " + str(rows))

    cols = len(board[0])
    #print("cols: " + str(cols))

    curline = [cols] 
    for i in range(rows):
        curline = board[i]
        print(curline)


#checks the position of a give piece on the board and returns the pos in a tuple. if it's not found return 11,11
def findpiece(board, piece):
    rows= len(board)
    cols = len(board[0])
    #debug check: print("Rows: " + str(rows) + "Cols: " + str(cols))
    piecepos = 11, 11
    for i in range(cols):
        for j in range(rows):
            #debug check: 
            #print( str(j) + str(i))
            #print(board[j][i])
            checkpiece = board[j][i]
            if checkpiece == piece:
                piecepos = j, i
    #print (piecepos)
    return piecepos


# roll a 5 sided dice for turn
def roll():
    return rand.randrange(1,6)


#Calculate what the valid board location is for moving a piece or move it off the board5
def calculatemove(startpos, moveval):
    startposx = int(startpos[0])
    startposy = int(startpos[1])
    print(startpos)
    print(moveval)
    
    print(startpos)
    if startposy + moveval >= 10:
        if startposx + 1  >= 3:
            print("piece is off board")
            dest = 11,11
            return dest
        else:
            startposx += 1
            startposy -= 10
            startposy += moveval
            #Debug for positions: 
            #print(startposx)
            dest = startposx , startposy
            return dest
    else:
        startpos = startposx, startposy +moveval
        dest = startpos
        return dest


#check what is in a designated location
def locationcheck(board, location):
    return board[location[0]][location[1]]
 

def validmove(board, piece, destpos,):
    print(destpos)
    checkspace = board[destpos[0]][destpos[1]]
    if len(checkspace) > 1:
        if checkspace[1] == piece[1]:
            print("you have a piece on your team there.")
            return False
        elif checkspace[1] != piece[1]:
            print("swaping enemy piece with your own.")
            return True 
    else:
        print(" moving the piece the designated distance.")
        return True


#calculates and performs a move on a piece
def move_piece(board, piece, move, player):
    endstate = True
    scorechange = 0
    if move == 0:
        move = roll()
    print( str(move) + " sticks came color side up!")
    piece = input("What piece would you like to move?  ")
    if piece == "end":
        endstate = False
        return board, endstate, scorechange
    #find where the piece you want to move is and if it exists
    printboard(board)
    startpos =  findpiece(board, piece)
    if startpos[1] == 11:
        print("That piece does not exist on thee board! Select a different piece to move.")
        board, endstate, scorechange  = move_piece(board, piece, move, player)
    elif piece[1] != player[0]:
        print("this is not your piece to move! Select one of your pieces to move.")
        board, endstate, scorechange  = move_piece(board, piece, move, player)
    else:
        #calculate where piece is trying to move
        destpos = calculatemove(startpos, move)
        #check for off board move
        if destpos[1] == 11 :
            print("you moved the piece off the board and have gained a point")
            board[startpos[0]][startpos[1]] = '0'
            scorechange = 1
            return board, endstate, scorechange
        elif validmove(board, piece,destpos):
            #print("Test: found a valid move")
            holdpiece = board[destpos[0]][destpos[1]]
            board[destpos[0]][destpos[1]] = piece
            #Debug Board moves
            #printboard(board)
            board[startpos[0]][startpos[1]] = holdpiece
            #Debug Board moves
            #printboard(board)
            return board, endstate, scorechange
        else:
            print("select a different piece to move.")
            board, endstate, scorechange = move_piece(board, piece, move, player)

    return board, endstate, scorechange


board = boardcreate()
player1= "W6"
player2= "B6"
playerscore1 = 0
playerscore2 = 0
#printboard(board)

#random move
#calculatemove(board, [rand.randrange(len(board)),rand.randrange(len(board[0]))], roll())

#establish loop end state bool value
endstate = True
printboard(board)
gofirst = rand.randint(0,1)
if gofirst == 1:
    player = player1
    print("Player 1 = W")
else:
    player = player2
    print("Player 1 = B")
print (gofirst)

while (endstate):

    #create the loop start variables
    proll = 0 
    piece = "1M"
    scorechange = 0
    #conduct a move
    board, endstate, scorechange = move_piece(board, piece, proll, player)
    #Check for score changes
    if player == player1:
        playerscore1 +=scorechange
    elif player == player2:
        playerscore2 += scorechange
    #change the player over.
    if player == player1: 
        player = player2
    else: 
        player = player1
    printboard(board)
    print("player 1 score = " + str(playerscore1))
    print("player 2 score = " + str(playerscore2))
    if playerscore1 == 5:
        print("Player 1 Wins!")
        endstate = False
        break
    if playerscore2 == 5:
        print("Player 2 Wins!")
        endstate = False
        break




