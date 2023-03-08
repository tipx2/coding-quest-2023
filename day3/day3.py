with open("day3/input3.txt") as f:
   lines = f.readlines()

def check_winner(boardstate):
    for line in boardstate:
        if len(set(line)) == 1 and 0 not in line:
            return line[0]
    
    for x in range(len(boardstate)):
        col = set([boardstate[0][x], boardstate[1][x], boardstate[2][x]])
        if len(col) == 1 and 0 not in col:
            return boardstate[0][x]

    diagonal1 = set([boardstate[0][0], boardstate[1][1], boardstate[2][2]])
    diagonal2 = set([boardstate[0][2], boardstate[1][1], boardstate[2][0]])

    if len(diagonal1) == 1 and 0 not in diagonal1:
        return boardstate[0][0]
    
    if len(diagonal2) == 1 and 0 not in diagonal2:
        return boardstate[0][2]


xtotal = 0
ototal = 0


for line in lines:
    xturn = True
    boardstate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for move in line.strip("\n").split(" "):
        x, y = divmod(int(move)-1, 3)
        if xturn:
            boardstate[x][y] = "X"
            if check_winner(boardstate) == "X":
                xtotal += 1
                break
        else:
            boardstate[x][y] = "O"
            if check_winner(boardstate) == "O":
                ototal += 1
                break
    
        xturn = not xturn

drawtotal = len(lines) - (xtotal + ototal)

print(xtotal * ototal * drawtotal)