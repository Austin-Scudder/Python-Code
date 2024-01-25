import random as rand;

#test Comment
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
    rows= 3
    cols = 10
    curline = [10] 
    for i in range(rows):
        curline = board[i]
        print(curline)


#checks the position of a give piece on the board and returns the pos in a tuple. if it's not found return 11,11
def findpiece(board, piece):
    rows= len(board)
    cols = len(board[0])
    piecepos = 11, 11
    for i in range(cols):
        for j in range(rows):
            if board[j][i] == piece:
                piecepos = j, i
    #print (piecepos)
    return piecepos


# roll a 5 sided dice for turn
def roll():
    return rand.randrange(1,6)


#Calculate what the valid board location is for moving a piece or move it off the board
def calculatemove(startpos, moveval):
    print(startpos)
    print(moveval)
    startpos[1] += moveval
    print(startpos)
    if startpos[1] >= 10:
        if startpos[0] >= 3:
            print("piece is off board")
            dest = 11,11
            return dest
        else:
            startpos[0] += 1
            startpos[1] -= 10
            print(startpos)
            dest = startpos
            return dest
    else:
        startpos[1] += moveval
        dest = startpos
        return dest


#check what is in a designated location
def locationcheck(board, location):
    return board[location[0]][location[1]]
 

def validmove(board, destpos, player):
    checkspace = board[destpos[0]][destpos[1]]
    if checkspace[1] == player[0]:
        print("you have a piece on your team there")
        return False
    elif checkspace[1] == 0:
        print("moving the piece the designated distance")
        return True 
    else:
        print("swaping enemy piece with your own")
        return True


#calculates and performs a move on a piece
def move_piece(board, piece, move, player):

    #find where the piece you want to move is and if it exists
    startpos = findpiece(board, piece)
    if startpos[1] == 11:
        print("That piece does not exist on the board! Select a different piece to move.")
        #move_piece(board, piece, move)
    elif piece[1] != player[0]:
        print("this is not your piece to move! Select one of your pieces to move.")
        #move_piece(board, piece, move)
    else:
        #calculate where piece is trying to move
        destpos = calculatemove(startpos, move)
        if destpos[1] == 11:
            print("you moved the piece off the board and have gained a point")
            board[startpos[0]][startpos[1]] = '0'
            player[1] = str(int(player[1]) + 1)
            return board, player[0]
        elif validmove(board, piece,destpos):
            holdpiece = board[destpos[0]][destpos[1]]
            board[destpos[0]][destpos[1]] = piece
            board[destpos[0]][destpos[1]] = holdpiece
            return board
        else:
            print("select a different piece to move.")
            #move_piece(board, piece, move)

    return board


board = boardcreate()
player1= "W0"
player2= "B0"
#printboard(board)

#random move
#calculatemove(board, [rand.randrange(len(board)),rand.randrange(len(board[0]))], roll())

#establish loop end state bool value
endstate = not True

while (endstate):
    endstate = True





