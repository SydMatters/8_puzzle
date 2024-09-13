from dataclasses import dataclass, field
import random

"""
Represents an 8-puzzle board

Attributes:
  board (list): 3x3 board
  inversions (int): number of inversions in the board
  
Methods:
  randomize_board(): Randomizes the board
  count_inversions(): Counts the number of inversions in the board
  is_solvable(): Checks if the board is solvable
  solvable_board(): Generates a solvable board
  goal_board(): Returns the goal board
  print_board(): Prints the board
  """
@dataclass
class Board:
  board : list = field(default_factory=lambda: [[1,2,3],[4,5,6],[7,8,0]])
  inversions : int = 0

  def randomize_board(self):
    # Flatten the board and shuffle it
    board_flat = [item for sublist in self.board for item in sublist]
    random.shuffle(board_flat)
    # Reshape the board
    self.board = [board_flat[i:i+3] for i in range(0, len(board_flat), 3)]

  def count_inversions(self):
    # Flatten the board
    board_flat = [item for sublist in self.board for item in sublist]
    # Count the number of inversions
    for i in range(len(board_flat)):
      for j in range(i+1, len(board_flat)):
        # An inversion is when a larger number precedes a smaller number with the blank space
        if board_flat[i] > board_flat[j] and board_flat[i] != 0 and board_flat[j] != 0:
          self.inversions += 1
  
  def is_solvable(self):
    # If the board is even and the number of inversions is odd, the board is solvable
    if self.inversions % 2 == 0 and self.inversions != 0:
      return True
    return False
  
  def solvable_board(self):
    # Generate a solvable board
    while True:
      # Randomize the board and count the inversions, if it is solvable, return the board.
      # Otherwise, repeat the process, thats why the inversions get reset to 0 every time
      self.inversions = 0
      self.randomize_board()
      self.count_inversions()
      if self.is_solvable():
        return self
  
  def goal_board(self):
    return [[1,2,3],[4,5,6],[7,8,0]]
  
  def print_board(self):
    for i in range(3):
      for j in range(3):
        print(self.board[i][j], end=' ')
      print()
    print()



