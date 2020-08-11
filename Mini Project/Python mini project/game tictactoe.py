board = [[1,2,3],[4,5,6],[7,8,9]]


def DisplayBoard(board):
  for i in board: 
    print('+-------+-------+-------+')
    print('|       |       |       |')  
    print('|   '+str(i[0])+'   |   '+str(i[1])+'   |   '+str(i[2])+'   |') 
    print('|       |       |       |')                                     
  print('+-------+-------+-------+')                   

#user move function
def EnterMove(board):
  vacant = False 
  while not vacant:
    move = int(input('Enter your move:')) 
    row = int((move-1)/3) # indeks_baris
    col = (move-1)%3      # indeks_kolom
    if (board[row][col] != 'X' and board[row][col] != 'O') and ( 0 < move and move < 10): 
      board[row][col] = 'O' # Memasukan move pilihan user
      vacant = True

def MakeListOfFreeFields(board):
  free = [] 
  for i in range(1,10):
      row = int((i-1)/3) 
      col = (i-1)%3      
      if board[row][col] != 'X' and board[row][col] != 'O': 
        free.append((row,col)) 
  return free

def VictoryCheck(board, sign):
  win = False  
  for i in board: 
    if i[0] == i[1] == i[2]: 
      win = True
  board_t = [list(x) for x in zip(*board)] 
  for i in board_t:
    if i[0] == i[1] == i[2]: 
      win = True
  if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]: 
    win = True

  if win: 
    if sign == 'O':
      print('You Won')
    else:
      print('Computer Won')
  return win

#comp move function
def DrawMove(board):
  from random import randrange
  if board[1][1] == 5: 
    row = 1
    col = 1
  else:
    vacant = False 
    while not vacant:
      row = randrange(0,3) 
      col = randrange(0,3) 
      if (row,col) in MakeListOfFreeFields(board): 
        vacant = True
  board[row][col] = 'X'

#game play
i = 0  
won = False  
while MakeListOfFreeFields(board) != [] and not won and i < 10:
    if i % 2 == 0: # Computer Move
        DrawMove(board)
        DisplayBoard(board) 
        won = VictoryCheck(board, 'X')
    else:          # User Move
        EnterMove(board)
        DisplayBoard(board)
        won = VictoryCheck(board, 'O')
    i += 1

if not won: # Jika turn sudah lebih dari 10, berarti sudah tidak ada kotak kosong, tetapi tidak ada yang menang, berarti permainan berakhir
  print('Draw')
