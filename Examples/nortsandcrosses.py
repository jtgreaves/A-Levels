import time

 

 

winningPos = [[0,1,2], [3,4,5], [6,7,8], # horizontal

              [0,3,6], [1,4,7], [2,5,8], # vertical

              [0,4,8], [2,4,6]] # diagonal

 

def drawGrid(grid):

               x = 0

               output=""

               while x<len(grid):

                              temp = " "

                             

                              if grid[x] == 1:

                                             temp="O"

                              elif grid[x] == 2:

                                             temp="X"

                              if x % 3 == 1:

                                             output+= "  | "+temp+" |"

                              else:

                                             output+= temp

                              if x % 3 == 2 and x != 8:

                                             output+= "\n----------"

                                             print(output)

                                             output=""

              

                              x = x + 1

               print(output)

def manageAIGo(grid):

               # we are about to do the maxMin algorithim

               # Max = the best move for the AI

               # min = the best move for the Player

               # assumption - we assume the player will always make the best move!!

               if playerWin(grid) == 0:

                              copyOfGrid = list(grid) # Correct way of copying a list! Normal assignment will not work.

                              grid[ maxMove(copyOfGrid)[1]] = 2

 

def generateMoves(currentGrid):

               x = 0

               moves = []

               while x<len(currentGrid):

                              if currentGrid[x] == 0:

                                             moves.append(x)

                              x = x + 1

               return moves

 

def maxMove(g):

               # max move looks for the best move for the AI

               moves = generateMoves(g)

               bestMoveScore = None # low value so it will be replaced!

               bestMove = None

               for moveToTest in moves:

                              # apply the AI move

                              g[moveToTest] = 2 # x is 2

                              newGameState = playerWin(g)

                              if newGameState != 0:

                                             score = calculateScore(g)

                              else:

                                             score,tempMove = minMove(g)

                              g[moveToTest] = 0 # undo the move, reset the board !IMPORTANT!

 

                              if bestMoveScore == None or score > bestMoveScore:

                                             bestMove = moveToTest

                                             bestMoveScore = score

                             

               return bestMoveScore, bestMove # instead of using OO I am using a python cheat to return two values

 

 

def minMove(g):

              

               # min will look for the best move for the player

               moves = generateMoves(g)

               bestMoveScore = None # low value so it will be replaced!

               bestMove = None

               for moveToTest in moves:

                              # apply the AI move

                              g[moveToTest] = 1 # o is 1

                              newGameState = playerWin(g)

                              if newGameState != 0:

                                             score = calculateScore(g)

                              else:

                                             score,tempMove = maxMove(g)

                             

                              g[moveToTest] = 0 # undo the move, reset the board !IMPORTANT!

 

                              if bestMoveScore == None or score < bestMoveScore:

                                             bestMove = moveToTest

                                             bestMoveScore = score

                             

               return bestMoveScore, bestMove # instead of using OO I am using a python cheat to return two values

 

 

def calculateScore(g):

               state = playerWin(g)

               if state == 1:

                              return -1

               elif state == 2:

                              return 1

               else:

                              return 0

 

def managePlayerGo(grid):

               print ("")

               go = int(input("What position do you want?"))

               while go < 0 or go >=9:

                              print ("invalid move")

                              go = int(input("What position do you want?"))

               while grid[go] != 0:

                              print ("invalid move")

                              go = int(input("What position do you want?"))

              

               grid[go] = 1

# returns 0 if no win

# returns 1 if o wins

# returns 2 if x wins

# returns -1 if it is a draw

 

# this is the evaluation function

 

def playerWin(grid):

               for winline in winningPos:

                              xplay = 0

                              oplay = 0

                              for pos in winline:

                                             if grid[pos] == 1:

                                                            oplay += 1

                                             elif grid[pos] == 2:

                                                            xplay += 10

                             

                              if oplay == 3:

                                            

                                             return 1 # o has won

                              if xplay == 30:

                                            

                                             return 2

              

               # check for draw

               draw = True

               for pos in grid:

                              if pos == 0:

                                             draw = False

                                             break

               if draw:

                             

                              return -1

               else:

                              return 0

                             

again = "y"

while again == "y" or again == "Y":

               grid = [0,0,0,0,0,0,0,0,0]

               drawGrid(grid)

               while playerWin(grid) == 0:

                              managePlayerGo(grid)

                              manageAIGo(grid)

                              drawGrid(grid)

               if playerWin(grid) == -1:

                              print ("draw")

               elif playerWin(grid) == 1:

                              print ("o wins")

               elif playerWin(grid) == 2:

                              print ("x wins")

               else:

                              print ("ERRORZ")

               again = input("Again y/n? -")
