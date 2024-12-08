import random

print('TIC TAC TOE \nInstructions:1.Player plays first.\n2.Player is denoted by X and computer by O\n3.Player is supposed to input the number of the position it wants to place the mark on\n')
board='  {}|{}|{}\n -------\n  {}|{}|{}\n -------\n  {}|{}|{}'
print(board.format('1','2','3','4','5','6','7','8','9'))

inputs=['1','2','3','4','5','6','7','8','9']
#GAME STARTS
while True:
  while True: #the whole point of this loop is to get a valid input in the inputs list and nothing else it terminates after doing so
    i = input('player X pick number ')
    if i in inputs:
        i2 = inputs.index(i)
        inputs[i2] = 'X'
        break
    else:
        print('invalid input')
  print(board.format(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7], inputs[8])) #prints board after a valid input is taken
  if (inputs[0] == inputs[1] == inputs[2] or inputs[3] == inputs[4] == inputs[5] or inputs[6] == inputs[7] == inputs[8] or inputs[0] == inputs[3] == inputs[6] or inputs[1] == inputs[7] == inputs[4] or inputs[2] == inputs[5] == inputs[8]) or inputs[0] == inputs[4] == inputs[8] or inputs[4] == inputs[2] == inputs[6]:
      print('PLAYER X WINS!') #the above is one of the winning conditions hence termination of the whole loop takes place
      break
#1st possibility is that wins
  c=0
  for a in inputs:
      if a!='X' and a!='O':
          c=c+1
  if c==0:
      print('GAME ENDS IN A TIE')
      break
#2nd possibility is a tie neither of them win

  while True:
      i = str(random.randint(1, 9))
      if i in inputs:
          i2 = inputs.index(i)
          inputs[i2] = 'O'
          break
  print('now computers turn')
  print(board.format(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], inputs[7],
                     inputs[8]))  #basically now we print the established move of the computer
  #now we print the winning condition for the computer
  if (inputs[0] == inputs[1] == inputs[2] or inputs[3] == inputs[4] == inputs[5] or inputs[6] == inputs[7] == inputs[
      8] or inputs[0] == inputs[3] == inputs[6] or inputs[1] == inputs[7] == inputs[4] or inputs[2] == inputs[5] ==
      inputs[8]) or inputs[0] == inputs[4] == inputs[8] or inputs[4] == inputs[2] == inputs[6]:
      print('computer wins')
      break
#3rd possibility that the computer wins