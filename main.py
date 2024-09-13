from view import draw_graph
from model.node import Node, State
from model.my_aStar import aStar
from model.board import Board

def main():
  
  initial_state = State(board = Board().solvable_board())
  
  initial_Node = Node(
    parent=None,
    state=initial_state,
    action=None,
    depth=0
  )
  
  print("Initial state:")
  initial_state.board.print_board()
  
  solution_nodes , all_nodes = aStar(initial_state)
  
  draw_graph(all_nodes, solution_nodes)
  
if __name__ == '__main__':
  main()