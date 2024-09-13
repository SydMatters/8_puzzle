from graphviz import Digraph

from model.node import Node

def draw_graph(nodes : list[Node], solution_nodes : list[Node]):
  dot = Digraph(comment='8 puzzle A* search')
  
  dot.attr(fontzie='25', font = 'bold')
  
  for node in nodes:
    parent = node.parent
    current_board = format_board(node.state.board.board)
    if node == nodes[0]:
        dot.node(current_board, current_board, color='blue', style='filled', fillcolor='lightblue')
    if node in solution_nodes:
      if node == solution_nodes[-1]:
        dot.node(current_board, current_board, color='green', style='filled', fillcolor='lightgreen')
      else:
        dot.node(current_board, current_board, color='red', style='filled', fillcolor='lightcoral')
    else:
      dot.node(current_board, current_board)
    
    if parent is not None:
      parent_board = format_board(parent.state.board.board)
      if node in solution_nodes:
        dot.edge(parent_board, current_board, color='red', label=str(node.action), fontcolor='red') 
      else:
        dot.edge(parent_board, current_board, label=str(node.action)) 
        
  dot.render('search_tree', format='png')

def format_board(board : list[list[int]]) -> str:
  return "\n".join([" ".join([str(cell) for cell in row]) for row in board])
