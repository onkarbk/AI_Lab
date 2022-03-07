a=[]
for i in range(3):
  a.append(['-','-','-'])
def prints():
  for i in range(3):
    for j in range(3):
      print(a[i][j],end=" ")
    print()
prints()
player1='X'
player2='O'
count=0
k=0
r=0
while count<=9:
  x,y=map(int,input("Player1 Enter the position where do u wanna put 'X'?").split())
  a[x][y]=player1
  prints()
  count+=1
  if(a[0][0]==a[1][1] and a[2][2]==a[1][1] and a[0][0]==player1):
    print("Player1 wins")
    k=1
    break
  for i in range(3):
    if(a[i][0]==a[i][1] and a[i][2]==a[i][1] and a[i][0]==player1):
      print("Player1 wins")
      k=1
      break
  for i in range(3):
    if(a[0][i]==a[1][i] and a[2][i]==a[1][i] and a[0][i]==player1):
      print("Player1 wins")
      k=1
      break
  if(a[0][2]==a[1][1] and a[2][0]==a[1][1] and a[2][0]==player1):
    print("Player1 wins")
    k=1
    break
  if(k==1):
    break
  m,n=map(int,input("Player2 Enter the position where do u wanna put 'O'?").split())
  a[m][n]=player2
  prints()
  count+=1
  if(a[0][0]==a[1][1] and a[2][2]==a[1][1] and a[0][0]==player2):
    print("Player2 wins")
    r=1
    break
  for i in range(3):
    if(a[i][0]==a[i][1] and a[i][2]==a[i][1] and a[i][0]==player2):
      print("Player2 wins")
      r=1
      break
  for i in range(3):
    if(a[0][i]==a[1][i] and a[2][i]==a[1][i] and a[0][i]==player2):
      print("Player2 wins")
      r=1
      break
  if(a[0][2]==a[1][1] and a[2][0]==a[1][1] and a[2][0]==player2):
    print("Player2 wins")
    r=1
    break
  if(count==9):
    print("Draw match")