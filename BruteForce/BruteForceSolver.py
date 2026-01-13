"""
Brute force calculate the EV by building the optimal-play graph.

MEMORY WARNING: The spacial complexity is exponential.
Start with small values!
"""
from BruteForce.TreeBasics import OptimalSnakeTree
from GridsAndGraphs.Adjacencies import find_grid_adjacency




class BruteForceSolver_Template(OptimalSnakeTree):
    def __init__(self, adjacency):
        super().__init__(adjacency)
        self.build_optimal_graph()
        self.name = 'BruteForce'
    
    def start_new_game(self, start):
        self.current_node = self.root.children[start]

    def find_path(self, apple):
        path = []
        temp_node = self.current_node
        while True:
            temp_node = temp_node.apple_to_move[apple]
            if temp_node.value == apple:
                self.current_node = temp_node
            yield temp_node.value
    

class GridSolver_BruteForce_Full(BruteForceSolver_Template):
     def __init__(self, m, n):
        super().__init__(find_grid_adjacency(m, n))
        self.name += ' Full'


from GridsAndGraphs.Adjacencies import find_grid_adjacency_dive
class GridSolver_BruteForce_Dive(BruteForceSolver_Template):
     def __init__(self, m, n):
        super().__init__(find_grid_adjacency_dive(m, n))
        self.name += ' Dive'


class GridSolver_BruteForce(BruteForceSolver_Template):
     def __init__(self, adjacency):
        super().__init__(adjacency)