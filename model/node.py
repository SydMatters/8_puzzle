'''
This is the solution for the 8-puzzle problem using the A* algorithm.
Without using the library simpleAI.
'''
from __future__ import annotations
from model.board import Board
from dataclasses import dataclass, field
from copy import deepcopy

import time 


@dataclass
class Time:
  start : float = time.time()

  def elapse(self):
    return time.time() - self.start

"""
This class represents the state of the 8-puzzle board. Each state has a board and a board_len.

Attributes:
  board (board): 8-puzzle board
  board_len (int): length of the board
  
Methods:
  find_0(): Finds the position of the 0 in the board
  is_valid(x, y): Checks if the position (x, y) is valid
  is_goal(): Checks if the board is the goal board
  successors(): Generates the possible moves from the current state
"""
@dataclass
class State:
  board : Board = field(default_factory=lambda: Board().solvable_board())
  board_len : int = 3
  
  def find_0(self):
    for i in range(self.board_len):
      for j in range(self.board_len):
        if self.board.board[i][j] == 0:
          # Return the position of the 0
          return i, j
  
  def is_valid(self, x, y):
    # A move is valid if the position is inside the board
    return 0 <= x < self.board_len and 0 <= y < self.board_len
    
  def is_goal(self):
    return self.board.board == Board().goal_board()
  
  def successors(self):
    # Find the position of the 0
    (x_zero,y_zero) = self.find_0()
    # Possible moves
    directions = {
      'up' : (-1,0),
      'down' : (1,0),
      'left' : (0,-1),
      'right' : (0,1)
    }
    
    # Generate the possible moves, the foor loop iterates over the directions in the list of tuples called directions
    for action, (directionX, directionY) in directions.items():
      # Calculate the new position, each one is the current position plus the direction
      new_x, new_y = x_zero + directionX, y_zero + directionY
      # If the move is valid, create a new board and a new state
      if self.is_valid(new_x, new_y):
        # Create a new board using the deepcopy function that creates a new object with the same value
        new_board = deepcopy(self.board.board)
        # Swap the values of the current position and the new position
        new_board[x_zero][y_zero], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x_zero][y_zero]
        # Create a new state with the new board
        new_state = State(board= Board(board = new_board))
        # Create the action
        action = f'{action}'
        #yiel for the action and the new state, this makes the function a generator
        yield action, new_state
        
    
  
"""
This class represents a node in the search tree. Each node has a parent, a state, an action, and a depth.

Attributes:
  parent (Node): parent node
  state (State): state of the node
  action (str): action to reach the node
  depth (int): depth of the node
  
Methods:
  expand(): Expands the node
  extract_solution(): Extracts the solution from the node
"""
@dataclass
class Node:
  parent : Node
  state  : State
  action : str
  depth  : int

  def expand(self):
    # Generate the possible moves from the current state, remember that the successors function is a generator
    for (action, succ_state) in self.state.successors():
      # Create a new node with the parent, the state, the action, and the depth
      succ_node = Node(
        parent = self,
        state = succ_state,
        action = action,
        depth=self.depth + 1)
      # Yield the new node
      yield succ_node

  def extract_solution  (self):
    # Create a list to store the solution
    solution = []
    # Create a node to store the current node
    node = self
    # While the parent is not None, append the node to the solution and update the node to the parent
    while node.parent is not None:
      solution.append(node)
      node = node.parent
    # Reverse the solution and return it, because the solution is from the goal to the initial state
    solution.reverse()
    return solution
  






