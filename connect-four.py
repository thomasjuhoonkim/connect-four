rows = 6
columns = 7
board = [[" "] * columns for _ in range(rows)] #row major array

#functions for printing the board
def printSepRowLine():
  for column in range(columns):
    print("+---", end="")
  print("+", end="")
  print()
def printSepColLineBlank():
  for column in range(columns):
    print("|   ", end="")
  print("|")
def printSepColLine(row):
  printSepColLineBlank()
  for column in range(columns):
    print("| " + str(board[row][column]) + " ",end="")
  print("|")
  printSepColLineBlank()
def printBoard():
  for column in range(columns):
    print("  " + str(column+1) + " ", end="")
  print()
  for row in range(rows):
    printSepRowLine()
    printSepColLine(row)
  printSepRowLine()

#functions for placing the player on the board
def playerTurn(turnNum):
  if turnNum % 2 == 0: player = "X"
  else: player = "O"
  return player
def emptySlotNum(chosenColumn):
  for row in range(rows):
    if board[row][chosenColumn] == "O" or board[row][chosenColumn] == "X": return row - 1
  return rows - 1
def placePlayerInColumn(player, chosenColumn):
  board[emptySlotNum(chosenColumn)][chosenColumn] = player  
def isValidInput(player, chosenColumn):
  validInput = True
  if player != "X" and player != "O":
    print("Make sure to use either an 'X' or 'O' as your piece")
    validInput = False
  elif chosenColumn < 0 or chosenColumn > columns:
      print("Make sure to pick a column between 1 and " + str(columns))
      validInput = False
  elif emptySlotNum(chosenColumn) < 0:
    print("Make sure to pick a column between 1 and " + str(columns) + " that is not full")
    validInput = False
  return validInput

#functions for checking for the winner
def checkHorizontal():
  for row in range(rows):
    for column in range(columns - 3):
      if board[row][column] == "X" or board[row][column] == "O":
        if board[row][column] == board[row][column + 1] and board[row][column] == board[row][column + 2] and board[row][column] == board[row][column + 3]:
          return True
      else: continue
def checkVertical():
  for column in range(columns):
    for row in range(rows - 3):
      if board[row][column] == "X" or board[row][column] == "O":
        if board[row][column] == board[row + 1][column] and board[row][column] == board[row + 2][column] and board[row][column] == board[row + 3][column]:
          return True
      else: continue
def checkDiagonalForward(): #/-direction
  for row in range(3, rows):
    for column in range(columns - 3):
      if board[row][column] == "X" or board[row][column] == "O":
        if board[row][column] == board[row - 1][column + 1] and board[row][column] == board[row - 2][column + 2] and board[row][column] == board[row - 3][column + 3]:
          return True
      else: continue
def checkDiagonalBackward(): #\-direction
  for row in range(rows - 3):
    for column in range(columns - 3):
      if board[row][column] == "X" or board[row][column] == "O":
        if board[row][column] == board[row + 1][column + 1] and board[row][column] == board[row + 2][column + 2] and board[row][column] == board[row + 3][column + 3]:
          return True
      else: continue
def checkWin():
  status = False
  if checkHorizontal() == True: status = True
  if checkVertical() == True: status = True
  if checkDiagonalForward() == True: status = True
  if checkDiagonalBackward() == True: status = True
  return status

turnNum = 0
gameEnd = False
printBoard()
while gameEnd == False:
  validInput = False
  while validInput == False:
    player = playerTurn(turnNum)
    print("It is " + player + "'s turn. Please select a column.")
    chosenColumn = int(input("Your options are " + str(list(range(1, columns + 1))) + ": ")) - 1
    validInput = isValidInput(player, chosenColumn)
  placePlayerInColumn(player, chosenColumn)
  print("Placed an " + player + " in column " + str(chosenColumn + 1))
  printBoard()
  if checkWin() == True:
    gameEnd = True
    print("=============================")
    print("Player " + player + " wins!")
    print("Game won in " + str(turnNum + 1) + " turns")
    print("=============================")
  turnNum += 1