import numpy 
board=numpy.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
player1='X'
player2='O'
chance = 0
j=0
k=0
x=0
y=0
while(chance<9 or x!=0 or y!=0):
    a,b=map(int,input("Player 1  where do u wanna put your 'X'? ").split())
    chance=chance+1
    board[a][b]='X'
    print(board)
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]=='X'):
        print("Player1 wins")
        x=1
        break
    elif(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]=='X'):
        print("Player1 wins")
        x=1
        break
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][0]=='X'):
            print("Player1 wins")
            x=1
            break
    if(x==1):
        break
    for j in range(3):
        if(board[0][j]==board[1][j] and board[1][j]==board[2][j] and board[0][j]=='X'):
            print("Player1 wins")
            x=1
            break
    if(x==1):
        break
            
    c,d=map(int,input("Player 2  where do u wanna put your 'O'? ").split())
    board[c][d]='O'
    chance=chance+1
    print(board)
    i=0
    j=0
    k=0
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]=='O'):
        print("Player2 wins")
        y=1
        break
    elif(board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]=='O'):
        print("Player2 wins")
        y=1
        break
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][0]==board[i][2] and board[i][0]=='O'):
            print("Player2 wins")
            y=1
            break
    if(y==1):
        break
    for j in range(3):
        if(board[0][j]==board[1][j] and board[1][j]==board[2][j] and board[0][j]=='O'):
            print("Player2 wins")
            y=1
            break
    if(y==1):
        break
if(chance>=9):
    print("Match withdraw")
    
