from __future__ import annotations
from .node import Node, State, Time
from .board import Board


import heapq
import itertools

start = Time()

def manhattan_distance(state : State) -> int:
  """Heuristic based on manhattan distance algorithm, for the a* search

  Args:
      state (State): current state

  Returns:
      int: heuristic value
  """ 
  
  #Declaration of variables for the goal Board
  goal_positions = {}
  goal_board = Board().goal_board()
  
  #Get the position of the goal board
  for i in range (state.board_len):
    for j in range(state.board_len):
      goal_positions[goal_board[i][j]] = (i,j)
  #Declaration of the distance variable to store the distance for heuristic    
  distance = 0
  
  #Get the position of the current board
  for i in range(state.board_len):
    for j in range(state.board_len):
      #Get the value of the current board
      value = state.board.board[i][j]
      #If the value is not 0, calculate the distance
      if value != 0:
        #Get the position of the goal board
        goal_x, goal_y = goal_positions[value]
        #Calculate the distance between the current board and the goal board
        distance += abs(i - goal_x) + abs(j - goal_y)
  
  return distance

"""
This function implements the A* algorithm

Args:
    initial_state (State): initial state
"""
def aStar(initial_state: State):
  # Create the root node
  root = Node(
      parent=None,
      state=initial_state,
      action=None,
      depth=0
  )
  # Create a counter to break ties in the priority queue
  counter = itertools.count()
  # Create the frontier, a priority queue
  frontier = []
  all_nodes = []
  # Push the root node to the frontier, the tuple has the f value, the counter and the node
  heapq.heappush(frontier, (0, next(counter), root))  # Push a tuple with (f, count, node)
  # Create the explored set
  
  all_nodes.append(root)
  explored = set()

# While the frontier is not empty
  while frontier:
    # Pop the node with the lowest f, cuz is a priority queue
      _, _, current_node = heapq.heappop(frontier)  # Pop the node with the lowest f

      # If the current node is the goal, return the solution
      if current_node.state.is_goal():
          return current_node.extract_solution(), all_nodes

      # Add the current node to the explored set, the node is a tuple of tuples, the set only accepts unique values
      explored.add(tuple(map(tuple, current_node.state.board.board)))

      # Expand the current node
      for succ_node in current_node.expand():
        # If the node is not in the explored set
        if tuple(map(tuple, succ_node.state.board.board)) not in explored:
            g = succ_node.depth  # Depth is the g(n)
            h = manhattan_distance(succ_node.state)  # Heuristic h(n)
            f = g + h 
            # Push the node to the frontier
            heapq.heappush(frontier, (f, next(counter), succ_node))  # Push (f, count, node)
            all_nodes.append(succ_node)
  return None

  
  